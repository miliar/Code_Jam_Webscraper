#include <iostream>

using namespace std;

int main()
{
    int t,x,y,a[5][5],b[5][5],i,j,c,e,k;
    cin>>t;
    for(k=1;k<=t;k++)
    {
        cin>>x;
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
            cin>>a[i][j];
        cin>>y;
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
            cin>>b[i][j];
        c=0;
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
        {
            if(a[x][i]==b[y][j])
                {c++;
                e=a[x][i];}
        }
        cout<<"Case #"<<k<<": ";
        if(c==1)
            cout<<e<<"\n";
        else if(c>1)
            cout<<"Bad magician!\n";
        else if(c==0)
            cout<<"Volunteer cheated!\n";
    }
    return 0;
}
