#include <bits/stdc++.h>
using namespace std;

int main() {
	int t,n;
	cin>>t;
	string s,k;
	for(int l=1;l<=t;l++)
	{
	cin>>s;
	cout<<"Case #"<<l<<": ";
	 k="";
	n=s.size();
	for(int i=0;i<n;i++)
	{
	if(!i) k+=s[i];
	if(i&&s[i]>=k[0])  k=s[i]+k;
	else if(i)  k+=s[i];
	}
	cout<<k<<endl;
	
	}
	return 0;
}