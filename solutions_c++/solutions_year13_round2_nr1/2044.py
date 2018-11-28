#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <iomanip>
#include <sstream>
#include <cstring>
#include <cmath>
#include <deque>
#include <cassert>

using namespace std;

typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<string> vs;
typedef vector<bool> vb;
typedef long long int ll;
typedef deque<ll> vll;

int main()
{
    int T,N;
    ll A;

    cin>>T;

    for(int c=1;c<=T;c++){

        cin>>A>>N;
        vll mo(N,0);

        for(int i=0; i<N;i++){
            cin>>mo[i];

        }

        sort(mo.begin(),mo.end());

        ll best = N, cur = 0;
        ll pt = A;
        ll iter = 0;

        if(pt > 1){

        while(!mo.empty()){

            iter = 0;

            while( !mo.empty() && pt > mo[0] ){

                pt += mo[0];
                //iter++;
                mo.pop_front();
            }

            //cur += iter;

            if( (ll)(cur+mo.size()) > 10*N){

                break;
            }

            best = min(best,(ll)(cur+mo.size()));

            if(!mo.empty()){

                assert(pt <= mo[0]);
                assert(pt-1 > 0);

                if(pt-1 > 0){

                    pt += min((ll)(pt-1),(ll)10000000);
                    cur++;
                }


                //pt = mo[0]+1;
            }








        }

        }


        cout<<"Case #"<<c<<": "<<best<<endl;


    }

    return 0;
}

