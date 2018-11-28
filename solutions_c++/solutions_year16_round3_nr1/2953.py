#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <sstream>
#include <set>
#include <iomanip>
#include <list>
#include <stack>
#include <queue>
#include <bitset>
#include <numeric>
#include <functional>

#include <cstdio>
#include <cmath>
#include <climits>
#include <cstring>
#include <cctype>
#include <cstdlib>

using namespace std;

typedef long long int ll;
typedef unsigned long long int ull;
typedef vector <int> vi;
typedef pair< int ,int > pii;
#define rep(i, n)       for(int i = 0; i < n; i++)
#define reps(i, a, n)   for(int i = a; i < n; i++)
#define foreach(it, v)  for( __typeof((v).begin())it = (v).begin() ; it != (v).end() ; it++ )
#define precout(a,b)    cout << fixed << setprecision((b)) << (a)
#define endl 			'\n'
#define pb              push_back
#define mp              make_pair
#define ff              first
#define ss              second
#define all(a)          a.begin(), a.end()
#define rall(a)			a.rbegin(), a.rend()
#define sz(x)			(int)x.size()
#define fastIO   		ios::sync_with_stdio(false); cin.tie(0);
string toString(long long n) { stringstream ss; ss << n; return ss.str(); }
long long toNumber(string s){ stringstream ss; long long n; ss << s; ss >> n; return n; }

bool cmp( pair <int, char> a, pair <int, char> b) {
	return a.ff > b.ff;
}

bool allone(map <char, int> m) {
	for (auto c : m) {
		if (c.ss != 1) return false;
	}
	return true;
}

int main() {
#ifndef ONLINE_JUDGE
    const clock_t begin_time = clock();
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
	
	fastIO
	
	int t;
	cin >> t;
	
	for (int T = 1; T <= t; T++) {
		cout << "Case #" << T << ": ";
		int n;
		cin >> n;
		map <char, int> m;
		char c = 'A';
		int x;
		int tot = 0;
		set < pair <int, char> > s;
		for (int i = 0; i < n; i++) {
			cin >> x;
			s.insert({-x, c + i});
			tot += x;
			m[c + i] += x;
			
		}

		if (n == 2) {
			while (m['A']) {
				cout << "AB ";
				m['A']--;
			}
			cout << endl;
		} else {
			pair <int, char> a1 = *s.begin();
			s.erase(a1);
			a1.ff *= -1;
			pair <int, char> a2 = *s.begin();
			s.erase(a2);
			a2.ff *= -1;
			pair <int, char> a3 = *s.begin();
			s.erase(a3);
			a3.ff *= -1;
			
			while (a1.ff != a2.ff) {
				a1.ff--;
				cout << a1.ss << " ";
			}
			
			while(a3.ff > 0) {
				cout << a3.ss << " ";
				a3.ff--;
			}
			
			while (a1.ff > 0) {
				cout << a1.ss << a2.ss << " ";
				a1.ff--;
			}
			cout << endl;
		}
		
		
	}
	
#ifndef ONLINE_JUDGE
   	cout << endl;
    cout << "Time : ";
    cout << float( clock () - begin_time ) / CLOCKS_PER_SEC << endl;
#endif
    
    return 0;
}
