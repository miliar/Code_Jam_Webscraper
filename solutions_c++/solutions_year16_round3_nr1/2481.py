#include <bits/stdc++.h>
#define vi vector<int>
#define all(v) v.begin(),v.end()
#define pii pair<int,int>
#define mp make_pair
using namespace std;
int main() {
#ifndef ONLINE_JUDGE
	freopen("/home/shiva/Learning/1.txt", "r", stdin);
	freopen("/home/shiva/Learning/2.txt", "w", stdout);
#endif
	ios::sync_with_stdio(false); cin.tie(0);
	int T, N;
	cin >> T;
	int x = 1;
	while (T--) {
		cin >> N;
		int temp;
		vector<pair<int, int>> arr;
		for (int i = 0; i < N; i++) {
			cin >> temp;
			arr.push_back({temp, i});
		}
		cout << "Case  #" << x << ": "; x++;
		sort(arr.begin(), arr.end(), greater<pair<int, int>>());
		int total = N;
		while (arr[0].first != 0) {
			if (arr[0].first == arr[1].first) {
				if (arr[0].first == 1 && total % 2 == 1) {
					cout << (char)('A' + arr[0].second);
					arr[0].first--;
				} else {
					cout << (char)('A' + (arr[0].second)) << (char)('A' + (arr[1].second));
					arr[0].first--; arr[1].first--;
				}
			} else if (arr[0].first >= 2) {
				char c = (char)('A' + (arr[0].second));
				cout << c << c;
				arr[0].first -= 2;
			} else if (arr[0].first == 1) {
				cout << (char)('A' + (arr[0].second));
				arr[0].first--;
			}

			if (arr[0].first == 0) total--;
			if (arr[1].first == 0) total--;
			cout << " ";
			sort(arr.begin(), arr.end(), greater<pair<int, int>>());
		}
		cout << endl;
	}

}