#include<iostream>
using namespace std;
int main()
{
int t,u=1;
cin>>t;
while(u<=t)
{
    int n,m,a[4][4],j,b[4][4],i;
    cin>>n;
    for(i=0;i<4;i++)
        for(j=0;j<4;j++)
            cin>>a[i][j];
    cin>>m;
    for(i=0;i<4;i++)
        for(j=0;j<4;j++)
            cin>>b[i][j];
    int ans=0,no;
    for(i=0;i<4;i++)
      for(j=0;j<4;j++)
        if(a[n-1][i]==b[m-1][j])
            {
             ans++;
             no=a[n-1][i];
             break;
            }

    if(ans==1)
        cout<<"Case #"<<u<<": "<<no<<endl;
    else if(ans>1)
        cout<<"Case #"<<u<<": "<<"Bad magician!"<<endl;
    else
        cout<<"Case #"<<u<<": "<<"Volunteer cheated!"<<endl;
u++;
}
}
