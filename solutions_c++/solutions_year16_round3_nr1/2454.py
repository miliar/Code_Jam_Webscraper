#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <functional>
#include <utility>
#define f first
#define s second
using namespace std; 
#define DEBUG(x) cout << '>' << #x << ':' << x << endl;
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
inline bool EQ(double a, double b) { return fabs(a-b) < 1e-9; }
const int INF = 1<<29;
typedef long long ll;
inline int two(int n) { return 1 << n; }
inline int test(int n, int b) { return (n>>b)&1; }
inline void set_bit(int & n, int b) { n |= two(b); }
inline void unset_bit(int & n, int b) { n &= ~two(b); }
inline int last_bit(int n) { return n & (-n); }
inline int ones(int n) { int res = 0; while(n && ++res) n-=n&(-n); return res; }
template<class T> void chmax(T & a, const T & b) { a = max(a, b); }
template<class T> void chmin(T & a, const T & b) { a = min(a, b); }
/////////////////////////////////////////////////////////////////////

void solve(vector<pair<int,int> >& A, int& total, vector<string>& ans) {
	int i;
	char ch1, ch2;
	if (A.size()==0) {
		for (i=0; i<ans.size(); i++) {
			cout << ans[i] << " ";
		}
		cout << endl;
		return;
	}
	if (A[0].f-1<=(total-2)/2 && A[1].f<=(total-1)/2) {
		ch1 = (char)(A[0].s+'A');
		string str1(1, ch1);
		ans.push_back(str1);
		A[0].f--;
		total--;
		//cout << "first case" << endl;
		//return;
	} else if (A[0].f==A[1].f || A[0].f==A[1].f+1) {
		ch1 = (char)(A[0].s+'A');
		ch2 = (char)(A[1].s+'A');
		string str2(1, ch1);
		str2.push_back(ch2);
		ans.push_back(str2);
		A[0].f--;
		A[1].f--;
		total -= 2;
		//cout << "second case" << endl;
	} else {
		ch1 = (char)(A[0].s+'A');
		string str3(1, ch1);
		str3.push_back(ch1);
		ans.push_back(str3);
		A[0].f-=2;
		total -= 2;
		//cout << "third case" << endl;
	}
	if (A.size()>=2 && A[1].f == 0) {
		A.erase(A.begin()+1);
	}
	if (A.size()>=1 && A[0].f == 0) {
		A.erase(A.begin());
	}
	sort(A.begin(), A.end(), greater<pair<int,int> >());
	solve(A, total, ans);
}
int main()
{
	int T, test, i, total, N, tmp;
	vector<pair<int, int> > A;
    cin >> T;
    vector<string> ans;
    for (test=1; test<=T; test++) {
    	cin >> N;
    	ans.clear();
    	A.clear();
    	total = 0;
    	for (i=0; i<N; i++) {
    		cin >> tmp;
    		A.push_back(make_pair(tmp, i));
    		// cin >> A[i].f;
    		// A[i].s = i;
    		total += A[i].f;
    	}
    	sort(A.begin(), A.end(), greater<pair<int,int> >());
    	cout << "Case #" << test << ": ";
    	solve(A, total, ans);
    }
    return 0;
}
