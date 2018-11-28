#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
	int t, tt = 1;
	for(cin >> t; t; t--, tt++){
		cout << "Case #" << tt << ": ";
		string s, t = "";
		cin >> s;
		t = s[0];
		for(int i = 1; i < s.size(); i++){
			if(s[i] >= t[0]){
				t = s[i] + t;
			}
			else	t += s[i];
		}
		cout << t << endl;
	}
	return 0;
}