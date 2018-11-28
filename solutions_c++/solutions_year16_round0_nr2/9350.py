#include <bits/stdc++.h>

using namespace std;

int main(){

	int T; 
	cin >> T;
	for(int t = 0; t < T;t++){
		cout << "Case #" << t+1 << ": ";
		string s,tt;
		cin >> s;
		tt = "+";
		while(tt.size()<s.size()){
			tt+="+";
		}
		int counter = 0;
		while(s!=tt){
			counter++;
			char a = s[0];
			char b = '+';
			if(a == '+'){
				b = '-';
			}
			int pos = 0;
			while(pos < s.size() && s[pos]==a){
				s[pos]=b;
				pos++;
			}

		}
		cout << counter << "\n";
	}

	return 0;
}