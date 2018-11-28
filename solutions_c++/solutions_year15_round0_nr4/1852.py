#include<algorithm>
#include<cassert>
#include<cctype>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<deque>
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

int cond = 1;
#define DB(X) {if(cond){cerr<<"Line:"<<__LINE__<<", "<<#X<<" = "<<X<<endl;}}
int tab[10000];
int n;
int count(int a, int b) {
	return (upper_bound(tab, tab + n, b) - lower_bound(tab, tab + n, a));
}	
int x = 1;
void res(string s) {
		cout << "Case #" << x << ": " << s << "\n";//result 
}
int main() {
	int t; cin >> t;
	for(; x <= t; ++x){
		int y, r, c; cin >> y >> r >> c;
		if (r * c % y) {
			res("RICHARD"); continue;
		}
		if (y == 1) {
			res("GABRIEL"); continue;
		}
		if (y == 2) {
			res("GABRIEL"); continue;
		}
		if (y == 3) {
			if (r == 1 || c == 1) {
				res("RICHARD"); continue;		
			}
			res("GABRIEL"); continue;		
		}
		//y == 4;
		if (r * c == 4) {
			res("RICHARD"); continue;		
		}
		if (r == 2 || c == 2) {
			res("RICHARD"); continue;
		}
		res("GABRIEL");
	}
	return 0;
}

