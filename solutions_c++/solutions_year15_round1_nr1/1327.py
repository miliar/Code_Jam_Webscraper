#include <iostream>
#include <queue>
#include <cmath>
#include <iterator>
#include <algorithm>
#include <fstream>
#include <set>
#include <sstream>
#include <ctime>
#include <map>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    ifstream in("input.txt");
    ofstream out("output.txt");
    #define cin in
    #define cout out
    int nb_cas;
    cin>>nb_cas;
    for(int cas=1;cas<=nb_cas;cas++)
    {
        cout<<"Case #"<<cas<<": ";
        int N;
        cin>>N;
        vector<long long int> v(N);
        long long int res;
        cin>>res;
        v[0]=res;
        long long int act = res;
        long long int maxiEcart = 0;
        for(int c=1;c<N;c++)
        {
            long long int z;
            cin>>z;
            v[c]=z;
            if(z > act)
            {
                res+=z-act;
            }
            else
            {
                maxiEcart = max(maxiEcart,act-z);
            }
            act=z;
        }
        res-=act;
        cout<<res<<" ";
        res = 0;
        act = 0;
        for(int c=0;c<N;c++)
        {
            res += min(act,maxiEcart);
            act = v[c];
        }
        cout<<res<<endl;
    }
}
