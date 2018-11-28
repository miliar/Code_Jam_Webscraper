#include<iostream>
#include<cstdlib>
#include<string.h>
using namespace std;
int P,Q;
bool check()
{
	int key=2;
	while(key<Q)
	{
		key=key*2;
	}
	if(key==Q)
	return true;
	else 
	return false;
}
int val()
{
	int key=1;
	while(key<P)
	{
		key=key*2;
	}
	if(key!=1)
	key=key/2;
	return key;
}
int main()
{
	int T;
	cin>>T;
	for(int p=0;p<T;p++)
	{
		a:
			if(p>=T)
			exit(0);
		char t;
		cin>>P;
		cin>>t;
		cin>>Q;
		cout<<"Case #"<<p+1<<": ";
		if(!check())
		{
			cout<<"impossible"<<endl;
			p++;
			goto a;
		}
		int k=val();
		int sol=Q/k,cnt=0;
	while(sol!=1)
	{
		sol=sol/2;
		cnt++;
	}
	cout<<cnt;
	cout<<endl;
}
	}
	
