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
	int T;
	scanf("%d", &T);
	for(int cc = 1; cc <= T; cc++){
		int n, l;
		scanf("%d%d", &n, &l);
		char s[1000];
		int ok = 1;
		for(int i = 0; i < n; ++i){
			scanf("%s", s);
			int tmp = 0, ll = strlen(s);
			for(int j = 0; j < ll; j++){
				if(s[j] == '0') tmp = 1;
			}
			if(tmp == 0) ok  = 0;
		}
		scanf("%s", s);
		if(ok == 0){
			printf("Case #%d: IMPOSSIBLE\n", cc);
			continue;
		}
		if(l == 1) printf("Case #%d: ? 0\n", cc);
		else {
			printf("Case #%d: ", cc);
			for(int i = 0; i < l - 1; ++i){
				printf("?");
			}
			printf(" ");
			printf("10?");
			for(int i = 0; i < l; ++i){
				printf("10");
			}
			printf("\n");
		}
	}
	return 0;
}

