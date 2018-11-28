#include <stdio.h>
#include <string>

char str[10000];
int main()
{
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++) {
		int N, L;
		scanf("%d%d", &N, &L);
		bool imp = false;
		for (int i=0; i<N; i++) {
			scanf(" %s", str);
			bool f = true;
			for (int j=0; j<L; j++) {
				if (str[j] == '0') {
					f = false;
					break;
				}
			}
			if (f) {
				imp = true;
			}
		}
		scanf(" %s", str);
		if (imp) {
			printf("Case #%d: IMPOSSIBLE\n", t);
		} else {
			std::string a, b;
			if (L == 1) {
				a = "?";
				b = "0";
			} else {
				for (int i=0; i<L-1; i++) {
					a += '?';
				}
				b = "010101010101010101010101010101010101010101010101010?10101010101010101010101010101010101010101010101010";
			}
			printf("Case #%d: %s %s\n", t, a.c_str(), b.c_str());
		}
	}

	return 0;
}