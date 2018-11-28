#include<iostream>
#include<cstdio>

#include<string>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<deque>
#include<stack>

#include<iomanip>
#include<algorithm>
#include<cstring>
#include<ctime>
#include<cassert>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define correct(x, y, n, m) (0 <= x && x < n && 0 <= y && y < m)
#define X first
#define Y second
#define all(a) a.begin(), a.end()
#define pb push_back
#define mp make_pair
#define sz(v) (int)(v.size())

template<typename T> inline T abs(T a){ return ((a < 0) ? -a : a); }
template<typename T> inline T sqr(T a){ return a * a; }

typedef long long li;
typedef unsigned long long uli;
typedef long double ld;
typedef pair<int, int> pt;

const int N = 1009;
const int MOD = 1e9 + 7;
const int INF = 1e9;
const li INF64 = 2e18;

int t, n, m;
string s, ss;

// 1 i j k
// 1 2 3 4
int a[5][5] = {
	{0, 0, 0, 0, 0},
	{0, 1, 2, 3, 4},
	{0, 2, -1, 4, -3},
	{0, 3, -4, -1, 2},
	{0, 4, 3, -2, -1}
};


int f(char x){
	if(x == '1')
		return 1;
	if(x == 'i')
		return 2;
	if(x == 'j')
		return 3;
	if(x == 'k')
		return 4;
}
int main(){
#ifdef _DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
     
    srand(time(NULL));
    cout << setprecision(7) << fixed;
    cerr << setprecision(7) << fixed;
    
	
	cin >> t;
	forn(nt, t){
		cin >> n >> m >> ss;
		s = "";
		forn(_, m)
			s += ss;

		bool neg = false;
		int cur = f(s[0]);
		for(int i = 1; i < sz(s); ++i){
			cur = a[cur][f(s[i])];
			if(cur < 0)
				cur *= -1, neg ^= true;
		}
		if(!(cur == 1 && neg)){
			cout << "Case #" << nt + 1 << ": NO\n";
			continue;
		}
		int l = sz(s), r = -1;
		neg = false;
		cur = f(s[0]);
		if(cur == 2)
			l = 0;
		else
			for(int i = 1; i < sz(s); ++i){
				cur = a[cur][f(s[i])];
				if(cur < 0)
					cur *= -1, neg ^= true;
				if(cur == 2 && !neg){
					l = i;
					break;
				}
			}

		neg = false;
		cur = f(s[sz(s) - 1]);
		if(cur == 4)
			r = sz(s) - 1;
		else
			for(int i = sz(s) - 2; i >= 0; --i){
				cur = a[f(s[i])][cur];
				if(cur < 0)
					cur *= -1, neg ^= true;
				if(cur == 4 && !neg){
					r = i;
					break;
				}
			}
		if(l + 2 <= r)
			cout << "Case #" << nt + 1 << ": YES\n";
		else
			cout << "Case #" << nt + 1 << ": NO\n";

	}
	
    return 0;   
}