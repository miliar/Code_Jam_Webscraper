#include<iostream>
#include<map>
#include<cstring>
#include<cstdio>
#include<string>

using namespace std;

int c[5][5];
bool fg[20];

int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("data.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int cs=1;cs<=t;cs++){
        int fir,sec;
        scanf("%d",&fir);
        memset(fg,0,sizeof(fg));
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
                scanf("%d",&c[i][j]);
        for(int i=1;i<=4;i++)
            fg[c[fir][i]]=1;
        scanf("%d",&sec);
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
                scanf("%d",&c[i][j]);
        int ans,ok=0;
        for(int i=1;i<=4;i++){
            if(fg[c[sec][i]]==1 && ok==0)
            {
                ok=1;
                ans=c[sec][i];
            }
            else if(fg[c[sec][i]]==1 && ok==1){
                ok=2;
            }
        }
        if(ok==0)printf("Case #%d: Volunteer cheated!\n",cs);
        if(ok==1)printf("Case #%d: %d\n",cs,ans);
        if(ok==2)printf("Case #%d: Bad magician!\n",cs);
    }
    return 0;
}
