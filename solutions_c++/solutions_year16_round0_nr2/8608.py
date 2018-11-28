#include <iostream>
#include<bits/stdc++.h>
using namespace std;

int main() {
	long long int t;
	cin>>t;
	for(long long int i = 1; i <= t; i++ ){
		cout<<"Case #"<<i<<": ";
		long long int ans = 0;
		string s, I , N;
		cin>>s;
		N= s;
		I = N;
		for(long long int i1 = 0; i1 < s.length(); i1++){
			if(s[i1] == '+'){
				N[i1] = '+';
				I[i1] = '-';
			}
			else{
				N[i1] = '-';
				I[i1] = '+';
			}
		}
		//cout<<" "<<N<<" "<<I<<endl;
		int flag = 1;
		for(long long i1 = 0; i1 < s.length(); i1++ ){
			
			if(s[s.length()-1-i1] == '+'){
				continue;
			}	
			else{
				ans++;
				if(flag == 1){
					s = I;
					flag = 0;
					
				}
				else{
					s = N;
					flag = 1;
				}
			}
			//cout<<s<<" "<<N<<" "<<I<<endl;
		}
		cout<<ans<<endl;
	}
	return 0;
}