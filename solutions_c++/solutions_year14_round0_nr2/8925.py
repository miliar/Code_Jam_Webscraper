/*
**  Coder : Amit Tiwari
** Handle : pipipzz
*/
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define pb push_back
#define all(v) v.begin(),v.end()
#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define rep2(i,m,n) for(int i=m;i<(int)(n);i++)
#define For(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define INF (int)1e9
#define eps 1.0e-11
const double pi = acos(-1.0);

typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vector<int> > vii;
typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;

int main()
{
    int t;
    cin >> t;
    for(int z=1; z<=t; z++)
    {
        double c, f, x;
        cin >> c >> f >> x;
        double tm = 0.0, curr = 0.0, temp, rate = 2.0;
        if(c >= x)
        {
            tm = x/2.0;
            printf("Case #%d: %.7f\n", z, tm);
            continue;
        }
        else
        {
            while(curr < x)
            {
                tm += c/rate;
                if((x-c)/rate > x/(rate+f))
                {
                    rate += f;
                    curr = 0.0;
                }
                else
                {
                    tm += (x-c)/rate;
                    curr = x;
                }
            }
        }
        printf("Case #%d: %.7f\n", z, tm);
    }
    return 0;
}
