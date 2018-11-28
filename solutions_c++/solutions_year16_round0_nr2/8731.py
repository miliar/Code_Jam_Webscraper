#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include <cstring>
#include <cstdio>
#include <map>
#include <stack>
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
#define ll long long
const int inf = (int)1e9;
const double pi = acos(-1.0);
const double eps = 1e-9;


int res, t, qq, p;
string s;

int get(string s) {
	int len = s.size();
	
	int res = 0;
 	for (;;)  {
 	      bool bad = 0;
 	      int p = 0;
 		for (int i = 0; i < len; i++) 
 			if (s[i] == '-') {
 			      p = i;
 				bad = 1;
 			}
 		if (!bad) return res;     
 		for (int i = 0; i < p + 1; i++) {
 			if (s[i] == '+') s[i] = '-'; else s[i] = '+';
 		}
 		res++;
 	}
 	return res;
 				
}
int main () {
    //freopen("in", "r", stdin);
    //freopen("out", "w", stdout);
    cin >> t;

    qq++;
    while (t--) {
      cin >> s;
      res = get(s);
      printf("Case #%d: %d\n", qq, res);
      qq++;
    }	
    return 0;
}