#include<cstdio>
#include<cstring>
using namespace std;
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("b.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        char a[10][10];
        int k,m;
        for(k=0;k<4;k++) scanf("%s",a[k]);
        int dot=0,ans=0;
        char won;
        for( k=0;k<4;k++)
        {
            char tp=0;
            for( m=0;m<4;m++)
            {
                if(a[k][m]=='T') continue;
                else if(a[k][m]!='.')
                {
                    if(tp!=0){if(a[k][m]==tp) continue; else break;}
                    tp=a[k][m];
                }
                else {dot=1;break;}
            }
            if(m==4) {won=tp;ans=1;break;}
        }
        if(ans==1) {printf("Case #%d: %c won\n",i,won);continue;}


        for(k=0;k<4;k++)
        {
            char tp=0;
            for(m=0;m<4;m++)
            {
                if(a[m][k]=='T') continue;
                else if(a[m][k]!='.')
                {
                    if(tp!=0){if(a[m][k]==tp) continue; else break;}
                    tp=a[m][k];
                }
                else break;
            }
            if(m==4) {won=tp;ans=1;break;}
        }
        if(ans==1) {printf("Case #%d: %c won\n",i,won);continue;}


        char tp=0;
        for( k=0;k<4;k++)
        {
            if(a[k][k]=='T') continue;
            if(a[k][k]!='.')
            {
                if(tp==0) {tp=a[k][k];continue;}
                else if(a[k][k]==tp) continue;
                else break;

            }
            else break;
        }
       if(k==4) {printf("Case #%d: %c won\n",i,tp);continue;}



        tp=0;
        for( k=0,m=3;k<4;k++,m--)
        {
            if(a[k][m]=='T') continue;
            if(a[k][m]!='.')
            {
                if(tp==0) {tp=a[k][m];continue;}
                else if(a[k][m]==tp) continue;
                else break;

            }
            else break;
        }
       if(k==4) {printf("Case #%d: %c won\n",i,tp);continue;}


       if(dot==0) printf("Case #%d: Draw\n",i);
       else printf("Case #%d: Game has not completed\n",i);

    }
    return 0;
}
