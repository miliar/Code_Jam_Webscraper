#include <bits/stdc++.h>

using namespace std;

int main() {
	int T;
	cin>>T;
	for(int i = 0; i < T; i++) {
		int smax;
		cin>>smax;
		string s;
		cin>>s;
		
		int sum = 0;
		int needed = 0;
		//cout<<"Case: "<<i+1<<"\n";
		for(int j = 0; j < s.size(); j++){
			if (sum >= j) {
				sum += s[j]-'0';
			} else {
				if(s[j]-'0' > 0){
					needed += j - sum;
					//cout<<"j: "<<j<<" sum: "<<sum<<"\n";
					sum += s[j]-'0';
					sum += needed;
				}
			}
		}		
		cout<<"Case #"<<i+1<<": "<<needed<<"\n";
	}
}
