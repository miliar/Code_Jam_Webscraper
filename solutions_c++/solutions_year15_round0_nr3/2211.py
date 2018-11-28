#include <string>
#include <cstring>
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
using namespace std;
#define all(v) (v).begin(),(v).end()
#define rall(v) (v).rbegin(),(v).rend()
#define pb(x) push_back(x)
#define REP(i,x,y) for(int (i)=(x);(i)<(y);(i)++)
#define REPIT(it,A) for(typeof(A.begin()) it = (A.begin()); it!=A.end();it++)
#define sqr(x) ((x)*(x))
#define mp(x,y) make_pair((x),(y))
#define trace(x) cerr << #x << ": " << x << endl;
#define fst first
#define snd second
#define itm1 fst.fst
#define itm2 fst.snd
#define itm3 snd
#define mt(a,b,c) mp(mp(a,b),c)
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef long long int64;
typedef unsigned long long uint64;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<ii, int> tri;
typedef pair<ll, ll> pll;
typedef pair<pll, ll> tri64;
typedef set<int> seti;
typedef set<ii> setii;
typedef stack<int> stki;
typedef stack<ii> stkii;
typedef queue<int> qi;
typedef queue<ii> qii;
typedef map<int,int> mapii;
typedef map<string,int> mapsi;
typedef unsigned int uint;

const double PI = 3.14159265359;

int n, x;
string base;
string s;


pair<char,int> mul(char a, char b){
	if (a == '1') return mp(b,0);
	if (b == '1') return mp(a,0);
	if (a == b) return mp('1',1);
	if (a == 'i'){
		if (b == 'j') return mp('k',0);
		if (b == 'k') return mp('j',1);
	}
	if (a == 'j'){
		if (b == 'i') return mp('k',1);
		if (b == 'k') return mp('i',0);
	}
	if (a == 'k'){
		if (b == 'i') return mp('j',0);
		if (b == 'j') return mp('i',1);
	}
}

int main(){
	int nCases;
	cin >> nCases;
	REP(casenum,0,nCases){
		cin >> n >> x;
		cin >> base;
		s = "";
		REP(i,0,x) s = s + base;

		int i = -1;
		char c = '1';
		int neg = 0;
		while (c != 'i' || neg != 0){
			if (i >= n*x-1) break;
			pair<char,int> res = mul(c, s[++i]);
			c = res.fst;
			neg ^= res.snd;
			//cout << "(" << c << "," << neg << "), ";
		}
		int j = n*x;
		c = '1';
		neg = 0;
		while (c != 'k' || neg != 0){
			if (j <= i+1) break;
			pair<char,int> res = mul(s[--j], c);
			c = res.fst;
			neg ^= res.snd;
		}
		//cout << "Got (i,j):" << i << "," << j << endl;
		c = '1';
		neg = 0;
		if (j > i){
			REP(k,i+1,j){
				pair<char,int> res = mul(c, s[k]);
				c = res.fst;
				neg ^= res.snd;
			}
		}
		//cout << "Product was " << c << "," << neg << endl;
		cout << "Case #" << casenum+1 << ": ";
		if (c == 'j' && neg == 0){
			cout << "YES" << endl;
		}
		else cout << "NO" << endl;
		//cout << "Became i at p:" << i << endl;
	}  
	return 0;
}

