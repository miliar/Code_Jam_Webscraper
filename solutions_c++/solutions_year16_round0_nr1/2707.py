#include <cstdio>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

string getAsleepNumber(int n) {
	if(0 == n) return "INSOMNIA";
	vector<bool> arr(10, false);
	int count = 0;
	int temp = n;
	while(true) {
		string s = to_string(temp);
		for(char ch : s) {
			int idx = ch - '0';
			if(!arr[idx]) {
				arr[idx] = true;
				count++;
			}
		}
		if(count == 10) return s;
		temp += n;
	}
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t;
	cin >> t;
	for(int cas = 1; cas <=t ; cas++) {
		int n;
		cin >> n;
		cout << "Case #" << cas << ": " << getAsleepNumber(n) << endl;
	}
	return 0;
}
