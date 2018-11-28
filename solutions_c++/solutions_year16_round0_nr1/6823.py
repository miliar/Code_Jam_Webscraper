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
const int N = 1e5+1000;
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
LL n;
int vis[15];
int main(){
    int T,cas=0;
    freopen("A-large.in","r",stdin);
    freopen("A-out.out","w",stdout);
    scanf("%d",&T);
    while(T--){
        clr(vis,0);
        cin >> n;
        if(n==0) {
            printf("Case #%d: INSOMNIA\n",++cas);
            continue;
        }
        int sum=0;
        LL x=n,f;
        while(1){
            f=x;
            while(x){
                if(!vis[x%10]) sum++,vis[x%10]=1;
                x=x/10;
            }
            if(sum==10) break;
            x=f+n;
        }
        printf("Case #%d: ",++cas);
        cout<<f<<endl;

    }
    return 0;
}
