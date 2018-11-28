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

int n;
long long P, Q, R, S;
long long a[2000222];

int main(){
	freopen("1.in","r",stdin);	
	freopen("1.out","w",stdout);
	int T;
	cin >> T;
	for (int tt = 1; tt <= T; tt++) {
		cin >> n;
		cin >> P >> Q >> R >> S;
		for (int i = 0; i < n; i++) a[i] = ((i * P + Q) % R + S);
//		for (int i = 0; i < n; i++) s[i + 1] = s[i] + a[i];
		long long sum = 0;
		for (int i = 0; i < n; i++) sum += a[i];
		long long l = 0;
		long long r = 1e18;
		while (l < r) {
			long long mid = (l + r) / 2;
			long long s = 0;
			int t = 0;
			for (int i = 0; i < n; i++) {
				if (s + a[i] <= mid) s += a[i]; else {
					s = a[i];
					if (s > mid) t = 50;
					t++;
				}
			}
			if (t > 2) l = mid + 1; else r = mid;
		}

		cout << "Case #" << tt << ": ";
		long double ret = l / 1. / sum;
		ret = 1 - ret;
		cout.precision(20);
		cout << fixed << ret << endl;

	}
	return 0;
}