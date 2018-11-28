//============================================================================
// Name        : GCJB.cpp
// Author      : Hossam El-Deen, Waleed, Bassem
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <cstdio>
#include <utility>
#include <vector>
using namespace std;

#define mp make_pair
#define pii pair<int, int>

int T, N, M, arr[109][109];
bool V, H, D;

int main() {
	freopen("B-large.in", "rt", stdin); // change in.txt to ur input file name, doesn't have to end with .txt
	freopen("B-large.out", "wt", stdout); // same for out.txt
	scanf("%d", &T);
	for (int i = 0; i < T; ++i) {
		vector<pii > v[109];
		D = 0;
		printf("Case #%d: ", i + 1);
		scanf("%d%d", &N, &M);
		for (int i = 0; i < N; ++i)
			for (int j = 0; j < M; ++j) {
				scanf("%d", &arr[i][j]);
				v[arr[i][j]].push_back(mp(i, j));
			}
		//End of input wel7ewarat dy :D

		for (int q = 0; q < 109; ++q) {
			for (unsigned int w = 0; w < v[q].size(); ++w) {
				if (arr[v[q][w].first][v[q][w].second] == -1)
					continue;
				H = 1;	V = 1;
				for (int i = 0; i < M; ++i)
					if (arr[v[q][w].first][i] > q) {
						H = 0;
						break;
					}
				for (int i = 0; i < N; ++i)
					if (arr[i][v[q][w].second] > q) {
						V = 0;
						break;
					}
				D = (!H && !V);
				if (D) {
					printf("NO\n");
					break;
				}
				if (H)
					for (int i = 0; i < M; ++i)
						arr[v[q][w].first][i] = -1;
				if (V)
					for (int i = 0; i < N; ++i)
						arr[i][v[q][w].second] = -1;
			}
			if (D)
				break;
		}
		if (D)
			continue;
		printf("YES\n");
	}
	return 0;
}
