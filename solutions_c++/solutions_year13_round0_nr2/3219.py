#include<iostream>
using namespace std;
int main()
{
int T;
cin>>T;
int C=1;
while(T--)
{
int maxrow[100]={0};
int maxcol[100]={0};
int data[100][100]={0};
int N,M;
cin>>N>>M;
for(int i=0;i<N;i++)
{
for(int j=0;j<M;j++)
{
cin>>data[i][j];
}
}
for(int j=0;j<M;j++)
{
int max=0;
for(int i=0;i<N;i++)
if(data[i][j]>max)
max=data[i][j];
maxcol[j]=max;
}
for(int i=0;i<N;i++)
{
int max=0;
for(int j=0;j<M;j++)
if(data[i][j]>max)
max=data[i][j];
maxrow[i]=max;
}
int i;
for(i=0;i<N;i++)
{
int j;
for(j=0;j<M;j++)
{
if(data[i][j]>=maxrow[i]||data[i][j]>=maxcol[j])
continue;
else
break;
}
if(j!=M)
break;
}
if(i!=N)
cout<<"Case #"<<C<<": NO\n";
else
cout<<"Case #"<<C<<": YES\n";

C++;
}

return 0;
}
