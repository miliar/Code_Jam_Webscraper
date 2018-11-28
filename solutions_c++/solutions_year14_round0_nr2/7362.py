#include<algorithm>
#include<iostream>
#include<iomanip>
#include<cstring>
#include<cstdlib>
#include<complex>
#include<cstdio>
#include<vector>
#include<stack>
#include<queue>
#include<cmath>
#include<deque>
#include<map>
#include<set>
#define oo 1000000000
#define ooll 1ll<<50
#define base 1000000007ll
using namespace std;
typedef long long ll;
typedef pair<int,int> ii;
typedef pair<int,ii> iii;
typedef vector<int> vi;
typedef vector<ii> vii;
                            /*                           END OF TEMPLATE                            */
//IOI 2014
double C,F,X;
void execute()
{
    scanf("%lf %lf %lf",&C,&F,&X);
    double rate=2,ans=X/2,cur=0;
    for(int i=1; ; i++)
    {
        cur+=C/rate;
        rate+=F;
        if(X/rate+cur<ans) ans=X/rate+cur;
        else
        {
            printf("%.7lf\n",ans);
            return;
        }
    }
}
int main()
{
    freopen("B.inp","r",stdin);
    freopen("B.out","w",stdout);
    int test;
    scanf("%d",&test);
    for(int tc=1; tc<=test; tc++)
    {
        printf("Case #%d: ",tc);
        execute();
    }
    return 0;
}
