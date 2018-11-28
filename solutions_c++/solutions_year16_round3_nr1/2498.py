#include "cmath"
#include "cstdio"
#include "algorithm"
#include "map"
#include "numeric"
#include "queue"
#include "set"
#include "string"
#include "utility"
#include "vector"
#include "iostream"
#include "assert.h"
using namespace std;
typedef long long i64;

string A(vector<int>& L, string str, char c, char digit)
{
	string res;
	if (L[c - 'A'] > 0) {
		int cnt = L[c - 'A'];
		res.append(cnt, digit);
		for (auto cc:str) {
			L[cc - 'A'] -= cnt;
		}
	}
	return res;
}

int main() {
	int T; scanf("%d", &T);
	for (int Ti = 1; Ti <= T; ++Ti) {
		fprintf(stderr, "Case #%d of %d...\n", Ti, T);

		int N;
		scanf("%d", &N);
		
		int sum = 0;
		vector<pair<int, int>> P;
		for (int i=0;i<N;++i) {
			int pi;
			scanf("%d", &pi);
			P.push_back(make_pair(i,pi));
			sum += pi;
		}
		
		printf("Case #%d:", Ti);

		while (true) {
			sort(P.begin(), P.end(), [](const pair<int,int>& lhs, const pair<int,int>& rhs){
				return lhs.second > rhs.second;
			});

			if (P[0].second == 0) break;
			
			assert(P[0].second * 2 <= sum);
			printf(" %c", P[0].first + 'A');
			P[0].second--;
			sum--;
			if (P[0].second <= P[1].second) {
				swap(P[0], P[1]);
			}
			if (P[0].second > 0 && sum != 2) {
				printf("%c", P[0].first + 'A');
				P[0].second--;
				sum--;
			}
		}
		printf("\n");
		
	}
	return 0;
}
