#include <iostream>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <cstdio>
using namespace std;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int test,t;
	cin >> t;
	for (test = 1; test <= t; test++){
		int n;
		cin >> n;
		if (n == 0){
			cout << "Case #" << test << ": " << "INSOMNIA" << endl;
			continue;
		}
		bool nums[10] = {false};
		for (int i = 1; i <= 100000; i++) {
			int k = n*i;
			string s = to_string(k);
			for (int j = 0; j < s.size(); j++){
				int g = s[j] - '0';
				nums[g] = true;
			}
			bool b = true;
			for (int j = 0; j < 10; j++) {
				if (nums[j] == false)
				{
					b = false;
					break;
				}
			}
			if (b) {
				cout << "Case #" << test << ": " << k << endl;
				break;
			}
		}
	}
	return 0;
}