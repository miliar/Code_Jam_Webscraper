#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>

#define sz(X) ((int)X.size())
#define FOR(i,x,y) for(int i=x; i<y; ++i)
#define FORE(i,x,y) for(int i=x; i<=y; ++i)
#define FORD(i,x,y) for(int i=x; i>y; --i)
#define FORDE(i,x,y) for(int i=x; i>=y; --i)
#define ALL(x) x.begin(), x.end()

#define INT_MAXIMUM 100000007
#define isPowerOfTwo(S) (!(S & (S - 1)))


using namespace std;

int main()
{
    ofstream cout ("output.txt");
    ifstream cin ("input.txt");

    int T;
    cin>>T;

    FOR(t,1,T+1)
    {
        long long ans = 0;
        char ch;
        long long P,Q; cin>>P>>ch>>Q;

        long long G = __gcd(P,Q);

        P = P/G; Q=Q/G;

        if(P >= Q) ans = 0;
        else if(!isPowerOfTwo(Q))
        {
            cout<<"Case #"<<t<<": "<<"impossible"<<endl;
            continue;
        }
        else
        {
            ans = 1;
            FOR(k, 1, 40)
            {
                if((1<<k) * P >= Q) { ans = k; break; }
            }
        }
        cout<<"Case #"<<t<<": "<<ans<<endl;
    }
    
    return 0;
}