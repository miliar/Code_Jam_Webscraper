#include <bits/stdc++.h>
/*#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>*/
using namespace std;

#define MOD 1000000007
#define PB push_back
#define MP make_pair
#define MT make_tuple
#define fi first
#define se second
#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define F0(i,n) for (int i=0; i<(int)(n); ++i)
#define F1(i,n) for (int i=1; i<=(int)(n); ++i)
#define FR0(i,n) for(int i=(int)n-1; i>=0; --i)
#define FR1(i,n) for(int i=(int)n; i>0; --i)
#define FAB(i, a, b) for (int i=(int)a; i<=(int)(b); ++i)
#define FRAB(i, a, b) for (int i=(int)a; i>=(int)(b); --i)

typedef vector<int> VI;
typedef vector<VI> VII;
typedef pair<int, int> PII;
typedef vector<PII> VPI;
typedef long long I64;
typedef vector<I64> VI64;
typedef vector<VI64> VVI64;
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;

#define SZ(x) (int)(x.size())
const double pi = atan(1.0)*4.0;
const double eps = 1e-8;
ll gcd(ll x, ll y) { return y ? gcd(y, x%y) : x; }
int bc(int n) { return n ? bc((n-1)&n)+1 : 0; }

string sr;
vector<int> dig;
//string sn[10]={"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
string sn[10]={"ZERO", "SIX", "TWO", "EIGHT", "THREE", "FOUR", "SEVEN", "FIVE", "NINE", "ONE" };
int mapi[10]={0,6,2,8,3,4,7,5,9,1};
 
bool mat(string S, string sub) {
	int pos;
	//cerr << S << " " << sub << endl;
	F0(i,SZ(sub)) {
		pos=S.find(sub[i]);
		if(pos==string::npos) return false;
		else S.erase(pos,1);
	}	
	sr=S;
	//cerr << "FOund " << sub << " " << sr << endl;
	return true;
}
void pr(VI d) {
	sort(all(d));
	F0(i,SZ(d)) cout << d[i];
	return;
}
void getm(string S) {
	int j;
	F0(i,10) {
		j=i;
		sr=S;
		FAB(j,0,9) {
			while (SZ(sr)!=0 && mat(sr,sn[j])) {dig.PB(mapi[j]);}
		}
		if (SZ(sr)==0){ pr(dig); dig.clear(); return;}
		else dig.clear();
	}
	return;	
}


int main(void) {

//freopen("A-small-attempt1.in", "r", stdin);
//freopen("A-small-attempt1.out", "w", stdout);

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int tt, tn;
	cin >> tt;
	string s;
	F1(tn,tt) {
		cin >> s;
		cout << "Case #" << tn << ": ";
		getm(s);
		cout << endl;
	}

	return 0;
}
