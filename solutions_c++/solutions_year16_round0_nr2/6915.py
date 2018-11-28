#include<cstdio>
#include<cstring>
#include<iostream>
#include<sstream>
#include<algorithm>
#include<vector>
#include<bitset>
#include<set>
#include<queue>
#include<stack>
#include<map>
#include<cstdlib>
#include<cmath>
#define PI 2*asin(1.0)
#define LL long long
#define pb push_back
#define pa pair<int,int>
#define clr(a,b) memset(a,b,sizeof(a))
#define lson lr<<1,l,mid
#define rson lr<<1|1,mid+1,r
#define bug(x) printf("%d++++++++++++++++++++%d\n",x,x)
#define key_value ch[ch[root][1]][0]
const int  MOD = 1000000007;
const int N = 100+15;
const int maxn = 450;
const int letter = 130;
const int INF = 1e17;
const double pi=acos(-1.0);
const double eps=1e-8;
using namespace std;
inline int read()
{
    int x=0,f=1;char ch=getchar();
    while(ch<'0'||ch>'9'){if(ch=='-')f=-1;ch=getchar();}
    while(ch>='0'&&ch<='9'){x=x*10+ch-'0';ch=getchar();}
    return x*f;
}
char s[N];
int n,a[N];
int main(){
    int T,cas=0;
    freopen("B-large.in","r",stdin);
    freopen("B-out.out","w",stdout);
    scanf("%d",&T);
    while(T--){
        clr(a,0);
        scanf("%s",s);
        n=strlen(s);
        for(int i=0;i<n;i++) if(s[i]=='+') a[i]=1;
        int sum=0;
        for(int i=n-1;i>=0;i--){
            if(!a[i]){
                for(int j=0;j<=i;j++) a[j]=!a[j];
                sum++;
            }
            int flag=0;
            for(int j=0;j<n;j++) if(!a[j]){flag=1;break;}
            if(!flag) break;
        }
        printf("Case #%d: %d\n",++cas,sum);
    }
    return 0;
}
