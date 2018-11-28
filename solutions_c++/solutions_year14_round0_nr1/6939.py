#include<fstream>
#include<iostream>
#include<cstdlib>
using namespace std;
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int ctr=1,T,x,y,ans,cnt;
    int a[4][4],b[4][4];
    cin>>T;
    while(ctr<=T)
    {
        cnt=0;
        cin>>x;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                cin>>a[i][j];
        cin>>y;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                cin>>b[i][j];
        ans=0;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                if(a[x-1][i]==b[y-1][j])
                {
                    cnt++;
                    if(cnt==1)
                        ans=a[x-1][i];
                }
            }
        }
        cout<<"Case #"<<ctr<<": ";
        switch(cnt)
        {
            case 0:
                cout<<"Volunteer cheated!"<<endl;break;
            case 1:
                cout<<ans<<endl;break;
            default:
                cout<<"Bad magician!"<<endl;break;
        }
        ctr++;
    }
}
