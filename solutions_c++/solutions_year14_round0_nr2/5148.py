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
#include <climits>
#include <string.h>

#define SZ(c) c.size()
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define SORT(a) sort(a.begin(),a.end())
#define tests int test; scanf("%d",&test); while(test--)
#define dbg(n) cout<<#n<<" = "<<n<<endl;

using namespace std;

int strToInt(string str) {int ans; stringstream s; s<<str; s>>ans; return ans;}
string intToStr(int n) {string str; stringstream s; s<<n; s>>str; return str;}
int MAX(int a,int b) {if(a >b) return a; return b;}
int MIN(int a,int b) {if(a <b) return a; return b;}
int ABS(int a) {if(a >0) return a; return -a;}

double buy (int farm, double cost, double extra)
{
    if(farm == 0)
        return 0;

    double ans =0.0;
    double capability = 2.0;
    for(int i=1; i<=farm; i++)
    {
        ans += (cost/capability);
        capability += extra;
    }

    return ans;

}

double solve(int farm, double cost, double extra, double target)
{
     double time = buy(farm, cost, extra);
     double capability = 2 + (farm* extra);
     return (time + (target* 1.0)/ capability);
}

int main()
{
    freopen("B-large.txt", "r", stdin);
    freopen("writeCookieLarge.txt", "w", stdout);
    int test;
    scanf("%d\n",&test);
    double c,f,x;
    for(int running=1; running <= test; running++)
    {
        cin>>c>>f>>x;
        double ans = 110000.00, last = 110000.00;
        for(int farm =0; farm <=111111; farm++)
        {
            double current = solve(farm, c, f, x);
            if( current > last)
                {
                    ans = last;
                    printf("Case #%d: %.7f\n", running, ans);
                    break;
                }
            else
                last = current;
        }

    }
    return 0;
}

