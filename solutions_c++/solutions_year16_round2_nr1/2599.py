#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <climits>
#include <cctype>
#define SZ(x) ( (int) (x).size() )
#define me(x,a) memset(x,a,sizeof(x))
#define FN(a,n) for(int a=0;a<n;a++)
#define FOR(a,ini,fin) for(int a=(ini);a<(fin);a++)
#define sc1(x) scanf("%d",&x)
#define sc2(x,y) scanf("%d %d",&x,&y)
#define sc3(x,y,z) scanf("%d %d %d",&x,&y,&z)
#define all(v) v.begin(),v.end()
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define F first
#define S second
#define endl "\n"
#define MOD 1000000007
#define MAXN 1000006
typedef long long LL;
typedef long double LD;
typedef unsigned long long ULL;
using namespace std;
string s;
int f[10];
int fl[26];

string vals[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

int ord1[] = {0,2,6,8,3,4,5,7,1,9};
char ord2[] = {'Z','W','X','G','H','R','F','V','O','I'};

int purge(int dig, char de) {
	int cnt = fl[de - 'A'];
	FN (i, SZ(vals[dig])) {
		fl[vals[dig][i] - 'A'] -= cnt;
	}
	return cnt;
}


int main () {
	int tc;
	sc1(tc);
	FN (itc, tc) {
		cin >> s;
		me(f, 0);
		me(fl, 0);
		
		FN (i, SZ(s)) {
			fl[s[i] - 'A']++;
		}
		
		FN (i, 10) {
			int cnt = purge(ord1[i], ord2[i]);
			f[ord1[i]] += cnt;
		}
		
		printf("Case #%d: ", (itc + 1));
		FN (i, 10) {
			FN (j, f[i]) {
				putchar(i + '0');
			}
		}
		
		puts("");
	}
}
