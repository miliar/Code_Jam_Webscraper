#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<ctime>
#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<deque>
#include<list>
#include<set>
#include<map>
#include<stack>
#include<queue>
#include<numeric>
#include<iomanip>
#include<bitset>
#include<sstream>
#include<fstream>
#define debug puts("-----")
#define pi (acos(-1.0))
#define eps (1e-8)
#define inf (1<<30)
using namespace std;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t;
    cin>>t;
    int cas=0;
    while(t--)
    {
        double c,f,x;
        cin>>c>>f>>x;
        double ans=0;
        double s=2;
        while(1)
        {
            if (x/s>c/s+x/(s+f))
            {
                ans+=c/s;
                s+=f;
            }
            else
                break;
        }
        ans+=x/s;
        printf("Case #%d: %.10lf\n",++cas,ans);
    }
    return 0;
}
