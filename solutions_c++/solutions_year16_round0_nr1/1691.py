#include <iostream>
#include <cstring>
#include <cstdlib>
using namespace std;

int main() {
	freopen("A-large.in","r",stdin);
	freopen("q1.out", "w",stdout);
	int TT;
	cin>>TT;
	for (int T=1; T<=TT; ++T) {
		int n, dig=0;
		bool f[20];
		memset(f, 0, sizeof(f));
		cin>>n;
		for (int i=1; i<10000; ++i) {
			int k=n*i;
			while (k>0) {
				if (!f[k%10]) {
					f[k%10]=1;
					++dig;
				}
				k/=10;
			}
			if (dig==10) {
				printf("Case #%d: %d\n", T, i*n);
				break;
			}
		}
		if (dig<10)
			printf("Case #%d: INSOMNIA\n", T);
		}
}
