#include <iostream>
#include <set>
#define ll long long
using namespace std;

ll solve(string s){
	ll ret = 0;
	int l = s.length();
	for(int i = 0; i < l; i++){
		if(s[i] == '-'){
			if(i == 0){
				ret++;
			}
			else if(s[i - 1] == '+'){
				ret += 2;
			}
		}
	}
	return ret;
}

int main() {
	int t;
	string s;
	cin >> t;
	for(int i = 1; i <= t; i++){
		cin >> s;
		cout << "Case #" << i << ": " << solve(s) <<endl;
	}
	return 0;
}