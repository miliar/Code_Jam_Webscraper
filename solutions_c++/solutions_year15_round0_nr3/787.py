#include <cstdio>
#include <algorithm>
#include <string>

using namespace std;
typedef long long i64;

int T, L; i64 X;
char S[101010];

int qmuls(int a, int b)
{
	if (a == 0 || b == 0) return a + b;
	if (a == b) return 4;
	
	int ret = 6 - a - b;
	if ((a + 1) % 3 != b % 3) ret |= 4;
	return ret;
}

int qmul(int a, int b)
{
	//0: 1, 1: i, 2: j, 3: k
	//+4: minus
	return qmuls(a & 3, b & 3) ^ (a & 4) ^ (b & 4);
}

int main()
{
	scanf("%d", &T);

	for (int t = 0; t++ < T;) {
		scanf("%d%lld%s", &L, &X, S);
		if (X > 20) X = (X - 20) % 4 + 20;

		string C;
		for (int i = 0; i < (int)X; ++i) C += string(S);

		bool valid = true;
		
		int mult = 0, lip = L, rip = -1;
		L = L * (int)X;
		for (int i = 0; i < L; ++i) {
			mult = qmul(mult, C[i] - 'h');

			if (lip == L && mult == 1) lip = i;
		}
		mult = 0;
		for (int i = L - 1; i >= 0; --i) {
			mult = qmul(C[i] - 'h', mult);

			if (rip == -1 && mult == 3) rip = i;
		}

		printf("Case #%d: %s\n", t, (mult == 4 && lip < rip) ? "YES" : "NO");
	}
	return 0;
}
