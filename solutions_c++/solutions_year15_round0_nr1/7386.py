#include<bits/stdc++.h>
using namespace std;

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	int t;
	cin>>t;
	for(int te=1;te<=t;te++)
	 {
	 	int n;
	 	string s;
	 	cin>>n;
	 	cin>>s;
		vector<int> a(n+1);
	 	for(int i=0;i<s.size();i++)
	 	   a[i]=s[i]-'0';
	 	int c=0;
	 	int standing=0;
	 	for(int i=0;i<=n;i++)
	 	 {
	 	 	if(standing<i)
	 	 	 {
	 	 	 	c+=i-standing;
	 	 	 	standing=i;
	 	 	 }
	 	 	standing+=a[i];
	 	 }
	 	cout<<"Case #"<<te<<": "<<c<<endl;
	 	
	 	
	 }
}
