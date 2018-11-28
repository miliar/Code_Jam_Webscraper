#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int a[5][5];
int t,m,n;
bool p[20];
int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("A-small-attempt1.out","w",stdout);
    int ca=1;
    scanf("%d",&t);
    while(t--)
    {
        memset(p,0,sizeof(p));
        scanf("%d",&n);
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                scanf("%d",&a[i][j]);
            }
            if(i==n)
            {
                for(int j=1;j<=4;j++)
                {
                    p[a[i][j]]=1;
                }
            }
        }
        scanf("%d",&m);
        int cnt=0;
        int ans=0;
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                scanf("%d",&a[i][j]);
            }
            if(i==m)
            {
                for(int j=1;j<=4;j++)
                {
                    if(p[a[i][j]]==1)
                    {
                        cnt++;
                        ans=a[i][j];
                    }
                }
            }
        }
        cout<<"Case #"<<ca++<<": ";
        if(cnt==1)
        {
            cout<<ans<<endl;
        }
        else if(cnt==0)cout<<"Volunteer cheated!"<<endl;
        else cout<<"Bad magician!"<<endl;
    }
    return 0;
}
