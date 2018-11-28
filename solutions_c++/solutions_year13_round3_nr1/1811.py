#include <stdio.h>
#include <string.h>
#include <string>
#include <queue>
#include <algorithm>
#include <math.h>
#include <vector>
#include <utility>
#include <map>
#include <stack>

#define fi first
#define se second
#define mp make_pair
#define ll long long
#define pii pair <int, int>
#define vi vector <int>
#define REP(a,b) for(int a = 0; a < b; ++a)
#define FORU(a,b,c) for(int a = b; a <= c; ++a)
#define FORD(a,b,c) for(int a = b; a >= c; --a)
#define MOD 1000000000
#define MODLL 1000007LL
#define INF 2123123123
#define pb push_back
using namespace std;

char st[1000005];
bool flag[1000005];

bool isVowel(char ch) {
	return ((ch == 'a') || (ch == 'i') || (ch == 'u') || (ch == 'e') || (ch == 'o'));
}

int main() {
	int k, T;	
	
	scanf("%d", &T);
	
	FORU(tc, 1, T) {
		scanf("%s %d", st, &k);
		
		int len = strlen(st);
		vi ans;
		
		REP(i, len - k + 1) {
			flag[i] = true;
			
			REP(j, k) {
				if (isVowel(st[i+j])) {
					flag[i] = false;
					break;
				}
			}
			
			if (flag[i])
				ans.pb(i);
		}
		
		int sz = ans.size();
		
		int answer = 0;
		
		// REP(i, sz) {
			// int belakang = (i == (sz - 1)) ? (len - 1) : (ans[i + 1] + k - 2);
			// int depan = (i == 0) ? 0 : ans[i - 1];
			
			// answer += (ans[i] - depan + 1) + ((len - 1) - (ans[i] + k - 1));
			
			// printf("cek %d %d %d\n", answer, (ans[i] - depan + 1), ((len - 1) - (ans[i] + k - 1) ));
		// }
		
		int posisi = 0;
		
		REP(i, len) {
			while ((posisi < sz) && (ans[posisi] < i))
				++posisi;
			
			if (posisi == sz)
				break;
			
			int belakang = ans[posisi] + k - 1;
			answer += len - belakang;
		}
		
		printf("Case #%d: %d\n", tc,  answer);
	}
	
	return 0;
}
