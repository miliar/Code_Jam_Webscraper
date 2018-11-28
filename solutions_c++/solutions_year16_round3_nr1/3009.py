#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
/*
#include "../threadpool/thread_pool.tpp"
using namespace thread_pool;

*/

using namespace std;


struct letter {
	char l;
	int n;
};

void bubble(vector<letter> &P, int idx) {
	for (; idx < P.size() - 1; ++idx) {
		if(P[idx].n < P[idx + 1].n)
			swap(P[idx], P[idx + 1]);
		else break;
	}
}

bool comp (letter &i,letter &j) { return (i.n > j.n); }

int main(int argc, char const *argv[])
{
	int T, N;
	scanf("%d", &T);
	
	for (int i = 0; i < T; ++i) {
		scanf("%d", &N);
		printf("Case #%d:", i+1);
		vector<letter> P(N);

		for (int j = 0; j < N; ++j) {
			int p;
			scanf("%d", &p);
			P[j] = {'A' + j, p};
		}

		sort(P.begin(), P.end(), comp);

		while(P[0].n > 0) {
			if (P[1].n + P[0].n == 1) {
					printf(" %c", P[0].l);
					break;
			}
			else if (P[2].n + P[1].n + P[0].n == 2) {
					printf(" %c%c", P[0].l, P[1].l);
					break;
			}
			else if (P[2].n + P[1].n + P[0].n == 3) {
				printf(" %c", P[0].l);
				if (P[2].n >  0)
					printf(" %c%c", P[1].l, P[2].l);
				else {
					printf(" %c%c", P[0].l, P[1].l);
				}
					break;
			}
			else {
				int diff = P[0].n - P[1].n;
				if (diff > 1) {
					P[0].n -= 2;
					printf(" %c%c", P[0].l, P[0].l);
					bubble(P, 0);
				}
				else {
					P[0].n -= 1;
					P[1].n -= 1;
					printf(" %c%c", P[0].l, P[1].l);
					bubble(P, 1);
					bubble(P, 0);
				}
			}
		}
		
		printf("\n");
	}
}