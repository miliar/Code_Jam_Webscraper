#include <iostream>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <string>
#include <cstring>
using namespace std;

int main() {
	int T;
	int a[100][100];

	cin >> T;
	for (int t = 1; t <= T; ++t) {
		int N, M;
		cin >> N >> M;
		int h[100] = {0};
		int v[100] = {0};
		for (int i = 0; i < N; ++i)
			for (int j = 0; j < M; ++j)
				cin >> a[i][j];
	
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < M; ++j) {
				if (a[i][j] > h[i])
					h[i] = a[i][j];
			}
		}
		for (int j = 0; j < M; ++j) {
			for (int i = 0; i < N; ++i) {
				if (a[i][j] > v[j])
					v[j] = a[i][j];
			}
		}
		string ans = "YES";
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < M; ++j) {
				if (a[i][j] < h[i] && a[i][j] < v[j])
				{
					ans = "NO";
					goto output;
				}
			}
		}

output:
		cout << "Case #" << t << ": " << ans << endl;
	}

	return 0;
}

