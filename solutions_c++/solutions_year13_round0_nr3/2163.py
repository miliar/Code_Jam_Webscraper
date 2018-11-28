#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <map>
#include <queue>

#define LL long long int
#define FOR(i, s, e) for (int i=(s);i<(e);i++)
#define FOE(i, s, e) for (int i=(s);i<=(e);i++)
#define FOD(i, s, e) for (int i=(e)-1;i>=(s);i--)
#define CLR(x, a) memset(x, a, sizeof(x))
#define MAX 100000000000000LL
using namespace std;

int testcase, cnt;
LL pw[20], a, b, ret[100000];

int Palin(LL x){
	int dig[20], len = 0;
	while (x){
		dig[len++] = x % 10;
		x /= 10;
	}
	FOR(i, 0, len / 2) if (dig[i] != dig[len - i - 1]) return 0;
	return 1;
}

void Exhaust(LL x, int len){
	//printf("%I64d, %d\n", x, len);
	if (x * x > MAX || len >= 8) return;
	if (Palin(x * x)) ret[cnt++] = x * x;
	FOR(i, 0, 10)
		if (!(x==0 && i==0))
			Exhaust(i * pw[len + 1] + x * 10 + i, len + 2);
}

int main(){
	
	pw[0] = 1;
	FOR(i, 1, 15) pw[i] = pw[i - 1] * 10;
	cnt = 0;
	
	Exhaust(0, 0);
	FOR(i, 0, 10){
		Exhaust(i, 1);
		if (i) Exhaust(i * 10 + i, 2);
	}
	
	sort(ret, ret + cnt);
	cnt = unique(ret, ret + cnt) - ret;
	//FOR(i, 0, cnt)
		//cout << ret[i] << endl;
	
	scanf("%d", &testcase);
	FOR(TC, 0, testcase){
		cin >> a >> b;
		int ans = upper_bound(ret, ret + cnt, b) - lower_bound(ret, ret + cnt, a);
		printf("Case #%d: %d\n", TC + 1, ans);
	}
	return 0;
}
