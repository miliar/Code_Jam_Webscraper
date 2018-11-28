#include <iostream>
#include <iomanip>
#include <stdio.h>
#include <cstdlib>
#include <algorithm>

#ifdef _WIN32
#define LL "%I64d"
#else
#define LL "%lld"
#endif

#define inp(x) scanf("%d",&x)
#define inpf(x) scanf("%f",&x)

using namespace std;

typedef long long int ll;
typedef long long unsigned int ull;

int main() {
	int T;
	int N,X;
	int S[10000];
	int pairs,j;

	cin >> T;

	for (int t = 1; t <= T; t++) {
		cin >> N >> X;

		for (int i = 0; i < N; i++) {
			cin >> S[i];
		}

		sort(S, S + N);

		pairs = 0;
		j = N - 1;
		for (int i = 0; i < j; i++) {
			if (S[N - 1 - i] + S[N - 1 - j] <= X) {
				pairs++;
				j--;
			}
		}
		
		cout << "Case #" << t << ": " << (N - pairs) << endl;
	}

	return 0;
}
