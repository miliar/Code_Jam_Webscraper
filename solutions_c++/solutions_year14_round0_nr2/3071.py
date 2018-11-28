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
#include <complex>
#include <utility>
#include <fstream>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cctype>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <climits>

using namespace std;

#define REP(i,a,b) for(int i=a;i<b;i++)
#define REV(i,a,b) for(int i=a-1;i>=b;i--)
#define GI ({ int x; scanf("%d",&x); x; })
#define ALL(v) v.begin(),v.end()
#define PB push_back
#define MP make_pair
#define PQ priority_queue
#define MAXX (int)(1e9)
#define MINN (double)(1e-9)
#define PI (double)(3.141592653589793238)

typedef long long LL;
typedef unsigned long long ULL;
typedef vector <int> VI;
typedef vector <string> VS;
typedef vector <vector <int> > VVI;
typedef pair <int,int> PII;

double C,F,X;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output2.txt","w",stdout);
    int T,cs=1;
    cin >> T;
    while(T--)
    {
        cin >> C >> F >> X;
        double te1=0.0,te2=0.0,te3=0.0;
        double t = 2.0;
        double ans = 0.0;
        bool finish = false;
        while(!finish)
        {
            te1 = X/t;
            te2 = C/t;
            te3 = X/(t+F);
            if( te2+te3 < te1 )
            {
                t+=F;
                ans += te2;
            }
            else
            {
                ans+= te1;
                finish = true;
            }
        }
       cout<<fixed;
       cout<<"Case #"<< cs++ << ": " << setprecision(7) << ans << endl;
    }
  return 0;
}
