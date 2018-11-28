#include <bits/stdc++.h>
using namespace std;

int main(){
	freopen("aain", "r", stdin);
	freopen("aaout", "w", stdout);	
	string str;
	int tc, t=0;
	cin>>tc;
	
	while(tc--){
		t++;
		cin>>str;
		int ans= 0;
		bool flg= false;
		for(int i=(int)str.length()-1;i>=0;i--){
			flg= false;
			while(str[i]=='-'){
				i-=1;
				flg= true;
			}
			if(flg){
				ans++;
				for(int j=0;j<=i;j++){
					if(str[j]=='+') str[j]= '-';
					else str[j]= '+';
				}
				i++;
			}
		}
		cout<< "Case #"<<t<<": "<<ans<<"\n";
	}
	
}
