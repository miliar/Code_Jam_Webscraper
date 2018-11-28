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

int cnt[200];

inline void reduce(string num){
	FOR(i,0,SZ(num)){
		if(!cnt[(int)num[i]])
			cerr << "NOOOOOOOOOOOOOOOOOOOOOO" << endl;
		cnt[(int)num[i]]--;
	}
}

int main(){
	ios_base::sync_with_stdio(false);
	int T;
	cin >> T;
	FOR(test,0,T){
		cout << "Case #" << test+1 << ": ";

		string str;
		cin >> str;
		fill(cnt,cnt+200,0);
		FOR(i,0,SZ(str))
			cnt[(int)str[i]]++;
		string ans = "";
		while(cnt['Z']){
			ans += "0";
			reduce("ZERO");
		}
		while(cnt['X']){
			ans += "6";
			reduce("SIX");
		}
		while(cnt['G']){
			ans += "8";
			reduce("EIGHT");
		}
		while(cnt['S']){
			ans += "7";
			reduce("SEVEN");
		}
		while(cnt['V']){
			ans += "5";
			reduce("FIVE");
		}
		while(cnt['F']){
			ans += "4";
			reduce("FOUR");
		}
		while(cnt['H']){
			ans += "3";
			reduce("THREE");
		}
		while(cnt['I']){
			ans += "9";
			reduce("NINE");
		}
		while(cnt['E']){
			ans += "1";
			reduce("ONE");
		}
		while(cnt['O']){
			ans += "2";
			reduce("TWO");
		}
		sort(ans.begin(), ans.end());
		cout << ans << endl;
	}

	return 0;
}
