#include<bits/stdc++.h>
using namespace std;

int main(){
	freopen("output.txt","w",stdout);
	int T,val=1;
	cin>>T;
	while(T--){
		string s,t="";
		cin>>s;
		t += s[0];
		for(int i=1;i<s.length();i++){
			if(s[i]>=t[0]){
				t = s[i] + t;
			}
			else{
				t = t +s[i];
			}
		}
		printf("Case #%d: ",val);
		cout<<t<<endl;
		val++;
		
	}
	return 0;
}
