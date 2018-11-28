/* Tomasz [Tommalla] Zakrzewski, Google Code Jam 2015
 * Qualification Round: Problem C. Dijkstra
 */
#include <cstdio>
#include <cmath>

using namespace std;


char trans[256][256];
char word[10000];
char origword[10000];
char res[10000][10000];


char multiply(char a, char b) {
	char sgn = a/(char)abs(a) * b/(char)abs(b);
	return trans[(int)abs(a)][(int)abs(b)] * sgn;
}


bool solve(int n) {
	for (int i = 0; i < n - 2; ++i) {
		if (res[0][i] == 'i') {
			for (int j = i + 1; j < n - 1; ++j) {
				if (res[i + 1][j] == 'j' && res[j + 1][n - 1] == 'k') {
					return true;
				}
			}
		}
	}

	return false;
}


int main() {
	trans[1][1] = 1;
	trans['i'][1] = 'i';
	trans['j'][1] = 'j';
	trans['k'][1] = 'k';

	trans[1]['i'] = 'i';
	trans['i']['i'] = -1;
	trans['j']['i'] = -'k';
	trans['k']['i'] = 'j';

	trans[1]['j'] = 'j';
	trans['i']['j'] = 'k';
	trans['j']['j'] = -1;
	trans['k']['j'] = -'i';

	trans[1]['k'] = 'k';
	trans['i']['k'] = -'j';
	trans['j']['k'] = 'i';
	trans['k']['k'] = -1;
	int t;
	scanf("%d", &t);

	for (int c = 1; c <= t; ++c) {
		int l, x;
		scanf("%d%d%s", &l, &x, origword);
		for (int i = 0; i < x; ++i) {
			for (int j = 0; j < l; ++j) {
				word[i * l + j] = origword[j];
			}
		}

		for (int i = 0; i < l * x; ++i) {
			char ch = 1;
			for (int j = i; j < l * x; ++j) {
				ch = multiply(ch, word[j]);
				res[i][j] = ch;
			}
		}
		printf("Case #%d: %s\n", c, solve(l * x) ? "YES" : "NO");

	}
	return 0;
}