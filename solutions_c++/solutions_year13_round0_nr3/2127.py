#include <stdio.h>
#include <string.h>
#include <math.h>

bool isps(int n) {
	long long r1, r2, t1, t2;
	char buf[200];
	bool flag = true;
	sprintf(buf, "%d", n);
	t1 = strlen(buf);
	for(r1=0; r1<t1/2; r1++) {
		if(buf[r1] != buf[t1-1-r1]) {
			flag = false;
			break;
		}
	}
	return flag;
}

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	long long t, a, b;
	long long ps[10000], cnt;
	long long lo, hi;
	long long cs, r1, r2, r3, t1, t2, t3;
	bool dbg = true;
	dbg = false;
	scanf("%ld", &t);
	cnt = 0;
	for(r1=1; r1<31; r1++) {
		if(!isps(r1)) continue;
		t1 = r1 * r1;
		if(isps(t1)) {
			ps[cnt++] = t1;
		}
	}
	for(cs=1; cs<=t; cs++) {
		scanf("%ld%ld", &a, &b);
		t2 = 0;
		for(r1=0; r1<cnt; r1++) {
			if(ps[r1] >=a && ps[r1] <= b) {
				if(dbg) printf("%d ", ps[r1]);
				t2++;
			}
		}
		printf("Case #%d: %d\n", cs, t2);
	}
	return 0;
}
