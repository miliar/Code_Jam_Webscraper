#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int main()
{
    //freopen("A-small-attempt0.in","r",stdin);
    //freopen("out.in","w",stdout);
    int a[5][5],b[5][5];
    int x,y,flag=0,t;
    cin>>t;
    for(int d=1; d<=t; d++)
    {
        memset(a,0,sizeof(a));
        cin>>x;
        for(int i=1; i<=4; i++)
        {
            for(int j=1; j<=4; j++)
                cin>>a[i][j];
        }
        cin>>y;
        for(int i=1; i<=4; i++)
        {
            for(int j=1; j<=4; j++)
                cin>>b[i][j];
        }
        int z;
        for(int i=1; i<=4; i++)
        {
            for(int j=1; j<=4; j++)
            {
                if(a[x][i]==b[y][j])
                {
                    z=a[x][i];
                    flag++;
                }
            }
        }
        if(flag==0)
        {
            cout<<"Case #"<<d<<": "<<"Volunteer cheated!\n";
        }
        else if(flag==1)
        {
            cout<<"Case #"<<d<<": "<<z<<"\n";
        }
        else
        {
            cout<<"Case #"<<d<<": "<<"Bad magician!\n";
        }
        flag=0;
    }
    return 0;
}
