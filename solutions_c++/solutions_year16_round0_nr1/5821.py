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

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> pii;
typedef vector<pii> vpii;

int n, aux, vezes[10], cnt, test;

void mark(int x) {
	while (x > 0) {
		if (vezes[x%10] == 0) cnt++;
		vezes[x%10]++;
		x /= 10;
	}
}

int main(int argc, char const *argv[]) {
	scanf("%d", &test);
	for (int t = 0; t < test; t++) {
		scanf("%d", &n);
		memset(vezes, 0, sizeof(vezes));
		cnt = 0;
		printf("Case #%d: ", t+1);
		if (n == 0) {
			puts("INSOMNIA");
			continue;
		}
		aux = n;
		do {
			mark(aux);
			aux += n;
		} while (cnt < 10);
		printf("%d\n", aux - n);
	}
	return 0;
}