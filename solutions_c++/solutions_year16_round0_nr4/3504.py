#include <cstdio>
#include <cstring>
#include <cassert>
#include <vector>
#include <algorithm>
using namespace std;
const int MAX_BUFF = 1000;

int testCases, K, C, S;
char buff[MAX_BUFF];

int main() {
	sscanf(gets(buff), "%d", &testCases);
	for(int t = 1; t <= testCases; t++) {
		sscanf(gets(buff), "%d %d %d", &K, &C, &S);		
		
		vector<unsigned long long> columns, next_column, r, nr;		
		unsigned long long uK = K;
		columns.resize(K);
		for(int i = 0; i < K; i++) {
			columns[i] = i+1;
			r.push_back(K - i - 1);
		}
		
		for(int c = 1; c < C; c++) {
			if(columns.size() == 1) break;
			for(int i = 0; i < columns.size(); i++) {
				if(nr.size() > 0 && r[i] == nr.back()) continue;
				if(nr.size() > 0 && nr.back() == 1) {
					next_column.push_back(next_column.back()+1);
					nr.push_back(0);											
					break;
				}
				next_column.push_back((uK * (columns[i] - 1)) + (columns[i]%K + 1));
				nr.push_back(r[i] == 0 ? 0 : r[i] - 1);
				//printf(" %llu(%d)", next_column.back(), nr.back());							
			}
			if(nr.size() > 0 && nr.back() == 1) {
				next_column.push_back(next_column.back()+1);
				nr.push_back(0);
				//printf(" %llu(%d)", next_column.back(), nr.back());							
			}
			//printf("\n");
			next_column.swap(columns);
			nr.swap(r);
			nr.clear();
			next_column.clear();
		}
		if(S >= columns.size()) {
			printf("Case #%d:", t);
			for(int i = 0; i < columns.size(); i++) {
				printf(" %llu", columns[i]);
			}
			printf("\n");	
		} else {
			printf("Case #%d: IMPOSSIBLE\n", t);
		}
	}
	return 0;
}