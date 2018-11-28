#include<bits/stdc++.h>
using namespace std;

int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	freopen("C:/Users/HP/Desktop/CodeJam/A2_input.txt","r",stdin);//redirects standard input
	freopen("C:/Users/HP/Desktop/CodeJam/A2_output.txt","w",stdout);//redirects standard output
	int t;
	string s;
	cin>>t;
	for(int tc=1; tc<=t; tc++)
	{
		char ans[3000];
		cin>>s;
		int start=s[0],end=s[0],top=1500,bottom=1500;
		ans[top]=s[0];
		for(int i=1; i<s.length(); i++)
		{
			if(s[i]>=start) {
				top--;
				ans[top]=s[i];
				start=s[i];
			}
			else {
				bottom++;
				ans[bottom]=s[i];
			}
		}
		cout<<"Case #"<<tc<<": ";
		for(int i=top; i<=bottom; i++)
		{
			cout<<ans[i];
		}
		cout<<endl;
	}
	return 0;
}
