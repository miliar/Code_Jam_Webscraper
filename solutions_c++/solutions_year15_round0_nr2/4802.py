#include<cstdio>
#include<cstring>
#include<algorithm>
#define mem(name,value) memset(name,value,sizeof(name))
#define FOR(i,n) for(int i=1;i<=n;i++)
using namespace std;

const int maxn = 1000+10;
int a[maxn];

int main(){
   // freopen("B-small-attempt1.in","r",stdin);
   // freopen("out.txt","w",stdout);
    int kase=0, T,n,m;
    scanf("%d",&T);
    while(T--){
        int maxv = 0;
        scanf("%d",&n);
        for(int i=0;i<n;i++){
            scanf("%d",&a[i]);
            maxv = max(maxv,a[i]);
        }
        int ans = maxv;
        for(int i=maxv;i>=1;i--){
            int p = 0;
            for(int j=0;j<n;j++) if(a[j]>i) p += ((a[j]-i-1)/i+1);
            ans = min(ans,i+p);
        }
        printf("Case #%d: %d\n",++kase,ans);
    }
    return 0;

}
