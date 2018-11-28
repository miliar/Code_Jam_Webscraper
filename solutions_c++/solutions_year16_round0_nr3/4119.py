#include <cstdio>
#include <vector>
#include <string.h>

FILE * in = fopen("in.txt", "r");
FILE * out = fopen("out.txt", "w");

using namespace std;

int n, m;
vector <long long> ans[17];
vector <long long> d[17][51];

void _out(long long ans) {
	if (ans == 0) return;
	else _out(ans / 2);
	fprintf(out, "%lld", ans % 2);
}

int main() {
	for (int i = 1; i <= 65536; i+=2) {
		long long count = 0, two;
		for (two = 1; ; two *= 2, count++)
			if (i / two < 2) break;

		if (ans[count].empty() || !ans[count].empty() && ans[count].size() <= 50) {
			long long t[12] = { 0 };
			vector <long long> temp;

			for (long long x = two; x > 0; x /= 2) 
				for (long long j = 2; j <= 10; j++)
					t[j] = t[j] * j + ((i / x) % 2);

			for (int j = 2; j <= 10; j++)
				for (long long x = 2; x * x <= t[j]; x ++)
					if (t[j] % x == 0) {
						temp.push_back(x);
						break;
					}

			if (temp.size() == 9) {
				ans[count].push_back(i);
				for (long long x : temp)
					d[count][ans[count].size() - 1].push_back(x);
			}
		}
	}

	scanf("%d %d %d", &n, &n, &m);

	fprintf(out, "Case #1:\n");
	for (int i = 0; i < m; i++){
		_out(ans[n - 1][i]);
		for (long long x : d[n - 1][i])
			fprintf(out, " %lld", x);
		fprintf(out, "\n");
	}

}