#include<bits/stdc++.h>
using namespace std;
int main() {
	int t;
	cin>>t;
	for(int j=1;j<=t;j++) {
	   string s;
	   int n;
	   cin>>n>>s;
	   int standing=s[0]-'0';
	   int cnt =0;
	   for(int i=1;i<=n;i++){
		if(s[i]=='0'){
		}
		else {
		  if(standing>=i){
			standing+=(s[i]-'0');
		  }
		  else {
		    cnt = cnt+(i-standing);	
		    standing+=(s[i]-'0')+(i-standing);
		  }
		}
	   }
	   cout<<"Case #"<<j<<": "<<cnt<<endl;
	}
}
