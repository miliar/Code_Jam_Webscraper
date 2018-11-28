#include<bits/stdc++.h>
using namespace std;
typedef long long LL;
typedef pair<int,int> PII;
#define MP make_pair
#define PB push_back
#define AA first
#define BB second
#define OP begin()
#define ED end()
#define SZ size()
#define cmin(x,y) x=min(x,y)
#define cmax(x,y) x=max(x,y)
#define NAME "B-large"
#define UsingFile 1

int main(){
    if(UsingFile)freopen(NAME".in","r",stdin);
    if(UsingFile)freopen(NAME".out","w",stdout);
    int i,j,k,_T;
    scanf("%d",&_T);
    for(int CA=1;CA<=_T;CA++){
        int n;
        scanf("%d",&n);
        vector<int>L;
        for(i=1;i<=n;i++){
            scanf("%d",&j);
            L.PB(j);
        }
        int q=*max_element(L.OP,L.ED);
        int ans=q;
        for(i=1;i<=q;i++){
            int now=i;
            for(j=0;j<L.SZ;j++)if(L[j]>i){
                now+=(L[j]-1)/i;
            }
            cmin(ans,now);
        }
        printf("Case #%d: %d\n",CA,ans);
    }
    return 0;
}

