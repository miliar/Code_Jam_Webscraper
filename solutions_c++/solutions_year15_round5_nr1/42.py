#include <set>
#include <map>
#include <ctime>
#include <queue>
#include <string>
#include <cstdio>
#include <vector>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>
using namespace std;
const int MAXN = 1000000 + 100;
int Test, N, D;
long long F[MAXN], G[MAXN];
long long As, Cs, Rs, S[MAXN];
long long Am, Cm, Rm, M[MAXN];
pair<long long, long long> P[MAXN];
priority_queue<long long> Heap;

int main(int argc, char **argv)
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &Test);
	for (int Case = 1; Case <= Test; Case ++) {
		scanf("%d%d", &N, &D);
		scanf("%lld%lld%lld%lld", &S[0], &As, &Cs, &Rs);
		scanf("%lld%lld%lld%lld", &M[0], &Am, &Cm, &Rm);
		F[0] = G[0] = S[0];
		P[0] = make_pair(F[0], G[0]);
		for (int i = 1; i < N; i ++) {
			S[i] = (S[i - 1] * As + Cs) % Rs;
			M[i] = (M[i - 1] * Am + Cm) % Rm;
			int k = M[i] % i;
			F[i] = min(F[k], S[i]);
			G[i] = max(G[k], S[i]);
			P[i] = make_pair(F[i], G[i]);
		}
		sort(P, P + N);
		while (Heap.empty() == false) {
			Heap.pop();
		}
		int Ret = 1;
		for (int i = N - 1; i >= 0; i --) {
			Heap.push(P[i].second);
			while (!Heap.empty() && Heap.top() > P[i].first + D) {
				Heap.pop();
			}
			if (P[i].first <= S[0] && P[i].first + D > 0) {
				Ret = max(Ret, (int)Heap.size());
			}
		}
		printf("Case #%d: %d\n", Case, Ret);
		cerr << Case <<endl;
	}
	return 0;
}