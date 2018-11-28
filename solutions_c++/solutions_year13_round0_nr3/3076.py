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
int main() {
	int t; cin >> t;
	int f_s[6] = {1, 4, 9, 121, 484, 676};
	for(int x = 1; x <= t; ++x){
		int a, b; cin >> a >> b;
		cout << "Case #" << x << ": " <<
		-(lower_bound(f_s, f_s + 5, a) - upper_bound(f_s, f_s + 5, b))
		<< endl;
	}
	return 0;
}
