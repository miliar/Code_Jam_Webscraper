#include <stdio.h>
#include <math.h>
#include <vector>

using namespace std;

typedef long long int lld;
typedef pair<bool, lld> PBI;

int N, J;
int printed = 0;


PBI is_prime2(lld num) {
	if (num == 1) return make_pair(false, 1);
	for (lld i=2; i<=sqrt(num); i++)
		if (num % i == 0) return make_pair(false, i);
	return make_pair(true, -1);
}

lld to_decimal(lld bit, int base) {
	lld ret = 0;
	for (int k=0; k<N; k++) {
		if (bit & (1 << k))
			ret += pow(base, k);
	}
	return ret;
}

void check(long long num) {
	lld tmp;
	vector<lld> result;
	
	if (printed >= J)
		return;
	
	for (int b=2; b<=10; b++) {
		tmp = to_decimal(num, b);
		PBI pp = is_prime2(tmp);
		
		if (pp.first == true)
			break;
		else
			result.push_back( pp.second );
	}
	
	if (result.size() == 9) {
		printed++;
		
		printf("%lld ", to_decimal(num, 10));
		
		for (int i=0; i<result.size(); i++)
			printf("%lld ", result[i]);
		printf("\n");
	}
}

void run() {
	scanf("%d %d", &N, &J);
	
	printed = 0;
	lld num = 1 << (N-1);
	
	while (true) {
		if (!(num & 1)) num++;
		
		check(num);
		if (++num >= (1 << N) || printed >= J)
			break;
	}
}

int main() {
	int testCase;
	scanf("%d", &testCase);
	
	for (int t=1; t<=testCase; t++) {
		printf("Case #%d:\n", t);
		run();
	}
}
