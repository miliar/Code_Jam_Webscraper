#include <iostream>
using namespace std;
int main(){
	string s;
	int t;
	cin >> t;
	for(int I=1; I<=t; I++){
		cin >> s;
		char c = s[0];
		int res = 0;
		for(int i=0; i<s.size();i++){
			if(s[i] != c){
				res++;
				c = s[i];
			}
		}
		if(c=='-') res++;
		cout << "Case #" << I << ": " << res << endl;
	}
}
