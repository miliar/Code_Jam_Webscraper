#include <iostream>
#include <string>
#include <cassert>

using namespace std;

int solve(int s_max, const std::string& shies) {
	int ans = 0;
	int has = shies[0] - '0';
	for (int i = 1; i <= s_max; i++) {
		int num_pos = shies[i] - '0';
		if (num_pos == 0) continue;
		if (has < i) {
			ans += i - has;
			has = i;
		}
		has += num_pos;
	}
	return ans;
}

int main() {
	int t;
	cin >> t;
	int s_max;
	string shies;
	for (int i = 1; i <= t; i++) {
		cin>>s_max>>shies;
		// cout<<s_max<<" "<<shies<<endl;
		cout<<"Case #"<<i<<": "<<solve(s_max, shies)<<endl;
	}
}


