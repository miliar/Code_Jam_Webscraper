#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<climits>
using namespace std;
double c, f, x;
double ans, sm, spd;
inline void work(){
	cin >> c >> f >> x;
	ans = x / 2;
	sm = 0; spd = 2;
	for (int i = 1; 1; ++ i){
		sm += c / spd;
		spd += f;
		if (ans > sm + x / spd) ans = sm + x / spd;
		else break;
	}
	printf("%.7f\n", ans);
}
int main(){
	//freopen("in", "r", stdin);
	//freopen("out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int cases = 1; cases <= T; ++ cases){
		printf("Case #%d: ", cases);
		work();
	}
}
