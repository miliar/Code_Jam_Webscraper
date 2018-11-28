#include <bits/stdc++.h>
using namespace std;



int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int t;
	cin>>t;
	int n,need;
	cin>>n>>need;
	string s="";

	for(int i=0;i<32;i++)
		s+='0';
	s[0]='1';
	s[31]='1';
	string ans="3 2 3 2 7 2 3 2 3";
	cout<<"Case #1:"<<endl;

	for(int i=2;i<=30;i+=2)
	for(int j=i+2;j<=30;j+=2)
	for(int k=1;k<=29;k+=2)
	for(int l=k+2;l<=29;l+=2)
	{
		if(need==0)
			continue;
		string temp=s;
		s[i]=s[j]=s[k]=s[l]='1';
		cout<<s<<" "<<ans<<endl;
		s=temp;
		need--;
	}	



	return 0;
}