#include <bits/stdc++.h>
using namespace std;
#define fr(i,a,b) for (int i = a; i < b; i++)
#define fre(i,a,b) for (int i = a; i <= b; i++)
#define cle(a,b) memset(a, b, sizeof(a))

char s[1000];

int main () {
	int T;
	scanf ("%d", &T);
	fre(i,1,T) {
		scanf (" %s", s);
		bool mud = 0;
		int tot = 0;
		if (s[0] == '+') mud = 1;
		for (int j = 1; s[j] != '\0'; j++) {
			if (s[j] == '-' && mud) { tot++; mud = 0;}
			else if (s[j] == '+' && !mud) { tot++; mud = 1;}
		}
		if (!mud) tot++;
		printf ("Case #%d: %d\n", i, tot);
	}	
	return 0;
}
