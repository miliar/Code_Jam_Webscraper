#include <bits/stdc++.h>
using namespace std;
#define PI 2*acos(0.0)
#define INF 1e8
#define EPSILON 1e-8
#ifdef DEBUG
#define DPRINTF(x) printf x
#else
#define DPRINTF(x) ;
#endif

typedef pair<int, int> pii;
typedef pair<int, pair<int, int> > piii;
typedef vector<int> vi;
typedef vector<pii> vpii;
typedef vector<bool> vb;
typedef vector<string> vs;

int testNum;
int main () {
	scanf("%d", &testNum);
	for (int tn=1; tn<=testNum; ++tn) { 
		long long n;
		int chk = 0;
		scanf("%lld", &n);
		if (n == 0)
			printf("Case #%d: INSOMNIA\n", tn);

		for (int i=1; i<=100; ++i) {
			long long t = n*i;
			while (t) {
				chk |= 1<<(t%10);
				t/=10;
			}
			if (chk == (1<<10)-1) {
				printf("Case #%d: %lld\n",tn, n*i);
				break;
			}
		}
	}
	return 0;
}


