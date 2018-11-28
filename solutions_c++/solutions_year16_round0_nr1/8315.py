//#include<iostream>
#include<bits/stdc++.h>
//#include<string>
using namespace std;
int n;
bool a[10] = {0};
bool exist()
{
	for(int i=0;i<10;i++)
	if(a[i]==0) return false;
	
	return true;
}
int kkk(int j)
{
	string s ;
	stringstream ss;
	ss << j;
	s = ss.str();

	for(int i=0;i<s.size();i++)
	{
		
		int c = s[i] -'0';
		//cout<<c<<endl;
		a[c] = 1;
	}
	if(exist())
	return j;
	else
	{
		return kkk(n+j);
	 } 
}

int main()
{
	freopen ("A-large.in","r",stdin);
    freopen("A-large1.out","w",stdout);
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
	
		cin>>n;
		int j = n;
		for(int j=0;j<10;j++)
		a[j] = 0;
		if(n==0)
		{
			cout<<"Case #"<<i+1<<": "<<"INSOMNIA"<<endl;
			continue;
		}
		cout<<"Case #"<<i+1<<": "<<kkk(j)<<endl;
	}
}
