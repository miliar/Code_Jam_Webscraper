#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <cstring>

using namespace std;

int reverse(int x) {
	int ans = 0;
	while (x) {
		ans = ans * 10 + x % 10;
		x /= 10;
	}
	return ans;
}

int main() {
	FILE *in = fopen("1.in", "r"), *out = fopen("1.out", "w");
	int T, cnt = 0;
	fscanf(in, "%d", &T);
	
	while (T--) {
		int res = 0, N;
		fscanf(in, "%d", &N);
		
		int *times = new int[N + 1];
		for (int i = 0; i <= N; i++)
			times[i] = N + 1;
		
		for (int i = 1; i <= N; i++) {
			
			if (times[i] > i || times[i] > times[i-1] + 1)
				times[i] = min(i, times[i-1] + 1);
			
			int rev = reverse(i);
			if (rev > N) continue;
			if (times[rev] > times[i] + 1 || times[rev] > rev)
				times[rev] = min(times[i] + 1, rev);
		}
		
		fprintf(out, "Case #%d: %d\n", ++cnt, times[N]);
		delete[] times;
	}
	fclose(in);
	fclose(out);
}
