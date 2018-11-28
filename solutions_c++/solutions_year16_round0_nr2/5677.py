#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <queue>
#include <vector>
using namespace std;
typedef long long int lli;
typedef pair<lli, lli> ii;
const int MAXN = 10010, MAXL = 1000010;

int n, flips;
char s[128];

int findUltimo();
int findPrimeiro();
void flip(int limite);

int main() {
	//freopen("B-large.in", "r", stdin);
	//freopen("output-large.txt", "w", stdout); 

	int t;
	scanf("%d", &t);

	for(int test=1; test<=t; test++) {
		printf("Case #%d: ", test);

		scanf("%s", s);
		n = strlen(s);

		flips = 0;

		int ha = 10;
		while(1) {
			int ultimo = findUltimo();
			if(ultimo == -1) break;

			int primeiro = findPrimeiro();
			if(primeiro > 0 and primeiro <= ultimo) {
				flip(primeiro);
				flips++;
			}
			flip(ultimo+1);
			flips++;
		}

		printf("%d\n", flips);
	}
}

void flip(int limite) {
	//printf("%s %d\n", s, limite);
	for(int i=0, j=limite-1; i<j; i++, j--) {
		char aux = s[i];
		s[i] = (s[j] == '-' ? '+' : '-');
		s[j] = (aux == '-' ? '+' : '-');
	}
	if(limite%2 == 1) {
		s[limite/2] = (s[limite/2] == '-' ? '+' : '-');
	}
}

int findUltimo() {
	for(int i=n-1; i>=0; i--) {
		if(s[i] == '-') return i;
	}
	return -1;
}

int findPrimeiro() {
	for(int i=0; i<n; i++) {
		if(s[i] == '-') return i;
	}
	return -1;
}
