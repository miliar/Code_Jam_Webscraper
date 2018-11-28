#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>
using namespace std;
#define LL unsigned long long

const int N=111,INF=0x3f3f3f3f;

int G[4][4],a[5],b[5];

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("yy.out","w",stdout);
    int T;cin>>T;
    for(int cs=1;cs<=T;++cs)
    {
        int t;
        cin>>t;--t;
        for(int i=0;i<4;++i)
        {
            for(int j=0;j<4;++j)
            {
                cin>>G[i][j];
            }
        }
        for(int j=0;j<4;++j) a[j]=G[t][j];
        cin>>t;--t;
        for(int i=0;i<4;++i)
        {
            for(int j=0;j<4;++j)
            {
                cin>>G[i][j];
            }
        }
        for(int j=0;j<4;++j) b[j]=G[t][j];
        int sum=0,ans;
        for(int i=0;i<4;++i)
            for(int j=0;j<4;++j)
                if(a[i]==b[j]) ++sum,ans=a[i];
        printf("Case #%d: ",cs);
        if(sum==0) printf("Volunteer cheated!\n");
        else if(sum==1) printf("%d\n",ans);
        else printf("Bad magician!\n");
    }
    return 0;
}
