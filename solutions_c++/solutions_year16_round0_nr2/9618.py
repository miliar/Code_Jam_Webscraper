#include <bits/stdc++.h>
using namespace std;
int main(){
	freopen("B-large.in","r",stdin);
	freopen("OutputBLarge.out","w",stdout);
	int tc,cp=0; cin>>tc;
	string s;
	while(tc--){
		cin>>s;
		s=s+'+';
		int ans=0;
		for(int i=0;i<s.size()-1;i++){
			if(s[i]!=s[i+1]) ans++;
		}
		cout<<"Case #"<<++cp<<": "<<ans<<endl;
	}
	return 0;
}
