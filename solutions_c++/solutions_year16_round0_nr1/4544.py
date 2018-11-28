#include <iostream>
using namespace std;
#define ll long long
bool arr[10];
ll ans[1000009];
bool check()
{
	for(int i=0;i<10;i++)
	{if(arr[i]==false)
	{//cout<<i<<" i"<<endl;
	return false;}}
	return true;
}
void make(ll n)
{
	while(n>0)
	{  //cout<<n%10;
		arr[n%10]=true;
		n/=10;
	}
	//cout<<endl;
	return ;
}
int main() {
int t;
cin>>t;
ll ui;
for(int j=1;j<=t;j++)
{for(int i=0;i<10;i++)
	arr[i]=false;
	cin>>ui;
	ll n=ui;
	while((!check())&&ui>0)
	{
		make(n);
			n+=ui;
	}
	ll ans=n-ui;
	if(ui==0)
	cout<<"Case #"<<j<<":"<<" INSOMNIA"<<endl;
	else cout<<"Case #"<<j<<": "<<ans<<endl;
}
	
	
}
