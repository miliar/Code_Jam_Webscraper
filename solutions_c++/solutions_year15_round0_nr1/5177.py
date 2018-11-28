#include<bits/stdc++.h>
using namespace std;
int main(){
	int tc;
	cin>>tc;
	for(int z=1;z<=tc;z++){
		int n;
		cin>>n;
		string s;
		cin>>s;
		int res=0;
		int standing=(s[0]-'0');
		//cout<<"0: "<<standing<<endl;
		for(int i=1;i<=n;i++){
			
			if(standing>=i){
				standing+=(s[i]-'0');
				//cout<<i<<": "<<standing<<endl;
			}
			if(standing<i && s[i]!='0'){
				
				
				res+=(i-standing);
				standing+=(s[i]-'0')+(i-standing);
				//cout<<i<<": "<<standing<<endl;
				//cout<<"res: "<<": "<<res<<endl;
			}
		}
		cout<<"Case #"<<z<<": "<<res<<endl;
	}
}