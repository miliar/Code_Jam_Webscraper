#include<cstdio>
using namespace std;

int pow_equals(int x) {
	int two = 1, i = 0;
	while(two < x) {
		two *= 2;
		i++;
	}
	if(two == x) return i;
	return -1;
}

int main() {
	FILE *in = fopen("input.in", "r");
	FILE *out = fopen("output.out", "w");
	int t, it, res, p, q, ans;
	fscanf(in, "%d", &t);
	for(it = 1; it <= t; it++) {
		fscanf(in, "%d/%d", &p, &q);
		res = pow_equals(q);

		if(res == -1) {
			fprintf(out, "Case #%d: impossible\n", it);
		} else {
			// e putere a lui 2
			ans = 0;
			while(p / q < 1) {
				ans++;
				p *= 2;
			}
			fprintf(out, "Case #%d: %d\n", it, ans);
		}
	}
	return 0;
}

