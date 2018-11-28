#include<bits/stdc++.h>
using namespace std;
#define ll long long
int freq[10];
bool done()
{
	for(int i=0;i<10;i++)
		if(freq[i]==0)
			return false;
	return true;
}
int main()
{
	int t;
	cin>>t;
	for(int x=1;x<=t;x++)
	{
		ll n;
		cin>>n;
		ll mult=1;
		ll newn=n;
		if(n==0)
		{
			cout<<"Case #"<<x<<": INSOMNIA"<<endl;
			continue;
		}
		memset(freq,0,sizeof(freq));
		while(!done())
		{
			newn=n*mult;
			mult+=1;
			string s=std::to_string(newn);
			for(int i=0;i<s.length();i++)
				freq[s[i]-'0']+=1;
		}
		cout<<"Case #"<<x<<": "<<newn<<endl;
	}
	return 0;
}