#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <string>
#include <stack>

using namespace std;

int T, V[2000];
string S;
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> T;
	for (int t = 1; t <= T; t++) {
		memset(V, 0, sizeof(V));
		char best = 'A';

		cin >> S;

		printf("Case #%d: ", t);

		stack<char> st;
		for (int i = 0; i < S.size(); i++) {
			if (S[i] >= best) {
				st.push(S[i]);
				best = S[i];

				V[i] = 1;
			}
		}

		while (!st.empty()) {
			printf("%c", st.top());
			st.pop();
		}

		for (int i = 0; i < S.size(); i++) if (!V[i])
			printf("%c", S[i]);
		printf("\n");
	}
}