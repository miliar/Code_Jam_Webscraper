#ifdef _MSC_VER
#define _CRT_SECURE_NO_WARNINGS
#endif
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<utility>
#include<set>
#include<map>
#include<queue>
#include<vector>
#include <string>

#define RI(X) scanf("%d", &(X))
#define RII(X, Y) scanf("%d%d", &(X), &(Y))
#define RIII(X, Y, Z) scanf("%d%d%d", &(X), &(Y), &(Z))
#define DRI(X) int (X); scanf("%d", &X)
#define DRII(X, Y) int X, Y; scanf("%d%d", &X, &Y)
#define DRIII(X, Y, Z) int X, Y, Z; scanf("%d%d%d", &X, &Y, &Z)
#define println(X) printf("%d\n",(X))
#define PB push_back
#define MP make_pair
using namespace std;

int main(){
	freopen("opera.in", "r", stdin);
	freopen("opera.out", "w", stdout);
	DRI(T);
	for (int tc = 1; tc <= T; tc++){
		cout << "Case #" << tc << ": ";
		DRI(N);
		string s; cin >> s;
		int total = s[0] - '0';
		int ans = 0;
		for (int i = 1; i <= N; i++){
			int x = (int)s[i] - '0';
			ans = max(ans, i - total);
			total += x;
		}
		//cout << total << "!\n";
		cout << ans << "\n";
	}
	return 0;
}