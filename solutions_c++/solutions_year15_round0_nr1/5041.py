#include <bits/stdc++.h>
//Compile using GNU g++

using namespace std;
int main(){
	freopen("A-large.in","rt",stdin);
	freopen("pa.out","w+t",stdout);
	int tc,nc=0;cin>>tc;
	while(tc-->0){
		nc++;
		int n;cin>>n;
		string st;cin>>st;
		int ans=0,now=0;
		for(int i=0;i<=n;i++){
			if(st[i]=='0')continue;
			while(now<i){
				now++;
				ans++;
			}
			now+=st[i]-'0';
		}
		cout<<"Case #"<<nc<<": "<<ans<<endl;
	}
	return 0;
}
