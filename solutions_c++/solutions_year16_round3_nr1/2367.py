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

int cnt[30];

int lef(){
	int x = 0;
	int ret = 0;
	for(int i = 0; i < 26; ++i){
		if(cnt[i] > 0) x++;
		ret += cnt[i];
	}
	if(x == 2){
		ret -= 2;
		printf(" ");
		for(int i = 0; i < 26; ++i){
			if(cnt[i] > 0){
				cnt[i]--;
				printf("%c", 'A' + i);
			}
		}
	} else {
		printf(" ");
		ret -= 1;
		int maxx = 0;
		for(int i = 1; i < 26; ++i){
			if(cnt[i] > cnt[maxx])
				maxx = i;
		}
		printf("%c", 'A' + maxx);
		cnt[maxx]--;
	}
	return ret;
}

int main() {
	int TT;
	scanf("%d", &TT);
	for(int cc = 1; cc <= TT; ++cc){
		memset(cnt, 0, sizeof(cnt));
		int n;
		scanf("%d", &n);
		for(int i = 0; i < n; ++i){
			scanf("%d", cnt + i);
		}
		printf("Case #%d:", cc);
		while(1){
			int tmp = lef();	
			if(tmp == 0)break;
		}
		printf("\n");
	}
	return 0;
}

