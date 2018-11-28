#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long LL;
typedef vector < int > vi;
typedef pair < int, int > pii;
typedef vector < pii > vii;

#define REP(i, a) for (int i = 0; i < (int)(a); i++)
#define FOR(i, a, b) for (int i = (int)(a); i <= (int)(b); i++)
#define REPD(i, a) for (int i = (int)(a - 1); i >= 0; i--)
#define FORD(i, a, b) for (int i = (int)(a); i >= (int)(b); i--)
#define mp make_pair
#define pb push_back
#define F first
#define S second
#define CLEAR(x, val) memset(x, val, sizeof(x))

int T, smax;
int shyness[1005];
char temp;

int main () {
	cin >> T;
	
	FOR(tc, 1, T) {
		scanf("%d ", &smax);
		
		FOR(i, 0, smax) {
			cin >> temp;
			shyness[i] = temp - '0';
		}
		
		int curr = 0, ans = 0, additional;
		FOR(i, 0, smax) {
			if (curr >= i) {
				curr += shyness[i];
			}
			else if (shyness[i] > 0) {
				additional = i - curr;
				ans += additional;
				curr += additional;
				curr += shyness[i];
			} 
		}
		
		printf("Case #%d: %d\n", tc, ans);
	}
}
