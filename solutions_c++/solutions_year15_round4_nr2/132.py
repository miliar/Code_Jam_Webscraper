/**
 * @author neko01
 */
//#pragma comment(linker, "/STACK:102400000,102400000")
#include <cstdio>
#include <cstring>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
#include <cmath>
#include <set>
#include <map>
using namespace std;
typedef long long LL;
#define min3(a,b,c) min(a,min(b,c))
#define max3(a,b,c) max(a,max(b,c))
#define pb push_back
#define mp(a,b) make_pair(a,b)
#define clr(a) memset(a,0,sizeof a)
#define clr1(a) memset(a,-1,sizeof a)
#define dbg(a) printf("%d\n",a)
typedef pair<int,int> pp;
const double eps=1e-9;
const double pi=acos(-1.0);
const int INF=0x3f3f3f3f;
const LL inf=(((LL)1)<<61)+5;
struct node{
    double v,r;
}a[105];
int n;
double x,c;
bool cmp(node u,node v)
{
    return u.r<v.r;
}
bool gao(double mid)
{
    int i=0,j=n-1;
    double sum=0;
    while(i<j){
        if(a[i].r>c||a[j].r<c) break;
        if()
    }
}
int main()
{
    //freopen("A-small-attempt0 (2).in" , "r" , stdin);
    //freopen("A-small-attempt0 (2).out" , "w" , stdout);
    int t,cnt=0;
    scanf("%d",&t);
    while(t--){
        scanf("%d%lf%lf",&n,&x,&c);
        for(int i=0;i<n;i++)
            scanf("%lf%lf",&a[i].v,&a[i].r);
        int sum1=0,sum2=0;
        for(int i=0;i<n;i++){
            if(a[i].r>c) sum1++;
            if(a[i].r<c) sum2++;
        }
        sort(a,a+n,cmp);
        if(sum1==n||sum2==n){
            printf("Case #%d: IMPOSSIBLE\n",++cnt);
            continue;
        }
        double l=0,r=1e10;
        for(int i=0;i<1000;i++){
            double mid=(l+r)/2;
            if(gao(mid)) r=mid;
            else l=mid;
        }
        printf("Case #%d: %d\n",++cnt,ans);
    }
    return 0;
}
