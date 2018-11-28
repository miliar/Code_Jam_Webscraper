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

int d, x, best, t;
int cnt[10];
vector<ii> v;

void cut(int num, int opt){
	if (num == 9 && opt == 2){
		cnt[9]--;
		cnt[3] += 3;
		t+= 2;
	}
	else{
		cnt[num]--;
		cnt[num/2]++;
		cnt[num - num/2]++;
		t++;
	}
	v.clear();
	REP(i,0,10) if (cnt[i]) v.pb(mp(i, cnt[i]));
}


void go(){
	REP(i,0,10) cnt[i] = 0;
	REP(i,0,v.size()) {
		cnt[v[i].fst] = v[i].snd;
	}
	best = min(best, v[v.size()-1].fst + t);
	
	if (cnt[9] >= 4) return;
	else if (cnt[9] >= 2) cut(9,1);
	else if (cnt[9] == 1){
		if (cnt[4] || cnt[5] || cnt[7] || cnt[8]) cut(9, 1);
		else cut(9,2);
	}
	else if (cnt[8] >= 4) return;
	else if (cnt[8]) cut(8,1);
	else if (cnt[7] >= 3) return;
	else if (cnt[7]) cut(7,1);
	else if (cnt[6] >= 3) return;
	else if (cnt[6]) cut(6,1);
	else if (cnt[5] >= 2) return;
	else if (cnt[5]) cut(5,1);
	else if (cnt[4] >= 2) return;
	else if (cnt[4]) cut(4,1);
	else return;
	go();	
}


int main(){
	int nCases;
	cin >> nCases;
	REP(casenum,0,nCases){
		v.clear();
		REP(i,0,10) cnt[i] = 0;
		best = 0;
		cin >> d;
		REP(i,0,d){
			cin >> x;
			cnt[x]++;
			best = max(best,x);
		}
		REP(i,0,10){
			if (cnt[i]) v.pb(mp(i, cnt[i]));
		}
		t = 0;
		go();
		cout << "Case #" << casenum+1 << ": " << best << endl;
	}  
	return 0;
}
