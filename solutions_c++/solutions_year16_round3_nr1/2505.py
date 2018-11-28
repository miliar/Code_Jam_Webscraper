#include<bits/stdc++.h>
using namespace std;

int main()
{
long long int p,m,x,n,y,z,t,k;
string s;

cin>>t;
for(int i=1;i<=t;i++)
{
int b[10000]={0};
cin>>n;
p=m=0;

int a[n];
for(int j=0;j<n;j++)
{
cin>>a[j];
p+=a[j];
}

k=0;

int f =0;
while(p>0)
{
y=-1;
m=-1;
f=0;
for(int j=0;j<n;j++)
{

if(a[j]==y && a[j]!=0 )
{
z=j;
m=y;

}

if(a[j]>y)
{
  x=j;
  y=a[j];
  
}

}

for(int j=0;j<n;j++)
{
if(y==a[j])
f++;
}

if(f==2)
{
  a[z]--;
  a[x]--;	  
	b[k++]=z;
  b[k++]=x;
  b[k++]=-1;
  p-=2;	
}
else
{
  a[x]--;
  b[k++]=x;
  b[k++]=-1;
  p--;		
}

}

cout<<"Case #"<<i<<": ";
for(int l=0;l<k-1;l++)
{
if(b[l]==-1)
cout<<" ";
else
cout<<char('A'+ b[l]);
}
cout<<endl;
}

return 0;
}

