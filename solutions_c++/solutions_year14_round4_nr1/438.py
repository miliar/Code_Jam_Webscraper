#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int file[10000];
bool vis[10000];

int main() {
	int T;
	cin >> T;
	for (int c = 1; c <= T; c++) {
		int N, C;
		cin >> N >> C;
		for (int i = 0; i < N; i++) {
			cin >> file[i];
		}
		sort(file, file + N);
		memset(vis, 0, sizeof(vis));
		int num = 0;
		for (int i = N - 1; i >= 0; i--) {
			if (vis[i]) continue;
			num++;
			for (int j = i - 1; j >= 0; j--) {
				if (vis[j]) continue;
				if (file[j] + file[i] <= C) {
					vis[j] = true;
					break;
				}
			}
		}
		cout << "Case #" << c << ": " << num << endl;
	}
	return 0;
}