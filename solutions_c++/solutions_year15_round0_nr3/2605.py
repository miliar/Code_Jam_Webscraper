#include <iostream>
#include <cstdio>
#include <iomanip>
#include <cmath>
#include <complex>
#include <numeric>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <cstring>
#include <cstdlib>
#include <algorithm>

using namespace std;
#define FOR(i,m,n) for(int i = (m); i < (n); i++)
#define ROF(i,m,n) for(int i = (n)-1; i >= (m); i--)
#define foreach(x,i) for( __typeof((x).begin()) i = (x).begin(); i != (x).end(); i++)
typedef long long LL;
typedef unsigned long long uLL;
typedef vector<int> VI;
typedef vector<LL> VLL;
#define SZ(x) ((int)(x).size())
typedef pair<int,int> pii;
typedef pair<LL,LL> pll;
#define FR first
#define SC second

int f[5][5] = { {0, 0, 0, 0, 0},
			  {0, 1, 2, 3, 4},
			  {0, 2,-1, 4,-3},
			  {0, 3,-4,-1, 2},
			  {0, 4, 3,-2,-1}};

const int MAX = 100*20000;
int pmul[MAX];
char s[MAX];

int sgn(int x){
	return x < 0 ? -1 : 1;
}

int main(){
	pmul[0] = 1;
	int T;
	cin >> T;
	FOR(cnt,0,T){
		int x, l;
		cin >> x >> l;
		cin >> s;
		
		l = l*x;
		FOR(i,0,l){
			pmul[i+1] = sgn(pmul[i]) * f[abs(pmul[i])][s[i%x]-'i'+2];
		}

		int p1 = 0, p2 = 0;
		FOR(i,0,l)
			if(!p1 && pmul[i+1] == 2)
				p1 = i+1;
		FOR(i,0,l-1)
			if(pmul[i+1] == 4)
				p2 = i+1;
		string ans = "NO";
		if(p1 && p2 && p1 < p2 && pmul[l] == -1)
			ans = "YES";
		cout << "Case #" << cnt+1 << ": " << ans << '\n';
	}
	return 0;
}
