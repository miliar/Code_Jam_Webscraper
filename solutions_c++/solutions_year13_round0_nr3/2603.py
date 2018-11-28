#include <iostream>
#include <iomanip>
#include <sstream>
#include <algorithm>
#include <functional>
#include <numeric>
#include <string>
#include <utility>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <bitset>
#include <deque>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>

using namespace std;

#define rep(i, n) for(int i = 0; i < (n); i++)
#define For(i, a, b) for(int i = (a); i < (b); i++)
#define foreach(it, c) for(__typeof (c).begin() it = (c).begin(); it != (c).end(); ++it)
#define pb push_back
#define mp make_pair
#define fst first
#define snd second
#define sz(v) (int)(v).size()
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define sqr(x) ((x) * (x))
#define clr(m, c) memset((m), (c), sizeof (m))
#define DBG(x) cout << #x << " = " << x << endl
#define EPS 1e-9
#define PI 3.14159265358979323846264338327950

template<class T> T abs(T x) { return x > 0 ? x : -x; }

typedef long long ll;
typedef long double ld;
typedef pair<int, int> ii;
typedef vector<int> vi;

const ll INF = 1LL<<60;
const ll MOD = 1000000007;

bool pal[1111];
bool sqpal[1111];

string toString(int n){
	ostringstream oss;
	oss << n;
	return oss.str();	
}

bool isPal(int n){
	string s = toString(n);
	int tam = sz(s);
	for(int i = 0; i < tam / 2; i++)
		if(s[i] != s[tam - i - 1]) return false;
	return true;
}

int main(){
	memset(pal, false, sizeof pal);
	memset(sqpal, false, sizeof sqpal);
	for(int i = 1; i <= 1010; i++) pal[i] = isPal(i);
	for(int i = 1; i <= 1010; i++){
		int isq = (int)sqrt(i);
		sqpal[i] = (pal[i] and sqr(isq) == i and pal[isq]);
	}
	int tt; cin >> tt;
	int a, b;
	for(int t = 1; t <= tt; t++){
		scanf("%d %d", &a, &b);
		int res = 0;
		for(int i = a; i <= b; i++) res += sqpal[i];
		printf("Case #%d: %d\n", t, res);
	}
	return 0;
}
