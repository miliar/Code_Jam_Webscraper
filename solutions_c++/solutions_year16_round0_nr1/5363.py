#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#include <stdio.h>
#include <vector>
#include <string>
#include <memory.h>
using namespace std;

typedef long long ll;
const int N = 1e6 + 5;
int res[N];
int bits[N * 10];
int get(int v){
	if (v >= N * 10){
		puts("!!");
	}
	if (bits[v] != -1)
		return bits[v];
	int msk = 0;
	while (v){
		msk |= 1 << (v % 10);
		v /= 10;
	}
	return bits[v] = msk;
}
int main(){
	freopen("AinL.txt", "r", stdin);
	freopen("AoutL.txt", "w", stdout);
	memset(bits, -1, sizeof(bits));
	for (int i = 1; i <= 1000000; ++i){
		int cur = i;
		int msk = get(i);
		while (msk + 1 != (1 << 10)){
			cur += i;
			msk |= get(cur);
		}
		res[i] = cur;
	}
	int T;
	cin >> T;
	for (int k = 1; k <= T; ++k){
		int n;
		cin >> n;
		if (!n)
			printf("Case #%d: INSOMNIA\n", k);
		else printf("Case #%d: %d\n", k, res[n]);
	}
}