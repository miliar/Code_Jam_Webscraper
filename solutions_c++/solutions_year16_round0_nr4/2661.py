#include "bits/stdc++.h"
using namespace std;
typedef unsigned long long llu;
int main() {
	freopen("", "r", stdin);
	FILE *fp = fopen("output.txt", "w");
	int Case;
	cin >> Case;
	for (int tc = 1; tc <= Case; tc++) {
		int K, C, S;
		cin >> K >> C >> S;
		fprintf(fp,"Case #%d:", tc);
		for (int i = 1; i <= K; i++)
			fprintf(fp," %d", i);
		fprintf(fp,"\n");
	}
	return 0;
}