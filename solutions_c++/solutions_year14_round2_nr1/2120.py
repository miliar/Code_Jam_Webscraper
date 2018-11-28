#include <bits/stdc++.h>
#include <iomanip>

using namespace std;

#define LL long long
#define DB double
#define sf scanf
#define pf printf
#define nl printf("\n")
#define FOR(i,a,b) for(i = a; i <= b; ++i)
#define FORD(i,a,b) for(i = a; i >= b; --i)
#define FORS(i,n) for(i = 0; i < n; ++i)
#define FORM(i,n) for(i = n - 1; i >= 0; --i)
#define reset(cok,n) memset(cok, n, sizeof(cok))
#define open freopen("A-small-attempt1.in","r",stdin); freopen("A-small-attempt1.txt","w",stdout)
#define close fclose(stdin); fclose(stdout)
#define mp make_pair

const LL mod = 1e9+7;

int gcd(int a, int b) { return b? gcd(b,a%b): a; }
int lcm(int a, int b) { return a*b / gcd(a,b); }

int tip[105][105];
char kamus[105], input[105];
int ans;

int main(void)
{
	open;
	int i, j, t, n, len, k, kar;
	sf("%d", &t);
	FOR(i,1,t) {
		reset(tip, 0);
		reset(kamus, '*');
		int maks = 0;
		sf("%d", &n);
		bool cek = 0;
		FOR(j,1,n) {
			cin >> input;
			len = strlen(input);
			if(j == 1) {
				kar = 0;
				kamus[kar] = input[0];
				tip[j][kar]++;
				FOR(k,1,len-1) {
					if(input[k] == input[k-1]) tip[j][kar]++;
					else {
						kar++;
						kamus[kar] = input[k];
						tip[j][kar]++;
					}
				}
			} else {
				kar = 0;
				if(kamus[kar] != input[0]) { cek = 1; goto PRINT; }
				tip[j][kar]++;
				FOR(k,1,len-1) {
					if(input[k] == input[k-1]) tip[j][kar]++;
					else {
						kar++;
						if(kamus[kar] != input[k]) { cek = 1; goto PRINT; }
						tip[j][kar]++;
					}
				}
			}
			maks = max(maks, kar);
			
		}
		ans = 0;
		FOR(k,0,maks) {
			int sum = 0;
			FOR(j,1,n) {
				if(!tip[j][k]) { cek = 1; goto PRINT; }
				sum += tip[j][k];
			}
			int standar = round((DB)sum/n);
			FOR(j,1,n) {
				ans += abs(standar - tip[j][k]);
			}
		}
		
		PRINT:;
		pf("Case #%d: ",i);
		if(cek) puts("Fegla Won");
		else cout << ans << endl;
		
	}
	
	close;
	
	return 0;
}