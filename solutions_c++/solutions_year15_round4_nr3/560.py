#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <cmath>
using namespace std;
#define eps 1e-6

char buf[233][11111];
int word[233][1010],num[233],cnt,bel[233],belong[4999];
map<string,int> M;

int main()
{
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    int t,n,ans;
    char wd[22];
    scanf("%d",&t);
    for (int cas=1;cas<=t;++cas)
    {
        M.clear();
        scanf("%d",&n);
        gets(buf[0]);
        for (int i=1;i<=n;++i) gets(buf[i]);
        printf("Case #%d: ",cas);
        cnt=0;
        for (int i=1;i<=n;++i)
        {
            num[i]=0;
            for (int j=0;buf[i][j];)
                if (buf[i][j]>='a'&&buf[i][j]<='z')
                {
                    int l=0;
                    for (;buf[i][j]>='a'&&buf[i][j]<='z';++j) wd[l++]=buf[i][j];
                    wd[l]=0;
                    if (M.find(wd)==M.end()) M[wd]=++cnt;
                    word[i][num[i]++]=M[wd];
                }
                else ++j;
        }
        bel[1]=0;
        bel[2]=1;
        ans=999999;
        for (int i=0;i<(1<<(n-2));++i)
        {
            for (int j=0;j<n-2;++j) bel[n-j]=(i&(1<<j))?1:0;
            memset(belong,0,sizeof(belong[0])*(cnt+1));
            int tmp=0;
            for (int j=1;j<=n;++j)
                for (int k=0;k<num[j];++k)
                {
                    int id=word[j][k];
                    if (belong[id]==0) belong[id]=bel[j]+1;
                    else if (belong[id]==3) ;
                    else if (belong[id]!=(bel[j]+1)) belong[id]=3,++tmp;
                }
            ans=min(ans,tmp);
        }
        printf("%d\n",ans);
    }
    return 0;
}
