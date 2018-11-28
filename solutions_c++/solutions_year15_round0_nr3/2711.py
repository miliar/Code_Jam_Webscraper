#include<algorithm>
#include<cassert>
#include<cctype>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<deque>
#include<sstream>
#include<iostream>
#include<list>
#include<map>
#include<queue>
#include<set>
#include<string>
#include<vector>
using namespace std;

typedef long long LL;
typedef long double LD;

#define dprintf(...) fprintf(stderr, __VA_ARGS__)

int cond = 0;
#define DB(X) {if(cond){cerr<<"Line:"<<__LINE__<<", "<<#X<<" = "<<X<<endl;}}
int tab[10000];
int n;
int x = 1;
int q[5][5] = { {0, 0, 0, 0, 0},
								{0, 1, 2, 3, 4}, 
								{0, 2, -1, 4, -3},
								{0, 3, -4, -1, 2},
								{0, 4, 3, -2, -1}};


int mul(int a, int b) {
	bool sg = (a*b > 0);
	if (a < 0) a = -a;
	if (b < 0) b = -b;
	int res = q[a][b];
	if (!sg) return -res;
 	return res;	
}
int pot(int a, long long x) {
	if (x == 1) {
		return a;
	}
	int x2 = pot(a, x/2);
	int xx = mul(x2, x2);
	if (x % 2) {
		return mul(xx, a);
	}
	return xx;
}
void resp(string s) {
		cout << "Case #" << x << ": " << s << "\n";//result 
}
int convert(char c) {
			if (c == 'i') {
				return 2;			
			}
			if (c == 'j') {
				return 3;
			}
			if (c == 'k') {
				return 4;
			}
}
int main() {
	int t; cin >> t;
	for(; x <= t; ++x){
		long long l, xx; cin >> l >> xx;
		string s; cin >> s;
		stringstream ss;
		int res = 1;
		for(int i = 0; i < l; ++i) {
			res = mul(res, convert(s[i]));
		}
		for (int i = 0; i < xx; ++i) {
			ss << s;
		}
		int resl = res;
		res = pot(res, xx);
		DB(res);
		if (res != -1) {
			resp("NO");	
			continue;
		}
		res = 1;
		int firsti = 0;
		s = ss.str();
		for(; firsti < l*xx; ++firsti) {
			res = mul(res, convert(s[firsti]));
			if (res == 2) break;
		}
		int lastj = l*xx - 1;
		res = 1;
		for(;lastj >= 0; --lastj) {
			res = mul(convert(s[lastj]), res);
			if (res == 4) break;
		}
		DB(firsti); DB(lastj);
		if (firsti < lastj) {
			resp("YES");
		}
		else {
			resp("NO");
		}
		
	}
	return 0;
}

