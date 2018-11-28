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

int n, p[20], c[20], b[20][20], a[20][20];


bool calc(){
 	sort(p, p + n);
 	do {
 		sort(c, c + n);
 		do {
 			int bad = 0;
 		     for (int i = 0; i < n; i++)
 		    	if (b[p[i]][c[i]]) {
 		    	 	continue;
 		    	} else {
 		    		bad = 2;
 		    	 	for (int j = i + 1; j < n; j++)
 		    	 		if (b[p[i]][c[j]]) bad =1;
 		    	     break;
 		    	}
 		    	if (bad == 2) {
 		    		return 0;	 	
 		    	}
 		} while (next_permutation(c, c + n));
 	} while (next_permutation(p, p + n));
 	return 1;
}
int t = 0;
int main () {
    //freopen("in", "r", stdin);
        cin >> t;
        int qq = 0;
     while (t--) {

     	 	cin >> n;
      	for (int i = 0; i < n; i++)
      		c[i] = i, p[i] = i;

      	qq++;
      	char ch;
      	for (int i = 0; i < n; i++)
      		for (int j = 0; j < n; j++) {
      		     cin >> ch;
                    if (ch == '1')	a[i][j] = 1; else a[i][j] = 0;
      		}
      	int res = n * n;
          for (int mask = 0; mask < (1 << (n * n)); mask++) {
          	int fm = mask, cr = 0;
           	for (int i = 0; i < n * n; i++) {
           		int x = i / n;	
           		int y = i % n;
           		b[x][y] = a[x][y];
           		if (mask & (1 << i)) {
           		 	if (!a[x][y]) cr++;
           		 	b[x][y] = 1;
           		}
           	//	cerr << x << " " << y << " " << a[x][y]<< endl;

           		if (a[x][y]) fm |= (1<<i);
               }
               if (calc()){
               //  cerr << cr << " " << mask << endl;
                 res = min(res, cr);
               }
               //return 0;
          }
          printf("Case #%d: %d\n", qq, res);
     }
        return 0;
}