#include<stdio.h>
#include<iostream>
#include<sstream>
#include<math.h>
using namespace std;
int main()
{
   // freopen("C:\\Users\\swarn\\Desktop\\input.txt","r",stdin);
   // freopen("C:\\Users\\swarn\\Desktop\\output.txt","w",stdout);
    long long t,u,i,j,flag[17],a[4][4],b[4][4],n1,n2,ans;
    cin>>t;
    for(u=1;u<=t;u++)
    {

    cin>>n1;
    for(i=0;i<17;i++)
    {
        flag[i]=0;
    }
    for(i=0;i<4;i++)
    {
        for(j=0;j<4;j++)
        {
            cin>>a[i][j];
            if(i==n1-1)
                flag[a[i][j]]++;
        }
    }
    cin>>n2;
    for(i=0;i<4;i++)
    {
        for(j=0;j<4;j++)
        {
            cin>>b[i][j];
            if(i==n2-1)
                flag[b[i][j]]++;
        }
    }
    long long mark=0;
    for(i=1;i<17;i++)
    {
        if(flag[i]==2)
            {mark++;ans=i;}
    }
    cout<<"Case #"<<u<<":"<<" ";
    if(mark==1)
       cout<<ans<<"\n";
    else if(mark==0)
        cout<<"Volunteer cheated!\n";
    else if(mark>1)
        cout<<"Bad magician!\n";
    }
    return 0;
}


