#include <bits/stdc++.h>
using namespace std;
#define ii pair<int, int>
#define vi vector<int>
#define vii vector<ii, ii>
#define vvi vector<vi>
#define MAX 1000000
#define MAXN 200005
#define MAXE 100005
#define INF 10000000
#define MOD 1000000007
#define FOR(x,n) for(int x = 0; x < n; x++)
#define FOR1e(x,n) for(int x = 1; x <= n; x++)

char palavra[1000];

long long need[105];

int main() {
	int t, k, c, s, n;
	scanf("%d", &t);

	FOR1e(caso, t) {
		scanf("%d %d %d", &k, &c, &s);
		printf("Case #%d:", caso);
		
		for(int i = 0; i <= k; i++) need[i] = k-i;
		n = k;

		long long ult;
		while(n > 1 && c > 1) {
			//4 3 2 1
			n--;
			ult = need[n];
			c--;
			for(int i = 0; i < n; i++) {
				need[i] = (ult-1LL)*k + (k-i);
			}
		}

		if(n > s) printf(" IMPOSSIBLE\n");
		else {
			for(int i = 0; i < n; i++) printf(" %lld", need[i]);
			printf("\n");
		}
	}
}



		/*string go = "";

		for(int i = 0; i < min(25, (int)tmp.size()); i++) {
			if(tmp[i] == 'L') {
				printf("LLLG "); 
				go += "LLLG";
			}
			else {
				printf("GGGG ");
				go += "GGGG";
			}
		}
		tmp = go;
		printf("\n");

		go = "";
		for(int i = 0; i < min(25, (int)tmp2.size()); i++) {
			if(tmp2[i] == 'L') {
				printf("LLGL "); 
				go += "LLGL";
			}
			else {
				printf("GGGG ");
				go += "GGGG";
			}
		}
		tmp2 = go;
		printf("\n");

		go = "";
		for(int i = 0; i < min(25, (int)tmp3.size()); i++) {
			if(tmp3[i] == 'L') {
				printf("LGLL "); 
				go += "LGLL";
			}
			else {
				printf("GGGG ");
				go += "GGGG";
			}
		}
		tmp3 = go;
		printf("\n");

		go = "";
		for(int i = 0; i < min(25, (int)tmp4.size()); i++) {
			if(tmp4[i] == 'L') {
				printf("GLLL "); 
				go += "GLLL";
			}
			else {
				printf("GGGG ");
				go += "GGGG";
			}
		}
		tmp4 = go;
		printf("\n");
// GGGGGGGG
		//GGGGG

		//LLL
		//LLLLLLLLL

		//LLG
		//LLGLLGGGG

		//LGL
		//LGLGGGLGL

		//LGG
		//LGGGGGGGG

		//GLL
		//GGGGLLGLL

		//GLG
		//GGGGLGGGG

		//GGL
		//GGGGGGGGL

		//GGG
		//GGGGGGGGG*/