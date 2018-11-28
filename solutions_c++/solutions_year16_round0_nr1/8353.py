#include <cstdio>
#define REP(i, n) for(int i = 0;i < n;++i)
bool have[11];

bool ok () {
	REP(i, 10) if(!have[i]) return false;
	return true;
}

void add (int x) {
	while(x) {
		have[x % 10] = true;
		x /= 10;
	}
}

int f (int x) {
	REP(i, 10) have[i] = false;
	int cur = x;
	add(cur);
	while(!ok()) {
		cur += x;
		add(cur);
	}
	return cur;
}

int main () {
	int t;
	scanf("%d", &t);
	REP(i, t) {
		int x;
		scanf("%d", &x);
		printf("Case #%d: ", i + 1);
		if(!x) printf("INSOMNIA\n");
		else printf("%d\n", f(x));
	}
}
