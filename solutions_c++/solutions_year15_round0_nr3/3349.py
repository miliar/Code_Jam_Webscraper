#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char c[10005];
char state = '1';
int neg = 0;

char do_state(char c)
{
	switch (state) {
	case '1':
		state = c;
		break;
	case 'i':
		state = (c == '1' ? 'i' : c == 'i' ? '1' : c == 'j' ? 'k' : 'j');
		if (c == 'i' || c == 'k') neg = 1 - neg;
		break;
	case 'j':
		state = (c == '1' ? 'j' : c == 'i' ? 'k' : c == 'j' ? '1' : 'i');
		if (c == 'i' || c == 'j') neg = 1 - neg;
		break;
	case 'k':
		state = (c == '1' ? 'k' : c == 'i' ? 'j' : c == 'j' ? 'i' : '1');
		if (c == 'j' || c == 'k') neg = 1 - neg;
		break;
	default: break;
	}
	return state;
}

void solve()
{
	int l, x;
	scanf("%d%d", &l, &x);
	scanf("%s", c);
	//printf("%d %d [%s]\n", l, x, c);

	for (int i = 1; i < x; i++) {
		memcpy(&c[i*l], c, l);
	}

	int i = 0;
	state = '1'; neg = 0;
	while (i < x*l) {
		if (do_state(c[i++]) == 'i' && neg == 0) break;
	}
	state = '1'; neg = 0;
	while (i < x*l) {
		if (do_state(c[i++]) == 'j' && neg == 0) break;
	}
	state = '1'; neg = 0;
	while (i < x*l) {
		do_state(c[i++]);
	}
	if (state == 'k' && neg == 0) {
		printf("YES\n");
	} else {
		printf("NO\n");
	}
}

int main()
{
	int t; scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		solve();
	}
}
