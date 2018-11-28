#include <stdio.h>
#include <iostream>
#include <string>
#include <string.h>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
using namespace std;

#define FOR(I,A,B) for(int I = (A); I < (B); ++I)
#define REP(I,N)   FOR(I,0,N)
#define ALL(A)     (A).begin(), (A).end()
typedef long long ll;

int D;
const int L[10][5] = {
	{0, 0, 0, 0, 0},
	{0, 0, 0, 0, 0},
	{0, 0, 0, 0, 0},
	{0, 0, 0, 0, 0},
	{2, 0, 0, 0, 0},
	{2, 0, 0, 0, 0},
	{2, 3, 0, 0, 0},
	{2, 3, 0, 0, 0},
	{2, 3, 4, 0, 0},
	{2, 3, 4, 0, 0}
};

int solve(priority_queue<int> pq)
{
/*	priority_queue<int> pqt = pq;
	while (!pqt.empty()) {
		printf("%d ", pqt.top());
		pqt.pop();
	}
	printf(".\n");
	*/
	
	int maxt = pq.top();
	if (maxt <= 3)
		return maxt;
	pq.pop();

	int minv = 10000000;
	for (int i = 0; L[maxt][i] != 0; i++) {
		priority_queue<int> pqt = pq;
		pqt.push(L[maxt][i]);
		pqt.push(maxt-L[maxt][i]);
		minv = min(minv, solve(pqt));
	}
	
	return min(maxt, 1+minv);
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		priority_queue<int> pq;
		scanf("%d", &D);
		for (int i = 0; i < D; i++) {
			int v;
			scanf("%d", &v);
			pq.push(v);
		}
		printf("Case #%d: %d\n", t, solve(pq));
	}
	return 0;
}
