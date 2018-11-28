#include <iostream>
#include <stack>

using std::cin;
using std::cout;
using std::endl;
using std::stack;

int a[100][100];
int left[100], right[100];
bool coverd[100][100];

int main() {
	int T, N, M;
	cin >> T;
	for (int CASE = 1; CASE <= T; CASE++) {
		bool ok = true;
		cin >> N >> M;
		for (int i = 0; i < N; i++)
			for (int j = 0; j < M; j++) {
				cin >> a[i][j];
				coverd[i][j] = false;
			}

		stack<int> st;
		for (int i = 0; i < N; i++) {
			st.push(0);
			for (int j = 1; j <= M; j++) {
				int right_most = st.top();
				int val = j == M ? 1000 : a[i][j];
				while (!st.empty() && a[i][st.top()] < val) {
					right[st.top()] = right_most;
					st.pop();
				}
				st.push(j);
			}
			st.pop();
			st.push(M-1);
			for (int j = M-2; j >= -1; j--) {
				int left_most = st.top();
				int val = j == -1 ? 1000 : a[i][j];
				while (!st.empty() && a[i][st.top()] < val) {
					left[st.top()] = left_most;
					st.pop();
				}
				st.push(j);
			}
			st.pop();
			for (int j = 0; j < M; j++) {
				// cout << left[j] << ' ' << right[j] << endl;
				if (left[j] == 0 && right[j] == M-1)
					coverd[i][j] = true;
			}
		}

		for (int i = 0; i < M; i++) {
			st.push(0);
			for (int j = 1; j <= N; j++) {
				int right_most = st.top();
				int val = j == N ? 1000 : a[j][i];
				while (!st.empty() && a[st.top()][i] < val) {
					right[st.top()] = right_most;
					st.pop();
				}
				st.push(j);
			}
			st.pop();
			st.push(N-1);
			for (int j = N-2; j >= -1; j--) {
				int left_most = st.top();
				int val = j == -1 ? 1000 : a[j][i];
				while (!st.empty() && a[st.top()][i] < val) {
					left[st.top()] = left_most;
					st.pop();
				}
				st.push(j);
			}
			st.pop();
			for (int j = 0; j < N; j++) {
				// cout << left[j] << ' ' << right[j] << endl;
				if (left[j] == 0 && right[j] == N-1)
					coverd[j][i] = true;
			}
		}
		for (int i = 0; i < N; i++)
			for (int j = 0; j < M; j++)
				if (!coverd[i][j]) {
					ok = false;
					goto result;
				}
result:
		cout << "Case #" << CASE << ": " << (ok ? "YES" : "NO") << endl;
	}
}