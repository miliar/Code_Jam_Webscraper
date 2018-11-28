#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>
using namespace std;
 
typedef vector<int> vi;
typedef vector<string> vs;
typedef long long ll;
typedef complex<int> pnt;
typedef pair<int, int> pii;

#define FOR(i,a,b) for(i=a;i<b;i++) 
#define RA(x) (x).begin(), (x).end()
#define REV(x) reverse(RA(x))
#define FE(i, x) for (typeof((x).begin()) i = (x).begin(); i != (x).end(); i++)
#define SZ(x) ((int) (x).size())
#define X first
#define Y second
#define MOD 1000000007
int main(){
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	int t=1, i, j, k, l, c, n, test;
	string s;
	cin >> t;
	FOR(test, 0, t){
		c = 0;
		cin >> s >> n;
		FOR(i, 0, SZ(s)) FOR(j, i, SZ(s)){
			l = 0;
			FOR(k, i, j+1){
				if(string("aeiou").find(s[k]) != string::npos)
					l = 0;
				else l++;
				if(l >= n){
					c++; break;
				}
			}
		}
		printf("Case #%d: %d\n", test+1, c);
	}
}

