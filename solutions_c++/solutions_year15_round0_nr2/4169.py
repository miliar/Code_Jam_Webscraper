#include <bits/stdc++.h>
using namespace std;

int orang[1005];

int go(int pos){
	if(pos == 0)
		return 0;
	if(orang[pos] == 0)
		return go(pos-1);
	int ret = pos;
	int temp;
	for(int i = 1; i < pos; i++){
		temp = orang[pos];
		orang[pos-i]+=temp;
		orang[i]+=temp;
		orang[pos] = 0;
		ret = min(ret,go(pos-1)+temp);
		orang[pos-i]-=temp;
		orang[i]-=temp;
		orang[pos]=temp;
	}
	return ret;
}

int main(){
	int tc, n, temp, maks;

	scanf("%d", &tc);
	for(int cc = 1; cc <= tc; cc++){
		memset(orang, 0, sizeof(orang));
		maks = 0;
		scanf("%d", &n);
		for(int i = 0; i < n; i++){
			scanf("%d", &temp);
			orang[temp]++;
			maks=max(maks,temp);
		}
		printf("Case #%d: %d\n", cc, go(maks));
	}
}
/*
INPUT:
1
10
6 6 6 6 6 6 6 6 6 16

EXPECTED:
Case #1: 8

*/