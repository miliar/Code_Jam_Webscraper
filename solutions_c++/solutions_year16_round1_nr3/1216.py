#include <cstdlib>
#include <vector>
#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>
#include <queue>
#include <stack>

using namespace std;

int main(int argc, char** argv) {
	int Tmax;
	scanf("%d", &Tmax);
	for (int T=1; T<=Tmax; T++) {
		int N;
		cin >> N;
		vector<int> F(N);
		for (int i=0; i<N; i++) {
			int tmp;
			cin >> tmp;
			F[i] = tmp-1;
		}
		vector<int> p(N);
		for (int i=0; i<N; i++) {
			p[i] = i;
		}
		vector<int> best;
		//int max = 0;
		for (int size=N; size>=2; size--) {
			do {
				//int curr = 0;
				for (int i=1; i<size-1; i++) {
					if (!(p[i-1] == F[p[i]] || p[i+1] == F[p[i]])) {
						//curr++;
						goto nope;
					}
					//printf("(%d %d %d,%d) ", i, F[p[i]], p[i-1], p[i+1]);
				}
				if (!(p[size-1] == F[p[0]] || p[1] == F[p[0]])) {
					//curr++;
					goto nope;
				}
				//printf("(%d %d %d,%d) ", 0, F[0], p[size-1], p[1]);
				if (!(p[size-2] == F[p[size-1]] || p[0] == F[p[size-1]])) {
					//curr++;
					goto nope;
				}
				//printf("(%d %d %d,%d) ", size-1, F[size-1], p[size-2], p[0]);
				printf("Case #%d: %d\n", T, size);
				//for (int i=0; i<size; i++) cout << p[i]+1; cout << "\n";
				//for (int i=0; i<size; i++) cout << F[p[i]]+1; cout << "\n";
				//for (int i=0; i<size; i++) cout << F[i]+1; cout << "\n";
				goto done;
				nope:;
				//if (curr > max) {
				//	max=curr;
				//	best = p;
				//}
			} while(next_permutation(p.begin(), p.end()));
		}
		printf("Case #%d: %d\n", T, 1);
		done:;
		//printf("Case #%d: %d\n", T, max);
		//for (int i=0; i<N; i++) cout << best[i]+1; cout << "\n";
	}
	
	return 0;
}

