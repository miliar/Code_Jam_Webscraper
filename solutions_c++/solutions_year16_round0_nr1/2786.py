#include <cstdlib>
#include <vector>
#include <cstdio>

using namespace std;

int main(int argc, char** argv) {
	int Tmax;
	scanf("%d", &Tmax);
	for (int T=1; T<=Tmax; T++) {
		long N;
		scanf("%d", &N);
		vector<char> seen(10,0);
		for (int i=N;; i+=N) {
			if (N == 0) {
				printf("Case #%d: INSOMNIA\n", T);
				break;
			}
			long d = 1;
			long n = i/d;
			while (n) {
				seen[n%10] = 1;
				d*=10;
				n = i/d;
			}
			bool done = true;
			for (int j=0; j<10; j++) {
				if (seen[j] == 0) {
					//printf("  ");
					done = false;
					//break;
				} else {
					//printf("%d ", j);
				}
			}
			//printf("\n");
			if (done) {
				printf("Case #%d: %d\n", T, i);
				break;
			}
		}
	}
	
	return 0;
}

