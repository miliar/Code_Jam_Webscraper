//============================================================================
// Name        : GCJ-1B-A.cpp
// Author      : Hossam El-Deen, Amgad, Amgad, Bassem, Hatem, Hassan
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <map>
using namespace std;

int A, N, arr[109], mn;

void DFS(int x, int a, int ctr) {
	if (x == N) {
		mn = min(mn, ctr);
		return;
	}
	if (arr[x] < a)
		DFS(x + 1, a + arr[x], ctr);
	else {
		DFS(x + 1, a, ctr + 1);
		if (a != 1)
			DFS(x, a + a - 1, ctr + 1);
	}
}

int main() {
	freopen("A-small-attempt0.in", "rt", stdin); // change in.txt to ur input file name, doesn't have to end with .txt
	freopen("A-small-attempt0.out", "wt", stdout); // same for out.txt
	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; ++i) {
		printf("Case #%d: ", i + 1);
		scanf("%d%d", &A, &N);
		for (int i = 0; i < N; ++i)
			scanf("%d", &arr[i]);
		sort(arr, arr + N);
		mn = 1e9;
		DFS(0, A, 0);
		printf("%d\n", mn);
		cout << flush;
	}
	return 0;
}
