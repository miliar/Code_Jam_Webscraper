#include <bits/stdc++.h>
#define iof(in, out) freopen(in, "r", stdin); freopen(out, "w", stdout);
#define f1(i, s, x) for(int i=s; i<x; i++)

int T;
long N;

std::string long2str(long n) {
	std::ostringstream ss;
	ss << n;
	return ss.str();
}

long solve(long N) {
	int r = 0, d[10] = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
	long n = N;
	if (N == 0)
		return 0;
	else {
		do {
			std::string str = long2str(n);
			for(std::string::iterator it = str.begin(); it != str.end(); ++it) {
				int g = *it - '0';
			    if (d[g] == 0) {
			    	d[g] = 1;
			    	r++;
				}
			}
			n += N;
		} while (r != 10);
		return n - N;
	}
}

int main() {
	//iof("q1.test.in.txt", "q1.test.out.txt")
	//iof("q1.small.in.txt", "q1.small.out.txt")
	iof("q1.large.in.txt", "q1.large.out.txt")
	scanf("%d", &T);
	f1(t, 0, T) {
		scanf("%d", &N);
		long R = solve(N);
		printf("Case #%d: ", t+1);
		if (R == 0)
			printf("INSOMNIA\n");
		else
			printf("%d\n", R);
	}
	return 0;
}


