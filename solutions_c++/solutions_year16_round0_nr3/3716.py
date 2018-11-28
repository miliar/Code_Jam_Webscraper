#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <cstring>
using namespace std;
typedef long long ll;

ll expon[11][35];
int N, J;

//	normal n
inline ll in_base(int b, const int* n) {

	ll ret = 0;
	for (int i = 0; i < N; i++)
		ret += expon[b][i] * n[i];
	return ret;
}

inline ll get_divisor(int base, const int* n) {

	ll n_in_base = in_base(base, n);

	ll root = static_cast<ll>(sqrt(n_in_base));

	for (ll i = 2ll; i <= root; i++) 
		if (n_in_base % i == 0)
			return i;
	
	return 0ll;
}

//	 normal n
inline void get_next(int* n) {

	for (int i = 1; i < N-1; i++) {
		if (n[i] == 0) {
			n[i] = 1;
			return;
		}
		n[i] = 0;
	}
}

int main() {

	for (int i = 0; i <= 10; i++)
		expon[i][0] = 1;

	for (int i = 2; i <= 10; i++)
		for (int j = 1; j <= 32; j++)
			expon[i][j] = expon[i][j-1] * i;

	freopen("C-small-attempt1.in", "r", stdin);
	freopen("sol.out", "w", stdout);

	int T; cin >> T;
	for (int test = 1; test <= T; test++) {
		
		cin >> N >> J;
		printf("Case #%d:\n", test);
		
		//	create n
		int n[32]; 
		memset(n, 0, sizeof(n));
		n[0] = 1; n[N-1] = 1;



		for (int j_row = 1; j_row <= J; j_row++) {
			
			bool flag = false;
			while (!flag) {
				
				flag = true;

				ll divisor[12];
				for (int b = 2; b <= 10; b++) {
					divisor[b] = get_divisor(b, n);
					if (divisor[b] == 0) {
						flag = false;
						break;
					}
				}

				if (flag) {			
					for (int i = N-1; i >= 0; i--)
						printf("%d", n[i]);
					printf(" ");

					for (int i = 2; i < 10; i++)
						printf("%lld ", divisor[i]);
					printf("%lld\n", divisor[10]);
				}
				get_next(n);
			}
		}
	}

}