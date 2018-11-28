#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>
#include <unistd.h>
#include <algorithm>
#include <map>
#include <queue>
#include <stack>
#include <vector>
#include <set>
#include <string>

#define pb push_back
#define mp make_pair
#define ll long long
#define FOR(i, A, N) for(int (i) = (A); (i) < (N); (i)++)
#define REP(i, N) for(int (i) = 0; (i) < (N); (i)++)

using namespace std;
char str[111111];
int mult(int a, int b) {
	int s = 1;
	if(a < 0) { s *= -1; a *= -1; }
	if(b < 0) { s *= -1; b *= -1; }
	if(a == 1) return s*b;
	if(b == 1) return s*a;
	if(a == b) return -s;
	if(a > b) { swap(a, b); s *= -1; }
	//i==2,j==3,k==4
	if(a == 2) return b == 3 ? s*4 : -s*3; 
	
	//j*k
	return s*2;
}

int mem[11111][5][5];
int X, L;
int find(int pos, int cres, int k) {
	int& ans = mem[pos][cres][k];
	if(k == 3 && pos == L)
		return 1;
	else if(pos == L)
		return 0;
	else if(k == 3)
		return 0;
	if(ans == -1) {
		int nres = mult(cres, str[pos]-'i'+2);
		ans = find(pos+1, nres, k);
		if(k <= 2 && nres == 2+k)
			ans = max(ans, find(pos+1, 1, k+1));		
	}
	return ans;
}

int main() {
	int T;
	scanf("%d", &T);
	for(int testc = 1; testc <= T; testc++) {
		scanf("%d%d", &L, &X);
		scanf("%s", str);
		REP(i, X-1) {
			REP(j, L)
				str[j+(i+1)*L] = str[j+i*L];
		}
		str[X*L] = '\0';
		L = X*L;
		memset(mem, -1, sizeof(mem));
		bool ok = find(0, 1, 0) == 1;
		printf("Case #%d: %s\n", testc, ok ? "YES" : "NO");
	}
	return 0;
}
