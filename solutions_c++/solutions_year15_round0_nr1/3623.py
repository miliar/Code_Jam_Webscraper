#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int T;

int solve(){
	int x, n, sum = 0, m = 0;
	string s;
	cin >> n >> s;
	for(int i = 0; i <= n; i++){
		m = max(m, i - sum);
		sum += s[i] - '0';
	}

	return m;
}

int main(){
	cin >> T;
	for(int i = 0; i < T; i++) cout << "Case #" << i+1 << ": " << solve() << endl;
	return 0;
}