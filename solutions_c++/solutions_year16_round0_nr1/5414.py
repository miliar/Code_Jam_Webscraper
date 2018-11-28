#include<stdio.h>
#include<iostream>
#include<vector>
#include<cmath>
#include<algorithm>
#include<memory.h>
#include<map>
#include<set>
#include<queue>
#include<list>
#include<sstream>
#define mp make_pair
#define pb push_back      
#define F first
#define S second
#define SS stringstream
#define sqr(x) ((x)*(x))
#define m0(x) memset(x,0,sizeof(x))
#define m1(x) memset(x,63,sizeof(x))
#define CC(x) cout << (x) << endl
#define pw(x) (1ll<<(x))
#define M 1000000007
#define N 111111
using namespace std;
typedef pair<int,int> pt;

int code(long long x) {
	int ret = 0;
	while (x > 0) {
		ret |= pw(x % 10);
		x /= 10;
	}
	return ret;
}

int main(){
	freopen("1.in","r",stdin);	
	freopen("1.out","w",stdout);
	int T;
	cin >> T;
	for (int tt = 1; tt <= T; tt++) {
		long long s;
		
		cin >> s;
		if (s == 0) {
			cout << "Case #" << tt << ": INSOMNIA" << endl;
			continue;
		}


		int mask = 0;
		
		long long x = s;
		while (mask < pw(10) - 1) {
			mask |= code(x);
			x += s;
		}


		cout << "Case #" << tt << ": ";
		cout << x - s << endl;

	}
	return 0;
}