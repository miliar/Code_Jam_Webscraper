#include<iostream>
using namespace std;

int canSleep(int a[])
{
for(int i=0;i<10;i++)
if(a[i]==0)
return 0;
return 1;
}

int main()
{
int t,n;
int count=1;
cin>>t;
while(t--)
{

int flag[10]={0};
cin>>n;
if(n==0)
{
cout<<"Case #"<<count++<<": INSOMNIA"<<endl;
continue;
}
int temp1=0;
while(!canSleep(flag))
{
temp1+=n;
int temp=temp1;
while(temp>0)
{
flag[temp%10]=1;
temp/=10;
}
}
cout<<"Case #"<<count++<<": "<<temp1<<endl;
}
return 0;
}


