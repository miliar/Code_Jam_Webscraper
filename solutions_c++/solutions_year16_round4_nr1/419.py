#include <stdio.h>
#include <string>


int main()
{
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++) {
		int N, R, P, S;
		scanf("%d%d%d%d", &N, &R, &P, &S);
		int r[15] = {R};
		int p[15] = {P};
		int s[15] = {S};
		bool valid = true;
		for (int i=0; i<N; i++) {
			int n = 1<<(N-i);
			s[i+1] = n/2-r[i];
			r[i+1] = n/2-p[i];
			p[i+1] = n/2-s[i];
			if (s[i+1] < 0 || r[i+1] < 0 || p[i+1] < 0) {
				valid = false;
				break;
			}
		}
		if (!valid) {
			printf("Case #%d: IMPOSSIBLE\n", t);
			continue;
		}
		std::string str[15];
		if (s[N] > 0) {
			str[N] = "S";
		}
		if (r[N] > 0) {
			str[N] = "R";
		}
		if (p[N] > 0) {
			str[N] = "P";
		}
		for (int i=N; i>0; i--) {
			for (int j=0; j<str[i].size(); j++) {
				if (str[i][j] == 'S') {
					if ((i-1)%6 == 0 || (i-1)%6 == 1 || (i-1)%6 == 5) {
						str[i-1] += "PS";
					} else {
						str[i-1] += "SP";
					}
				}
				if (str[i][j] == 'R') {
					if ((i-1)%6 == 0 || (i-1)%6 == 4 || (i-1)%6 == 5) {
						str[i-1] += "RS";
					} else {
						str[i-1] += "SR";
					}
				}
				if (str[i][j] == 'P') {
					if ((i-1)%6 == 0 || (i-1)%6 == 1 || (i-1)%6 == 2) {
						str[i-1] += "PR";
					} else {
						str[i-1] += "RP";
					}
				}
			}
		}
		printf("Case #%d: %s\n", t, str[0].c_str());
	}

	return 0;
}