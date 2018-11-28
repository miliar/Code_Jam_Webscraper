/*
 * ProbC.cpp
 *
 *  Created on: 13-Apr-2013
 *      Author: nataraj
 */




#include <cmath>
#include <cstdio>
#include <cstring>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int T,prob;
int A,B;

int inp[]={1,4,9,121,484};
void solve(){

	int cnt=0;
	for(int i=0;i<5;++i){
		if(inp[i]>=A && inp[i]<=B)
			++cnt;
	}
	printf("Case #%d: %d\n", prob++, cnt);

}

int main(int argc, char **argv) {
	scanf("%d",&T);prob=1;
	while(T--){
		scanf("%d%d",&A,&B);
		solve();
//		printf("Case #%d: %s\n", prob++, solve());
	}

	return 0;
}
