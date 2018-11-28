#include<bits/stdc++.h>
using namespace std;
int t,sz,ans;
char sig;
string s;
int main(){
	cin >> t;
	for(int cases=1;cases<=t;cases++){
		ans=0;
		cin >> s;
		sz=s.length();
		sig=s[0];
		for(int i=0;i<sz;i++){
			if(s[i]!=sig){
				ans++;
				sig=s[i];
			}
		}
		if(sig=='-') ans++;
		cout << "Case #"<<cases<<": "<<ans<<endl;
		
	}
}

