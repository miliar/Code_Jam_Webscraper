#include <bits/stdc++.h>


using namespace std;
#define FOR(i, n) for (int i=0; i<(n); i++)
#define ll long long

char s[1010];

int k;
void flip(int i)
{
	FOR(j, k)
		s[j + i] = (s[j + i] == '-') ? '+' : '-';
}

void vyres(void)
{
	int n;
	scanf("%s %d", s, &k);
	n = strlen(s);
	int c = 0;
	FOR(i, n - k + 1)
		if(s[i] == '-')
			flip(i), c++;
	
	FOR(i, n)
		if (s[i] == '-'){
			printf("IMPOSSIBLE\n");
			return;
		}
	
	printf("%d\n", c);
}

int main(void)
{
	int t;
	scanf("%d", &t);
	FOR(i, t){
		printf("Case #%d: ", i + 1);
		vyres();
	}
}
