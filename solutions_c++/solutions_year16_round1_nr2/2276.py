#include <cstdio>
#include <iostream>
#include <string>
#include <queue>
#include <cmath>
#include <vector>
#include <algorithm>
#include <unordered_map>
using namespace std;

void sol(vector<vector<int> > &d, int N) {
	int i, j;
	unordered_map<int, int> m;
	for (i = 0; i < 2*N - 1; i++) {
		for (j = 0; j < N; j++) {
			m[d[i][j]]++;
		}
		
	}
	vector<int> r;
	for (auto e : m) {
		if (e.second % 2) {
			r.push_back(e.first);
		}
	}
	sort(r.begin(), r.end());
	for (i = 0; i < N; i++) {
		printf(" %d", r[i]);
	}
	printf("\n");
}

int main() {
	int T, N;
    int i, j, k;
    scanf("%d", &T);
    // ios_base::sync_with_stdio(false);
    // cin.tie(NULL);
    for (i = 1; i <= T; i++) {
    	scanf("%d", &N);
    	vector<vector<int> > data(2*N - 1, vector<int>(N)); 
    	for (j = 0; j < 2*N - 1; j++) {
    		for (k = 0; k < N; k++) {
    			scanf("%d", &data[j][k]);
    		}
    	}
    	printf("Case #%d:", i);
    	sol(data, N);
    }
}