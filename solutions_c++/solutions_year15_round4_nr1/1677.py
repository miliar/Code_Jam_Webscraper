#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<cstring>
struct point
{
    int v;
    int dis;
} a[200][200];
using namespace std;
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int T,ca,R,C,i,j;
    cin>>T;
    for (ca=1;ca<=T;ca++)
        {
            memset(a,0,sizeof a);
            cin>>R>>C;
            char tmp[200];
            for (i=1;i<=R;i++)
            {
                scanf("%s",tmp);
                for (j=0;j<C;j++)
                 {
                    if (tmp[j]=='^') a[i][j+1].v=1;
                    if (tmp[j]=='v') a[i][j+1].v=2;
                    if (tmp[j]=='<') a[i][j+1].v=4;
                    if (tmp[j]=='>') a[i][j+1].v=8;
                    if (tmp[j]=='.') a[i][j+1].v=0;
                 }
            }
            for (i=1;i<=R;i++)
            {
                j=1;
                while (a[i][j].v==0&&j<=C) j++;
                if (j<=C) a[i][j].dis=a[i][j].dis+4;
                j=C;
                while (a[i][j].v==0&&j>=1) j--;
                if (j>=1) a[i][j].dis=a[i][j].dis+8;
            }
            for (j=1;j<=C;j++)
            {
                i=1;
                while (a[i][j].v==0&&i<=R) i++;
                if (j<=C) a[i][j].dis=a[i][j].dis+1;
                i=R;
                while (a[i][j].v==0&&i>=1) i--;
                if (i>=1) a[i][j].dis=a[i][j].dis+2;
            }
         /*    for (i=1;i<=R;i++){
                for (j=1;j<=C;j++)
                cout<<a[i][j].v<<' ';
                cout<<endl;
             }
              for (i=1;i<=R;i++){
                for (j=1;j<=C;j++)
                cout<<a[i][j].dis<<' ';
                cout<<endl;
             }
        */
            int ans;
            ans=0;
            for (i=1;i<=R;i++)
                for (j=1;j<=C;j++)
                {
                    if (a[i][j].v==5) continue;
                    if (a[i][j].dis==15) {ans=-1;break;}
                    int t;
                    t=a[i][j].v&a[i][j].dis;
                    if (t>0) ans++;
                }
            printf("Case #%d: ",ca);
            if (ans<0) cout<<"IMPOSSIBLE"<<endl;
            else cout<<ans<<endl;



        }




    return 0;
}
