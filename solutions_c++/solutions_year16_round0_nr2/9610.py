#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

int main(int argc, char** argv) {
	int T;
	int test_case;

	scanf("%d", &T);
	for (test_case = 1; test_case <= T; ++test_case) {
		char S[101] = { 0, };
		scanf("%s", S);

		printf("Case #%d: ", test_case);

		int len = strlen(S);
		int nFlip = 0;
		int flag = 0;
		char chk[] = { '-', '+' };
		
		for (int i = len - 1; i >= 0; --i) {
			if (S[i] == chk[flag] && S[i + 1] != chk[flag]) {
				nFlip++;
				flag = !flag;
			}
		}

		printf("%d\n", nFlip);
	}

	return 0;
}