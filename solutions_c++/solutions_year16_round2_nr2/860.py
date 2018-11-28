#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
using namespace std;
#define pb(X) push_back(X)
#define mp(X,Y) make_pair(X,Y)
#define sz(X) (int)X.size()
#define clr(X) memset(X,0,sizeof(X));
#define xx first
#define yy second
typedef pair<int, int> pii;
typedef long long ll;
typedef unsigned long long ull;

int br, bs;

void solve(string r, string s) {
	for(int i=0;i<sz(r);i++) {
		if(r[i]=='?') {
			string rr = r;
			for(char j='0'; j<='9';j++) {
				rr[i]=j;
				solve(rr,s);
			}
			return;
		}
	}
	for(int i=0;i<sz(s);i++) {
		if(s[i]=='?') {
			string ss =s;
			for(char j='0'; j<='9';j++) {
				ss[i]=j;
				solve(r,ss);
			}
			return;
		}
	}
	int xr = atoi(r.c_str());
	int xs = atoi(s.c_str());
	if(abs(xr-xs) <= abs(br-bs)) {
		if(abs(xr-xs) < abs(br-bs)) {
			br = xr;
			bs = xs;
		} else if (xr <= br) {
			if(xr<br) {
				br = xr;
				bs = xs;
			} else if (xs < bs) {
				br = xr;
				bs = xs;
			}
		}
	}
}

int main(){
	int T;
	scanf("%d", &T);
	for(int caso=1;caso<=T;caso++) {
		string r, s;
		cin >> r >> s;
		br =0; bs = 100000;
		solve(r,s);
		if(sz(r)==1) {
		  printf("Case #%d: %01d %01d\n",caso,br,bs);
		} else if(sz(r)==2) {
		  printf("Case #%d: %02d %02d\n",caso,br,bs);
		} else {
		  printf("Case #%d: %03d %03d\n",caso,br,bs);
		}
	}
	return 0;
}
