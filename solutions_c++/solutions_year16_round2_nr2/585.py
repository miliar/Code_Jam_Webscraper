#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <iomanip>
#include <complex>
#include <numeric>
#include <cstdio>
#include <vector>
#include <string>
#include <cmath>
#include <deque>
#include <queue>
#include <set>
#include <map>

//#include <unordered_map>
//#include <unordered_set>

using namespace std;
#define FOR(i,m,n) for(int i = (m); i < (n); i++)
#define ROF(i,m,n) for(int i = (n)-1; i >= (m); i--)
#define foreach(x,i) for( __typeof((x).begin()) i = (x).begin(); i != (x).end(); i++)
typedef long long LL;
typedef long long ll;
typedef unsigned long long uLL;
typedef vector<int> VI;
typedef vector<LL> VLL;
#define SZ(x) ((int)(x).size())
typedef pair<int,int> pii;
typedef pair<LL,LL> pll;
#define FR first
#define SC second
typedef complex<double> point;
#define X first
#define Y second
//#define X real()
//#define Y imag()

template<class T> ostream& operator << (ostream &o, const vector<T> &t){
	o << "[" << SZ(t);
	bool f = false;
	foreach(t,it)
		o << (f++ ? ", " : ": ") << (*it);
	return o << "]";
}

template<class T1, class T2> ostream& operator << (ostream &o, const pair<T1, T2> &p){
	return o << "(" << p.FR << ", " << p.SC << ")";
}

LL ans1, ans2;

inline void check_ans(LL a, LL b){
	if(abs(a-b) < abs(ans1-ans2)){
		ans1 = a;
		ans2 = b;
	}
	else if(abs(a-b) == abs(ans1-ans2)){
		if(a < ans1){
			ans1 = a;
			ans2 = b;
		}
		else if(a == ans1 && b < ans2){
			ans1 = a;
			ans2 = b;
		}
	}
}

LL mystoll(string s){
	if(s == "")
		return 0;
	return stoll(s);
}
string set_min(string s){
	string t = s;
	replace(t.begin(), t.end(), '?', '0');
	return t;
}
string set_max(string s){
	string t = s;
	replace(t.begin(), t.end(), '?', '9');
	return t;
}

bool can_be_eq(string a, string b){
	FOR(i,0,SZ(a))
		if(a[i] != '?' && b[i] != '?' && a[i] != b[i])
			return false;
	return true;
}
string set_eq_min(string a, string b){
	string s = a;
	FOR(i,0,SZ(a))
		if(b[i] != '?')
			s[i] = b[i];
	return set_min(s);
}

LL concatll(LL a, LL b, LL l){
	FOR(i,0,l)
		a *= 10;
	return a+b;
}

string mylead(LL a, int l){
	string y = to_string(a);
	string x(l-SZ(y), '0');
	return x+y;
}

int main(){
	ios_base::sync_with_stdio(false);

	int T;
	cin >> T;
	FOR(test,0,T){
		ans1 = -(1ll<<61);
		ans2 = 1ll<<61;

		string a, b;
		cin >> a >> b;
		int n = SZ(a);

		FOR(eq,0,n){
			if(!can_be_eq(a.substr(0,eq), b.substr(0,eq)))
				break;
			FOR(i,0,10) FOR(j,0,10) if(i != j)
				if(a[eq] == '?' || a[eq] == i+'0')
					if(b[eq] == '?' || b[eq] == j+'0'){
						LL p1 = mystoll(set_eq_min(a.substr(0,eq), b.substr(0,eq)));
						LL p2 = 10*p1+j;
						p1 = 10*p1+i;
						LL t1, t2;
						if(i > j){
							t1 = mystoll(set_min(a.substr(eq+1)));
							t2 = mystoll(set_max(b.substr(eq+1)));
						}
						else{
							t1 = mystoll(set_max(a.substr(eq+1)));
							t2 = mystoll(set_min(b.substr(eq+1)));
						}
						check_ans(concatll(p1,t1,n-eq-1), concatll(p2,t2,n-eq-1));
					}
		}
		if(can_be_eq(a.substr(0,n), b.substr(0,n))){
			string x = set_eq_min(a.substr(0,n), b.substr(0,n));
			LL y = mystoll(x);
			check_ans(y, y);
		}

		cout << "Case #" << test+1 << ": " << mylead(ans1,SZ(a)) << ' ' << mylead(ans2, SZ(a)) << endl;
	}

	return 0;
}
