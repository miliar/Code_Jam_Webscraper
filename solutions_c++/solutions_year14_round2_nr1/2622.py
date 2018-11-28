#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
const int N = 110;

char s[N];
int a[N][N][2],n,ll[N];

int main()
{
    freopen("A-small-attempt0.in","rb",stdin);
    freopen("test.out","wb",stdout);
    int T;scanf("%d",&T);
    for(int cas=1;cas<=T;++cas){
        printf("Case #%d: ",cas);
        scanf("%d",&n);
        for(int i=0;i<n;++i){
            scanf("%s",s);
            memset(a[i],0,sizeof a[i]);
            int tot=0;a[i][tot][0]=s[0],a[i][tot][1]=1;
            for(int j=1;s[j];++j){
                if(s[j]!=s[j-1]) ++tot,a[i][tot][0]=s[j];
                ++a[i][tot][1];
            }
            ll[i]=tot;
        }
        bool ok=true;
        for(int i=1;i<n;++i)
            if(ll[i]!=ll[i-1]) ok=false;
        for(int i=1;i<n;++i)
            for(int j=0;j<=ll[i];++j)
                if(a[i][j][0]!=a[0][j][0]) ok=false;
        int ans=0,res;
        for(int i=0;i<=ll[0];++i){
            res=0;
            for(int j=0;j<n;++j) res+=a[j][i][1];
            res/=n;
            for(int j=0;j<n;++j)
                ans+=abs(a[j][i][1]-res);
        }
        if(!ok) printf("Fegla Won\n");
        else printf("%d\n",ans);
    }
    return 0;
}
