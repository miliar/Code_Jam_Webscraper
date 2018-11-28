#include <iostream>
#include <cstdio>
#include <algorithm>
#include <stack>
#include <queue>
#include <vector>
#include <map>
#include <set>
#include <cstring>
#include <cmath>
#include <cstdlib>

//Hendri's Template
#define REP(i, n) for(int i = 0, _n = (n); i < _n; i++)
#define FOR(i, a, b) for(int i = (a), _b = (b); i <= _b; i++)
#define FORD(i, a, b) for(int i = (a), _b = (b); i >= _b; i--)
#define FOREACH(it,c) for (__typeof ((c).begin()) it = (c).begin(); it != (c).end(); it++)
#define RESET(A,v) memset(A, v, sizeof(A))
#define DEBUG(x) cout << #x << " = " << x << endl;

#define MP make_pair
#define PB push_back
#define F first
#define S second

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;

template<class T> inline T MIN(T a, T b){return a < b?a:b;}
template<class T> inline T MAX(T a, T b){return a > b?a:b;}

template<class T> inline void getInt(T& x)
{
	char c;
	int mul = 1;
	while((c = getchar()) != EOF)
	{
		if(c == '-')mul = -1;
		if(c >= '0' && c <= '9')
		{
			x = c-'0';
			break;
		}
	}
	if(c == EOF){x = EOF;return;}
	while(c = getchar())
	{
		if(c >= '0' && c <= '9')
		{
			x = (x<<1)+(x<<3)+(c-'0');
		}
		else break;
	}
	x *= mul;
}
//End of Hendri's Template

int tcase,N,M;
int entry[1001], exits[1001], num[1001];

long long MOD = 1000002013;

inline long long dis(int a, int b) {
	if (a == b) return 0LL;
	long long x = 0;
	long long y = 0;
	for (int i = a + 1; i <= b; i++, y++) {
		x += N - y;
	}
	return x;
}

int main()
{
	getInt(tcase);
	FOR(t,1,tcase)
	{
		getInt(N);
		cout << "Case #" << t << ": " ;
		getInt(M);
		vector<pii> v;
		long long ori = 0;
		REP(i, M) {
			cin >> entry[i] >> exits[i] >> num[i];
			v.PB(MP(entry[i], -num[i]));
			v.PB(MP(exits[i], num[i]));
			ori += (long long)num[i] * dis(entry[i], exits[i]);
			ori %= MOD;
		}
		//cout << "ORI " << ori << endl;
		sort(v.begin(), v.end());
		vector<pii> v2;
		long long res = 0;
		REP(i, v.size()) {
			//cout << v[i].F << " " << v[i].S << endl;
			if (v[i].S < 0) {
				v2.PB(MP(v[i].F, -v[i].S));
			} else {
				int left = v[i].S;
				int s = v2.size() - 1;
				while (left) {
					while (v2[s].S == 0) s--;
					int use = min(left, v2[s].S);
					v2[s].S -= use;
					left -= use;
					res += (long long)use * dis(v2[s].F, v[i].F);
					res %= MOD;
					//cout << use << endl;
				}
			}
		}
		cout << ori - res << endl;
	}
	return 0;
}
