#include<iostream>

using namespace std;
int e,r,n;

int check(int v[],int i,int c)
{
//cout<<i<<" "<<c<<endl;
if(i==n)
return 0;
else 
{
int max=0;
for(int k=0;k<=c;k++)
{
int now=v[i]*k+check(v,i+1,c-k+r>e?e:c-k+r);
if(now>max)
max=now;
}
//cout<<"returning:"<<max<<endl;
return max;
}
}


int main()
{
int T=1;
cin>>T;

for(int k=1;k<=T;k++)
{
cin>>e>>r>>n;
int v[n];

int sum=0;
int max=0;
for(int i=0;i<n;i++)
{
cin>>v[i];
sum+=v[i];
if(v[i]>max)
max=v[i];
}

cout<<"Case #"<<k<<": ";
if(e>r)
cout<<check(v,0,e)<<endl;
else
cout<<sum*e<<endl;
}
}