#include<iostream>
#include<sstream>
#include<cstdio>
#include<cstring>
#include<string>
#include<cstdlib>
#include<cmath>
#include<cctype>
#include<ctime>
#include<algorithm>
#include<iomanip>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<cassert>
#include<bitset>

using namespace std;

int main() {
	int TT;
	scanf("%d", &TT);
	for(int cc = 1; cc <= TT; cc++){
		int k, c, s;
		scanf("%d%d%d", &k, &c, &s);
		printf("Case #%d:", cc);
		for(int i = 1; i <= s; i++){
			printf(" %d", i);
		}
		printf("\n");
	}
	return 0;
}

