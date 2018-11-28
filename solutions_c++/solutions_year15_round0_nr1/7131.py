#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <stack>
#include <queue>
#include <deque>
#include <list>
#include <string>
#include <algorithm>
#include <math.h>
#include <stdio.h>

using namespace std;

#define SZ(a) int((a).size()) 
#define PB push_back 
#define MP make_pair
#define ALL(c) (c).begin(),(c).end() 
#define TR(c, i) for(auto i = (c).begin(); i != (c).end(); i++) 
#define DISP(c)	tr(c,i)	cout << *i << endl;
#define PR(c, x) ((c).find(x) != (c).end()) 
#define CPR(c, x) (find(all(c),x) != (c).end()) 	
#define FF1(i, n) for(int i = 0; i < n; i++)
#define FF2(i, a, b) for(int i = a; i < b; i++)
#define FF3(i, a, b, c)	for(int i = a; i < b; i += c)
#define TL(T)	int T; for(cin >> T; T; T--)
#define RM(a, n) a % n >= 0 ? a % n : (n + a % n)
#define GI(t, type)	type t; cin >> t;
#define F first
#define S second
#define _ ios_base::sync_with_stdio(false);

const double EPS = 1e-9;
const double PI = acos(-1.0);
const int MOD = 1000 * 1000 * 1000 + 7;
const int INF = 2000 * 1000 * 1000;

typedef vector<int> vi; 
typedef vector<vi > vvi; 
typedef pair<int,int> ii; 
typedef long long int ll;

int main(){ _
	int t; cin >> t;
	for(int T = 1; T <= t; T++){
		int smax; cin >> smax;
		string s; cin >> s;
		int res = 0, count = s[0] - '0';
		for(int i = 1; i < s.size(); i++){
			res += max(i - count, 0);
			count += s[i] - '0' + max(i - count, 0);
		}
		cout << "Case #" << T << ": " << res << endl;
	}

	return 0;
}