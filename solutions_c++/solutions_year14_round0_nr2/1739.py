#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <bitset>
#include <sstream>
#include <string>

#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>

#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

#define FILL(arr,n) memset(arr,n,sizeof(arr))
#define FORUP(i,m,n) for(int i=(m); i<(n); i++)
#define FORDOWN(i,m,n) for(int i=(m)-1; i>=(n); i--)

#define PB push_back
#define MP make_pair
#define F first
#define S second

#define INF 2000000000
#define EPS 1e-11
#define PI acos(-1.0)
#define MAX_N 1000005
#define MOD 1000000007
using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<pii> vii;

int
main()
{
    int T;
    double C,F,X;
    scanf("%d", &T);
    for(int tc = 1;tc <= T;tc++)
    {
        scanf("%lf %lf %lf",&C,&F,&X);
        double ans;
        ans = X/2.0;
        double cookiesNow = 0.0;
        double rateNow = 2.0;
        double timeNow = 0.0;
        while(true)
        {
            double waitTime = C / rateNow;
            if(ans > timeNow + (X / (rateNow+F)))
            {
                ans = min(ans, timeNow + (X / rateNow));
                cookiesNow += (waitTime * rateNow);
                rateNow += F;
                timeNow += waitTime;
            }
            else
            {
                ans = min(ans, timeNow + (X / rateNow));
                break;
            }
        }
        printf("Case #%d: ",tc);
        printf("%.6f\n",ans);
    }
}
