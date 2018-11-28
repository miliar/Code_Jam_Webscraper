#include<iostream>
using namespace std;
#include<string>
int main()
{
	freopen("data.in","r",stdin);
	freopen("data.out","w",stdout);
	int t; cin>>t;
	for(int k=1;k<=t;k++){
		int s_max; cin>>s_max;
		string str; cin>>str;
		int tot=0,ans=0;
		for(int i=0;i<=s_max;i++){
			if(tot>=i) { tot+=str[i]-'0'; }
			else { ans+=i-tot; tot=i; tot+=str[i]-'0'; }
			//cout<<ans<<" ";
		}
		cout<<"Case #"<<k<<": ";
		cout<<ans<<endl;
	}
	return 0;
}