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

int tcase,N,P;

inline int worst(int x) {
	int stronger = x + 1;
	int res = 0;
	int s = N-1;
	while (stronger >= 2) {
		res |= (1<<s);
		s--;
		stronger /= 2;
	}
	return res;
}

inline int best(int x) {
	int weaker = (1<<N) - x;
	int res = 0;
	int s = N-1;
	while (weaker >= 2) {
		s--;
		weaker /= 2;
	}
	while (s >= 0) {
		res |= (1<<s);
		s--;
	}
	return res;
}

int main()
{
	getInt(tcase);
	FOR(t,1,tcase)
	{
		getInt(N);
		cout << "Case #" << t << ": " ;
		getInt(P);
		int ans1 = -1, ans2 = -1;
		FORD(i, (1<<N)-1, 0) {
			//cout << best(i) << " " << worst(i) << " " << P << endl;
			if (ans1 == -1 && worst(i) < P) ans1 = i;
			if (ans2 == -1 && best(i) < P) ans2 = i;
		}
		cout << ans1 << " " << ans2 << endl;
	}
	return 0;
}
