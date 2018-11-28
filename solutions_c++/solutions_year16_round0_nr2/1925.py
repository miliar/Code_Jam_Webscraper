#include <bits/stdc++.h>
using namespace std;

int main(){	
	int t; cin >> t;
	for(int i=0; i<t; i++){
		string s; cin >> s;
		int flips = 0;
		for(int k=s.size()-1; k>=0; k--){
			if(s[k]=='-'){
				flips++;	
				for(int j=0; j<k; j++)
					if(s[j]=='+') s[j] = '-';
					else s[j] = '+';
			}
		}		
		cout << "Case #" << (i+1) << ": " << flips << '\n';
	}
	return 0;
}
