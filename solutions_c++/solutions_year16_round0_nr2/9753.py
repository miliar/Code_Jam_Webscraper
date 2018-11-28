#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin>>t;
	for(int tc=0;tc<t;tc++){
		string str;
		cin>>str;
		int ans=0;
		int len = str.length();
		
		int minus = 0;
		for(int i=len-1;i>=0;i--){
			if(ans%2){
				str[i] = (str[i]=='-')?'+':'-';
			}
			
			if(str[i]=='-'){
				minus++;
			}
			else{
				if(minus>0){
					ans++;
                                        minus = 1;
				}
			}
		}
		
		if(minus >0)ans++;
		
		cout<<"Case #"<<tc+1<<": "<<ans<<endl;
	}
	return 0;
}
