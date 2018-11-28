#include <bits/stdc++.h>
using namespace std;

#define INF 0x3F3F3F3F
#define INFL 0x3F3F3F3F3F3F3F3FLL
#define sz(X) int((X).size())
#define st first
#define nd second
#define pb push_back
#define mp make_pair
#define ll long long

int main(int argc, char const *argv[]) {
	int test, ind, ans, len, correct;
	scanf("%d", &test);
	char str[128], aux[128];
	for (int t = 0; t < test; ++t) {
		scanf("%s", str);
		len = strlen(str), ans = 0, correct = 0;
		for (int i = 0; str[i]; i++)
			correct += (str[i] == '+');
		while (correct < len) {
			for (int i = 0; str[i]; i++) {
				if (str[i] == '+') {
					str[i] = '-';
					correct--;
				} else {
					if (i > 0) ans++;
					break;
				}
			}
			for (int i = len-1; i >= 0; i--) {
				if (str[i] == '-') {
					ind = i;
					break;
				}
			}
			for (int i = 0; i <= ind; i++) {
				aux[i] = str[ind-i];
			}
			for (int i = 0; i <= ind; i++) {
				if (aux[i] == '+') {
					str[i] = '-';
					correct--;
				} else {
					str[i] = '+';
					correct++;
				}
			}
			ans++;
		}
		printf("Case #%d: %d\n", t+1, ans);
	}
	return 0;
}