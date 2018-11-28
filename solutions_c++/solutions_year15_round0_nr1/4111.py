
#include <bits/stdc++.h>
using namespace std;

int main() {

	freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w", stdout);
	int t;
	cin>>t;
	for(int j=1;j<=t;j++){
		string s;
		int l,i,sum=0,ans=0;
		cin>>l;
		cin>>s;
		sum+=s[0]-'0';
		for(i=1;i<=l;i++){
			if(sum>=i){
				sum+=s[i]-'0';
			}
			else{
				ans+=i-sum;
				sum=i;
				sum+=s[i]-'0';
			}

		}
		cout<<"Case #"<<j<<": "<<ans<<endl;

	}
	return 0;
}
