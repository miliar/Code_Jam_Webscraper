#include<bits/stdc++.h>
using namespace std;
#define lld long long int
#define max 1000000000
int check(lld temp,lld a[])
{
	lld count=0,i;
	while(temp>0)
	{
		a[temp%10]=1;
		temp=temp/10;
	}
	for(i=0;i<10;i++)
	count+=a[i];
	if(count==10)	return 1;
	else return 0;
}
int main()
{
 lld t,n,x=1;
 cin>>t;
 while(t--)
 {
 cin>>n;
 lld a[10]={},temp,i;
 if(n==0) cout<<"Case #"<<x<<": INSOMNIA"<<endl;
 else
 {
 	 for(i=1;i<max;i++)
 {
 	temp=n*i;
 	if(check(temp,a))	break;
 }
 if(i!=max)cout<<"Case #"<<x<<": "<<temp<<endl;
 else cout<<"Case #"<<x<<": INSOMNIA"<<endl;
 }
 x++;
 }	
	return 0;
}
