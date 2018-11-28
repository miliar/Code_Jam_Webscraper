#include <cstdio>
#include <cstring>
#include <queue>

using namespace std;
char S[1024];

int main() {
	int tests;
	scanf("%d", &tests);
	for (int case_no = 1; case_no <= tests; ++case_no) {
		scanf("%s", S);
		int len = strlen(S);
		deque <char> q;
		q.push_front(S[0]);
		for (int i = 1; i < len; ++i) {
			if (q.front() <= S[i]) {
				q.push_front(S[i]);
			} else {
				q.push_back(S[i]);
			}
		}

		for (int i = 0; i < q.size(); ++i)
			S[i] = q[i];

		printf("Case #%d: %s\n", case_no, S);
	}
}