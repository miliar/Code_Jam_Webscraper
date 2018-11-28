// By Aman Jain(jainaman224)
// 9/4/16

#include <iostream>

using namespace std;

int main(){
	int i,j,ans,x,t;
	string s;
	cin >> t;
	for(i=1;i<=t;i++){
		ans=x=0;
		cin >> s;
		for(j=0;j<s.length();j++){
			if(s[j]=='+')
				x=1;
			else if(s[j]=='-' && x==0){
				x=2;
				ans++;
			}
			else if(s[j]=='-' && x==1){
				x=2;
				ans+=2;
			}
		}
		cout << "Case #" << i << ": " << ans << endl;
	}
}