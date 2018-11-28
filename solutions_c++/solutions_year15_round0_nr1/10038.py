#include<iostream>
#include<conio.h>
#include<math.h>
using namespace std;
int main()
{
	freopen("in.txt","r",stdin);
    freopen("out","w",stdout);
int smax,k,i,a[1010],sum,minFriends;
int temp,t1,s,p,tc;
cin>>tc;
for(int qq=1;qq<=tc;qq++)
{
	cout<<"Case #"<<qq<<": ";
minFriends=0;
cin>>smax;
cin>>k;
s=smax;
temp=k;
for(i=0;i<=smax;i++)
{
p=pow(10,s);
a[i]=temp/p;
temp=temp%p;
s--;
}
	sum=a[0];
for(i=0;i<smax;i++)
{
if((i+1-sum)<=0)
sum=sum+a[i+1];
else
{
sum=sum+a[i+1]+(i+1-sum);
minFriends++;}
}
if(qq<100)
cout<<minFriends<<endl;
else
cout<<minFriends;
}
return 0;
}
