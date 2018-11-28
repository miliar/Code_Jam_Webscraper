#include <bits/stdc++.h>

#define i64 long long
#define u64 unsigned long long
#define i32 int
#define u32 unsigned int

#define pii pair<int, int>
#define pll pair<long long, long long>

#define defmod 1000000007
using namespace std;

int vittu(string s){
	int n = s.length();
	int ans = 0;
	
	for(int i = n-1; i >= 0; i--){
		if(s[i] == '-'){
			ans++;
			for(int j = i; j >= 0; j--){
				if(s[j] == '-')
					s[j] = '+';
				else
					s[j] = '-';
			}
		}
	}
	return ans;
}

int main(){
	cin.sync_with_stdio(0);
	cin.tie(0);
	
	int tests; cin >> tests;
	for(int test = 1; test <= tests; test++){
		string s; cin >> s;
		int ans = vittu(s);
		
		cout << "Case #" << test << ": " << ans << endl;

	}
	return 0;
}