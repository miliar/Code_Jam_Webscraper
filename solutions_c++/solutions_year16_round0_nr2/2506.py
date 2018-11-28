#include<bits/stdc++.h>
using namespace std;

int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	freopen("C:/Users/HP/Desktop/CodeJam/codejam_2_large_input.txt","r",stdin);//redirects standard input
	freopen("C:/Users/HP/Desktop/CodeJam/codejam_2_large_output.txt","w",stdout);//redirects standard output
	int t,ans;
	string s,a;
	cin>>t;
	for(int tc=1; tc<=t; tc++)
	{
		cin>>s;
		bool chk=0;
		for(int i=0; i<s.length(); i++)
		{
			if(s[i]=='-') {
				chk=1;
				break;
			}
		}
		if(!chk) {
			cout<<"Case #"<<tc<<": "<<0<<endl;
			continue;
		}
		int cnt=0,end=0;
		ans=0;
		for(int i=s.length()-1; i>=0; i--)
		{
			if(s[i]!='+') {
				end=i;
				//cout<<" "<<s[s.length()-1]<<" "<<i<<" "<<end<<endl;
				break;
			}
		}
		if(s[0]=='+') cnt++;
		//cout<<" "<<s.length()<<" "<<end<<endl;
		for(int i=1; i<=end; i++)
		{
			if(s[i]=='+' && s[i-1]=='-') cnt++;
		}
		ans=2*cnt;
		if(s[0]=='-') ans+=1;
		//cout<<" "<<s<<" "<<cnt<<" "<<ans<<endl;
		cout<<"Case #"<<tc<<": "<<ans<<endl;
	}
	return 0;
}
