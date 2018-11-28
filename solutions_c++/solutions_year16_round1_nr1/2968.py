#include <cstdio>
#include <cstdlib>
#include <vector>

using namespace std;

const int S_MAX = 1000;

char S[S_MAX];
vector<char> R;

void print_result(int t) {
	printf("Case #%d: ", t);
	for (int i = 0; i < R.size(); ++i) {
		printf("%c", R[i]);
	}
	printf("\n");
}

int main() {
	int T;
	scanf("%d", &T); getchar();
	for (int t = 1; t <= T; ++t) {
		char c;
		int n = 0;
		while ((c = getchar()) != '\n') {
			S[n++] = c;
		}
		R.clear();
		R.push_back(S[0]);
		for (int i = 1; i < n; ++i) {
			if (S[i] >= R[0]) {
				R.insert(R.begin(), S[i]);
			} else {
				R.push_back(S[i]);
			}
		}
		print_result(t);
	}
	return 0;
}