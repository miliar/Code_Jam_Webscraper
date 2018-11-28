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

int cnt = 0,  have[100];

void cal(long long x){
	if(!x)return;
	if(have[x % 10] == 0){
		cnt++;
	  have[x % 10] = 1;
	}
	cal(x / 10);
}

int main() {
	int TT;
	scanf("%d", &TT);
	for(int cc = 1; cc <= TT; ++cc){
		int x = 0;
		scanf("%d", &x);
		//int tmp = x;
		//while(tmp > 0 && tmp % 10 == 0)tmp/=10;
		if(x == 0){
			printf("Case #%d: INSOMNIA\n", cc);
			continue;
		}
		cnt = 0;
		memset(have, 0, sizeof(have));
		int j = 1;
		for(;;j++){
			cal(j * x);
			if(cnt == 10){
		    printf("Case #%d: %d\n", cc, j * x);
				break;
			}
		}
	}
	return 0;
}

