#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main() {
	int N; 
	cin>> N ; 

	for(int T = 1 ; T <= N ; T++) {
		string s;
		cin >> s ;
		reverse(s.begin(), s.end());

		int ret = 0;
		char a = '+';
		for (int i = 0 ; i < s.size() ; i++) {
			if( s[i] == a ) continue;
			if (a == '+') a = '-';
			else a = '+';
			ret++;
		}
		cout<<"Case #"<<T<<": "<<ret<<endl;
	}
	return 0 ;
}