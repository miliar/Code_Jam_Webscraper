#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int main(){
	ifstream inp("./bLarge.in");
	ofstream out("./bLarge.out");
	int t;
	inp>>t;
	for(int i=1; i<=t; i++){
		out<<"Case #"<<i<<": ";
		string str;
		inp>>str;
		int j=0;
		int ans = 0;
		bool flag = true; 
		for(int k=0; k<str.size(); k++){
			if(str[k]=='-'){
				flag = false;
			}
		}
		if(flag){
			out<<0<<endl;
		}
		else{
			while(j<str.size()){
				if(str[j]=='-'){
					while(j<str.size() && str[j]=='-'){
						j++;
					}
					ans ++;
				}
				else{
					while(j<str.size() && str[j]=='+'){
						j++;
					}
					if(j!=str.size())ans ++;
				}
			}
			out<<ans<<endl;
		}
	}
}