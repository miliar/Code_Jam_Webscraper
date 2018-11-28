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

char s[5100];
int use[5100];
char output[5100];
int f = 0;

int main() {
	int TT;
	scanf("%d", &TT);
	for(int cc = 1; cc <= TT; ++cc){
		scanf("%s", s);
		memset(use, 0, sizeof(use));
		f = 0;
		int l = strlen(s) - 1;
		while(l >= 0){
			int x = l;
			for(int i = l; i >= 0; i--){
				if(s[i] > s[x]){
					x = i;
				}
			}
			output[f++] = s[x];
			use[x] = 1;
			l = x - 1;
		}
		l = strlen(s);
		for(int i = 0; i < l; ++i){
			if(!use[i])output[f++] = s[i];
		}
		output[l] = '\0';
		if(strlen(s) != strlen(output)){
			printf("=========%d  %d  %d=====\n", cc, strlen(s), strlen(output));
		}
		printf("Case #%d: %s\n", cc, output);
	}
	return 0;
}

