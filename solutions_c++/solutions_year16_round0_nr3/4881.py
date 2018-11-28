#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <queue>
#include <numeric>
#include <array>
#include <map>
#include <set>
#include <unordered_map>
#include <functional>
#include <iostream>
#include <thread>
#include <sstream>
#include <atomic>

using namespace std;


set<vector<long long> > S;

int P[10] = {3, 5, 7, 11, 13, 17, 19, 23, 27, 29};

int main () {
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++) {
		int N, J;
		scanf("%d %d", &N, &J);
		printf("Case #1:\n");
		while (S.size()< J) {
			vector<long long> V(10);
			vector<long long> L(N);
			for (long long &x:L) x=rand()%2;
			L[0]=L[N-1]=1;
			for (int D=2; D<=10; D++) {
				long long X=0;
				for (long long &c:L) {
					X*=D;
					X+=c;
				}
				if (D==10) V[0]=X;
				int i=0;
				while (i<10 && X%P[i]) i++;
				if (i<10) V[D-1]=P[i];
				else goto ups;
				
			}
			S.insert(V);
			ups:;
		}
		for (auto &v:S) {
			for (auto &x:v) {
				printf("%lld ", x);
			}
			printf ("\n");
		}
		
	}
	return 0;
}
