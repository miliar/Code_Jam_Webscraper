#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

int main(){
	int T;
	cin >> T;
	for(int tc=1; tc <= T; ++tc){
		string s;
		int k;
		cin >> s >> k;
		int hm = 0;
		for(int i=0; i+k<s.size()+1; ++i){
			if(s[i] == '-'){
				++hm;
				for(int j=0; j<k; ++j){
					s[i+j] = (s[i+j]=='-') ? '+' : '-';
				}
			}
		}
		for(int i=0; i<k; ++i){
			if(s[s.size() - i - 1] != '+') {
				cerr << "BAD:" << s << endl;
				hm = -1;
				break;
			}
		}
		cout << "Case #" << tc << ": ";
		if(hm < 0) cout << "IMPOSSIBLE" << endl;
		else cout << hm << endl;
	}
}