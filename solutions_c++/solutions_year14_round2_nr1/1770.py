#include <functional>
#include <algorithm>
#include <iostream>
#include <climits>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <numeric>
#include <cstring>
#include <cassert>
#include <cstdio>
#include <string>
#include <vector>
#include <bitset>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <list>
#include <set>
#include <map>

using namespace std;

typedef long long        LL;
typedef pair<int, int>   pii;
typedef pair<int, pii>   piii;
typedef vector<int>      vi;
typedef vector<pii>      vii;
typedef vector<piii>     viii;

#ifdef _WIN32
#define getchar_unlocked getchar
#endif
inline void inpint( int &n ) {
  n=0; register int ch = getchar_unlocked(); bool sign = 0;
  while(ch < 48 || ch > 57) { if(ch == '-') sign = 1; ch = getchar_unlocked(); }
  while(ch >= 48 && ch <= 57) { n = (n << 3) + (n << 1) + ch - 48, ch = getchar_unlocked(); }
  if(sign) n = -n;
}

inline int sqr(int x){return x * x;}
inline int cube(int x){return x * x * x;}
inline LL sqrLL(LL x){return x * x;}
inline LL cubeLL(LL x){return x * x * x;}

const LL LLINF      = 9223372036854775807LL;
const LL LLINF17    = 100000000000000000LL;
const int INF       = 2147483647;
const int INF9      = 1000000000;
const int MOD       = 1000000007;
const double eps    = 1e-7;
const double PI     = acos(-1.0);

#define FOR(a,b,c)   for (int (a)=(b); (a)<(c); (a)++)
#define FORN(a,b,c)  for (int (a)=(b); (a)<=(c); (a)++)
#define FORD(a,b,c)  for (int (a)=(b); (a)>=(c); (a)--)
#define REP(i,n)     FOR(i,0,n)
#define REPN(i,n)    FORN(i,1,n)
#define REPD(i,n)    FORD(i,n,1)

#define RESET(a,b)   memset(a,b,sizeof(a)) 
#define SYNC         ios_base::sync_with_stdio(0);
#define SIZE(a)      (int)(a.size())
#define MIN(a,b)     (a) = min((a),(b))
#define MAX(a,b)     (a) = max((a),(b))
#define ALL(a)       a.begin(),a.end()
#define RALL(a)      a.rbegin(),a.rend()
#define SIZE(a)      (int)(a.size())
#define LEN(a)       (int)(a.length())

#define fi           first
#define se           second
#define pb           push_back
#define mp           make_pair

int dr[] = {1,0,-1,0,-1,1,1,-1};
int dc[] = {0,-1,0,1,1,1,-1,-1};
int t, n; vector<string> v; string s;
int pos[105], cnt[105];
int main(){
	scanf("%d",&t);
	REPN(tc,t){
		scanf("%d",&n); 
		string s1, s2;
		cin >> s1 >> s2;

		int i = 0, j = 0; bool valid = 1;
		if(s1[i] != s2[j]) valid = 0;

		int ans = 0;
		while(valid && i < LEN(s1) && j < LEN(s2)){
			int cnt1 = 1, cnt2 = 1; 
			while(i + 1 < LEN(s1) && s1[i] == s1[i+1]) 
				i++, cnt1++;
			while(j + 1 < LEN(s2) && s2[j] == s2[j+1])
				j++, cnt2++;
			ans += abs(cnt1 - cnt2);
			i++; j++;

			if(i < LEN(s1) && j < LEN(s2) && s1[i] != s2[j]){
				valid = 0;
				break;
			}
		}

		if(i != LEN(s1) || j != LEN(s2)) valid = 0;

		printf("Case #%d: ",tc);
		if(!valid) puts("Fegla Won");
		else printf("%d\n",ans);

		// bool valid = 0;
		// RESET(cnt,0);
		// RESET(pos,0);

		// REPN(i,n){
		// 	char prev = '.'; 
		// 	int j = 0;
		// 	while(j < LEN(v[i])){
		// 		while(j + 1 < LEN(v[i]) && v[i][j] == v[i][j+1]){
		// 			j++;
		// 		}
		// 		j++; prev = v[i][j]; cnt[i]++;
		// 	}
		// }

		// FORN(i,2,n){
		// 	if(cnt[i] != cnt[1]){
		// 		valid = 0;
		// 		goto end;
		// 	}
		// }

		// while(1){
		// 	while(pos[1] + 1 < LEN(v[1]) && v[1][pos[1]] == v[1][pos[1]+1])
		// 		pos[1]++;
		// 	char cur = v[1][pos[1]];

		// 	bool end = 1;
		// 	for(int i = 2; i <= n; i++){
		// 		if(v[i][pos[i]] != cur){
		// 			valid = 0;
		// 			goto end;
		// 		}

		// 		while(pos[i] + 1 < LEN(v[i]) && v[i][pos[i]] == v[i][pos[i]+1])
		// 			pos[i]++;
		// 		if(pos[i] != LEN(v[i])) end = 0;
		// 	}

		// 	if(end) break;
		// }

		// end:
		// printf("Case #%d: ",tc);
		// if(!valid) puts("Fegla Won");
	}

	return 0;
}