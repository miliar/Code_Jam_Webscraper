#include <iostream>
#include <fstream>
#include <sstream>
#include <cstring>

using namespace std;

typedef long long ll;

const int maxn = 105;
bool arr[maxn];
int n;

void flip(int k) {
	int cpy[maxn];
	for (int i = 0; i <= k; i++) {
		cpy[k-i] = !arr[i];
	}
	for (int i = 0; i <= k; i++) {
		arr[i] = cpy[i];
	}
}

int main() {
	ios_base::sync_with_stdio(0);
	ifstream cin("All.in");
	ofstream cout("All.out");
	int t;
	cin >> t;
	for (int rep = 1; rep <= t; rep++) {
		cout << "CASE #" << rep << ": ";
		string str;
		cin >> str;
		n = str.size();
		for (int i = 0; i < n; i++) {
			arr[i] = str[i] == '+';
		}
		int cnt = 0;
		for (int i = 0; i < n-1; i++) {
			if (arr[i] != arr[i+1]) {
				flip(i);
				cnt++;
			}
		}
		if (!arr[0]) cnt++;
		cout << cnt << '\n';
	}
	return 0;
}

