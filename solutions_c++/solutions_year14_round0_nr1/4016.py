#include <iostream>
#include<stdio.h>
using namespace std;
int T,t,k,n,i,j,sol,ans,sto1[5],sto2[5],a[5][5];
int main()
{
    freopen("inp1.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>T;
    t=T;
    while(T--)
    {
        k=0;
        cin>>n;
        for(i=1;i<=4;i++)
        for(j=1;j<=4;j++)
        {
        cin>>a[i][j];
        if(i==n)
        {
        sto1[k]=a[i][j];
        k++;
        }
        }
        k=0;
        cin>>n;
        for(i=1;i<=4;i++)
        for(j=1;j<=4;j++)
        {
        cin>>a[i][j];
        if(i==n)
        {
        sto2[k]=a[i][j];
        k++;
        }
        }
        sol=0;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
        {
            if(sto1[i]==sto2[j])
            {sol++;
            ans=sto1[i];
            }
        }
        cout<<"Case #"<<t-T<<": ";
        if(sol==1)
        cout<<ans;
        else if(sol==0)
        cout<<"Volunteer cheated!";
        else
        cout<<"Bad magician!";
        cout<<endl;
    }
    return 0;
}
