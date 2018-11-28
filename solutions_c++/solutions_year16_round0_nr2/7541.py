/****************
*PID:
*Auth:Jonariguez
*****************
*/
#define lson k*2,l,m
#define rson k*2+1,m+1,r
#define rep(i,s,e) for(i=(s);i<=(e);i++)
#define For(j,s,e) For(j=(s);j<(e);j++)
#define sc(x) scanf("%d",&x)
#define In(x) scanf("%I64d",&x)
#define pf(x) printf("%d",x)
#define pfn(x) printf("%d\n",(x))
#define Pf(x) printf("%I64d",(x))
#define Pfn(x) printf("%I64d\n",(x))
#define Pc printf(" ")
#define PY puts("YES")
#define PN puts("NO")
#include <stdio.h>
#include <string.h>
#include <string>
#include <math.h>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
typedef long long LL;
typedef int Ll;
Ll quick_pow(Ll a,Ll b,Ll MOD){a%=MOD;Ll res=1;while(b){if(b&1)res=(res*a)%MOD;b/=2;a=(a*a)%MOD;}return res;}

const int maxn=100000+10;
int a[maxn],b[maxn];
char str[maxn];

void flip(int x,int y){
    int now=x,i;
    for(i=y;i>=x;i--)
        b[now++]=a[i];
    for(i=x;i<=y;i++)
        a[i]=(b[i]^1);
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int i,j,kcase=1,T;
    scanf("%d",&T);
    while(T--){
        int n;
        scanf("%s",str+1);
        printf("Case #%d: ",kcase++);
        n=strlen(str+1);
        for(i=1;i<=n;i++){
            if(str[i]=='+')
                a[i]=0;
            else a[i]=1;
        }
        int i=n,res=0;
        while(i>0){
            while(i>=1 && a[i]==0) i--;
            if(i==0) break;
            j=1;
            while(j<=i && a[j]==0) j++;
            if(j>1){
                flip(1,j-1);res++;
            }
            flip(1,i);
            res++;
        }
        printf("%d\n",res);
    }
    return 0;
}





