#include <iostream>
#include <algorithm>

using namespace std;

int v[10010];

int solve() {
	int N, X;

	cin >> N >> X;

	for(int i = 0; i < N; i++)
		cin >> v[i];

	sort(v, v + N);

	int ans = 0;
	for(int i = 0, j = N - 1; i <= j;) {
		if(i == j) {
			ans++;
			break;
		}

		if(v[i] + v[j] <= X) {
			ans++;
			i++; j--;
		} else {
			ans++;
			j--;
		}
	} 

	return ans;
}

int main() {
	int T;
	cin >> T;
	for(int i = 1; i <= T; i++) {
		cout << "Case #" << i << ": " << solve()  << endl;
	}
}