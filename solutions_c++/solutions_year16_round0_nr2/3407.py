#include <bits/stdc++.h>
typedef long long int ll;
#define fio ios_base::sync_with_stdio(false)
using namespace std;

int cal(string s,int l,int r)
{
	if(r<l) return 0;
	if(r==l) return (s[l]=='+'?0:1);
	int ans=0;
	if(s[l]=='+' && s[r]=='-')
	{
		int temp=l;
		while(s[temp]=='+') {s[temp]='-';temp++;}
		for(int i=l;i<=r;i++)
			s[i]=(s[i]=='-'?'+':'-');
		ans+=2;
	}
	else if(s[l]=='-' && s[r]=='-')
	{
		for(int i=l;i<=r;i++)
			s[i]=(s[i]=='-'?'+':'-');
		reverse(s.begin()+l,s.begin()+r+1);
		ans+=1;
	}
	while(s[r]=='+' && r>l) r--;
	return ans+cal(s,l,r);
}

int main() {
	int t;
	cin>>t;
	for(int z=1;z<=t;z++)
	{
		string s;
		cin>>s;
		cout<<"Case #"<<z<<": "<<cal(s,0,s.size()-1)<<"\n";
	}
	return 0;
}