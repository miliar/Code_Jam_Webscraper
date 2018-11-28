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

inline string solve(char f, int n){
	if(n == 0){
		if(f == 'P')
			return "P";
		else if(f == 'R')
			return "R";
		else
			return "S";
	}
	if(f == 'P'){
		string s1 = solve('P',n-1), s2 = solve('R',n-1);
		return s1 < s2 ? s1+s2 : s2+s1;
	}
	else if(f == 'R'){
		string s1 = solve('R',n-1), s2 = solve('S',n-1);
		return s1 < s2 ? s1+s2 : s2+s1;
	}
	else{
		string s1 = solve('S',n-1), s2 = solve('P',n-1);
		return s1 < s2 ? s1+s2 : s2+s1;
	}
}

int main(){
	ios_base::sync_with_stdio(false);

	int T;
	cin >> T;
	FOR(test_no,0,T){
		int n, p, r, s;
		cin >> n >> r >> p >> s;		
		cout << "Case #" << test_no+1 << ": ";
		string s1 = solve('P',n);
		if(count(s1.begin(), s1.end(), 'P') != p || count(s1.begin(), s1.end(), 'R') != r || count(s1.begin(), s1.end(), 'S') != s)
			s1 = "Z";
		string s2 = solve('S',n);
		if(count(s2.begin(), s2.end(), 'P') != p || count(s2.begin(), s2.end(), 'R') != r || count(s2.begin(), s2.end(), 'S') != s)
			s2 = "Z";
		string s3 = solve('R',n);
		if(count(s3.begin(), s3.end(), 'P') != p || count(s3.begin(), s3.end(), 'R') != r || count(s3.begin(), s3.end(), 'S') != s)
			s3 = "Z";
		string ans = min(s1, min(s2, s3));
		cout << (ans != "Z" ? ans : "IMPOSSIBLE") << '\n';
	}

	return 0;
}
