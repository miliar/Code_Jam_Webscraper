#ifdef _MSC_VER
#define _CRT_SECURE_NO_WARNINGS
#endif

#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <stack>
#include <vector>
#include <string>
#include <queue>
#include <map>
#include <math.h>
#include <time.h>

using namespace std;

/*
double C(unsigned n, unsigned k)
{
if (k > n) return 0;
if (k * 2 > n) k = n - k;
if (k == 0) return 1;

int result = n;
for (int i = 2; i <= k; ++i) {
result *= (n - i + 1);
result /= i;
}
return (double) result;
}

double binomial(int n, int a, int b, double p) {
double prob = 0;
for (; a <= b; a++) {
prob += (C(n, a) * pow(p, a) * pow((1.0 - p), n - a));
}

printf("%lf\n%lf", prob, 1.0 - prob);
return prob;
}

int main() {
COMMENT BEGIN
int n = 5;
int a = 0;
int b = 3;
double p = 0.4;
COMMENT END

int N = 20;
int n = 5;
//int k = 3;
int a = 2;
int b = 2;

double prob = 0;
for (; a <= b; a++) {
//prob += (C(k, a) * C(N - k, n - a)) / C(N, n);
}

//printf("%lf\n%lf\n\n", prob, 1.0 - prob);

//binomial(4, 3, 3, 0.384);

float m = 40;
float d = 6;

float k = 34.5;
float k2 = 46.5;
float z = (k - m) / d;
float z2 = (k2 - m) / d;

printf("%f %f", z, z2);

}
//*/

//*
long long n, m;

bool seen[10];

int main() {
	long long w;

	scanf("%lld", &w);

//	freopen ("in.txt", "w", stdout);
	freopen ("out.txt", "w", stdout);

	long long cas = 1;
	while (cas <= w) {
		scanf("%lld", &n);

		if (n == 0) {
			printf("Case #%lld: INSOMNIA\n", cas);
			cas++;
			continue;
		}

		long long N = n;
		while (true) {
			long long aux = n;

			long long x = 1;
			while (aux > 0) {
				seen[aux % 10] = true;
				aux /= 10;
			}

			bool correct = true;
			for (long long i = 0; i < 10; i++) {
				if (!seen[i]) {
					correct = false;
					break;
				}
			}

			if (correct) {
				break;
			}

			n += N;
		}

		printf("Case #%lld: %lld\n", cas, n);
		cas++;

		for (long long i = 0; i < 10; i++) {
			seen[i] = false;
		}
	}
}
//*/

/*
3 3
1 7 4
5 2 6
3 8 9

3 3
3 3 3
3 3 3
3 3 3

4 3
4 4 4
2 2 2
3 3 3
2 2 2
*/