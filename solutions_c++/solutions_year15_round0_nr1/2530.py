#include <bits/stdc++.h>
using namespace std;
int main(){
	int t;
	freopen("in.txt","r+",stdin);
	freopen("out.txt","w+",stdout);
	cin>>t;
	for(int kj=1;kj<=t;kj++){
		int n;
		string s;
		cin>>n>>s;
		int ans=0,tot=s[0]-'0';
		for(int i=1;i<=n;i++){
			int num=s[i]-'0';
			if(num>0){
				if(i>tot){
				 ans+=(i-tot);
				 tot+=(i-tot);
				}
			    tot+=num;
			}

		}
		cout<<"Case #"<<kj<<": "<<ans<<endl;
	}
	return 0;
}
