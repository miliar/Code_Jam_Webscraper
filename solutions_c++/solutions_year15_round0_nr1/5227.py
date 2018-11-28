#include <stdio.h>
#include <string.h>


using namespace std;

const int N = 1000 + 239;

int n;
char s[N + 1];

int t;

int main() {
	scanf("%d", &t);
	for (int q = 0; q < t; ++q) {	
		scanf("%d ", &n);
		gets(s);          
		n = strlen(s);
		int ans = 0;
		for (int i = 0, ed = 0; i < n; ++i) {
			if (s[i] == '0')
				continue;
		    //printf("%d %d %c\n", i, ed, s[i]);
			if (ed < i) {
				ans += i - ed;
				ed = i;
			}
			ed += s[i] - '0';
		
		}
		printf("Case #%d: %d\n", q + 1, ans);
	}


	return 0;
}


