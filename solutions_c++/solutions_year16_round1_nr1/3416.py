#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include <cstring>
#include <cstdio>
#include <map>
#include <set>
#include <queue>
#include <algorithm>

using namespace std;

#define f first
#define s second
#define mp make_pair
#define pb push_back
#define all(a) a.begin(), a.end()
#define sqr(x) (x) * (x)
#define forn(i, l, r) for(int i = l; i < r; i ++)
#define forit(it, s) for(__typeof(s.begin()) it = s.begin(); it != s.end(); it ++)
#define y1 salnk
#define N 200100              
#define sz(a) (int)a.size()
#define ll long long
const int inf = (int)1e9;
const double pi = acos(-1.0);
const double eps = 1e-9;

string v, g, resmi, resma, s;
int t, n, f;
vector <string> vv;
set <string> q;
set <string> :: iterator it;
int main () {
    //freopen("in", "r", stdin);
    cin >> t;
    while (t--) {
     	cin >> s;
     	n = s.size();
     	f++;
     	cout << "Case #"<<f<<": ";
     	if (n == 1) {
     	 	cout << s << endl;
     	 	continue;
     	}
     	q.clear();

     	v = s[0];
     	q.insert(v);
     	for (int i = 1; i < n; i++) {
 	 	resmi = char(200);
 	 	resma = char(0);
 	 //	cerr << resmi << " " << resma << endl;
 	 	for (it = q.begin(); it != q.end(); it++) {
     	 	 	v = *it;//q.begin();
     	 	 	g = v+s[i];
     	 	 	resmi = min(resmi, g);
     	            	 	resma = max(resma, g);
     		 	g = s[i]+v;
     	             	 	resmi = min(resmi, g);
     	 	 	resma = max(resma, g);
     	 	}
     	 	q.clear();
     	 	q.insert(resmi);
     	 	q.insert(resma);
     	}
     			
     	it = q.end();
     	it--;
     	cout << *it << endl;
    }
    return 0;
}