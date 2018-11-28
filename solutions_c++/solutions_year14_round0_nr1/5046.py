#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{
int t,ans[101][2],q[5][5],a[5][5],x,y,c,st,f[17]={0};
cin>>t;
for(int k=0;k<t;k++)
{
    for(int i=0;i<17;i++)
    f[i]=0;
 c=0;st=0;
cin>>x;
for(int i=1;i<5;i++)
{
    for(int j=1;j<5;j++)
    {
        cin>>q[i][j];
    }
}

cin>>y;
for(int i=1;i<5;i++)
{
    for(int j=1;j<5;j++)
    {
        cin>>a[i][j];
    }
}

for(int i=1;i<5;i++)
{
   f[q[x][i]]=1;
}

for(int i=1;i<5;i++)
{
   if(f[a[y][i]])
   {
       st=a[y][i];
       c++;
   }

}
ans[k][0]=c;ans[k][1]=st;
}
for(int k=0;k<t;k++)
{
    if(ans[k][0]==1)
    cout<<"Case #"<<k+1<<": "<<ans[k][1]<<endl;
    else if(ans[k][0]==0)
    cout<<"Case #"<<k+1<<": "<<"Volunteer cheated!"<<endl;
    else
    cout<<"Case #"<<k+1<<": "<<"Bad magician!"<<endl;
}
return 0;
}
