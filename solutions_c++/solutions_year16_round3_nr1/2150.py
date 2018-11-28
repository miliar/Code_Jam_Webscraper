#include <iostream>
#include <bitset>
#include <cmath>
#include <algorithm>
#include <cstdlib>
#include <functional>
#include <numeric>
#include <vector>
#include <set>
#include <map>
#include <climits>

using namespace std;

typedef unsigned long long int ulli;
typedef long long int lli;

void test_large(){

}


void test_small(){

    int T;
    cin>>T;

    for(int c=1; c<=T; c++){

        int N;
        cin>>N;
        vector<int> P(N);
        for(int i=0; i<N; i++) cin>>P[i];

        multimap<int, char, std::greater<int> > s;

        for(int i=0; i<N; i++){

            s.insert(make_pair(P[i], i+'A'));
        }

        string plan = "";

        while(s.size() > 0){

            auto it = s.begin();

            if(it->first <= 0) break;

            plan+=it->second;


            auto it2 = next(it, 1);
            if(it2 != s.end()){

                if(it2->first == it->first && s.size()%2 == 0){

                    plan += it2->second;

                    auto p = make_pair(it2->first-1, it2->second);
                    s.erase(it2);
                    if(p.first > 0)
                     s.insert(p);
                }


            }

            plan += " ";

            auto p = make_pair(it->first-1, it->second);
            s.erase(it);
            if(p.first > 0)
             s.insert(p);


        }


        cout<<"Case #"<<c<<": "<<plan<<endl;
    }

}

int main(int argc, char *argv[])
{
    test_small();
    //test_large();
    return 0;
}
