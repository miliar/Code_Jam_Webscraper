#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

typedef long long lol;

int N, P;

vector<lol> toBinary(lol n) {
	vector<lol> bits;
	for (int i = 0; i < N; ++i) {
		bits.push_back(n % 2);
		n /= 2;
	}
	reverse(bits.begin(), bits.end());
	return bits;
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int Ti = 1; Ti <= T; Ti++)
	{
		// input
		scanf("%d %d", &N, &P);
		
		vector<lol> Pbin = toBinary(P - 1);
		//for (int i = 0; i < N; ++i) printf("%lld", Pbin[i]); printf("\n");

		int s = 0; // leading ones
		while (s < N && Pbin[s] == 1) ++s;
		//printf("s = %d\n", s);
		lol guaranteedPrize = (1LL << (s + 1)) - 2;
		if (s == N)
			guaranteedPrize /= 2;
		
		lol possiblePrize = 0LL;
		for (int i = 1; (1LL << i) <= P; ++i) {
			//printf("+ %lld\n", (1LL << (N - i)));
			possiblePrize += (1LL << (N - i));
		}

		printf("Case #%d: %lld %lld\n", Ti, guaranteedPrize, possiblePrize);
	}
	return 0;
}