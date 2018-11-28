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
#define N 2222
using namespace std;
typedef pair<int,int> pt;

int a[N], f[N];

int main(){
	freopen("1.in","r",stdin);	
	freopen("1.out","w",stdout);
	int T;
	cin >> T;
	for (int tt = 1; tt <= T; tt++) {
		int n;
		cin >> n;
		for (int i = 0; i < n; i++) cin >> a[i];
		m0(f);
		int ans = 0;
		for (int i = 0; i < n; i++) {
			int mi = 1e9 + 1, l = -1;
			for (int j = 0; j < n; j++) if (!f[j] && a[j] < mi) {
				mi = a[j];
				l = j;
			}
			f[l] = 1;
			int q1 = 0, q2 = 0;
			for (int j = 0; j < n; j++) if (!f[j]) {
				if (j < l) q1++; else q2++;
			}
			ans += min(q1, q2);
		}
		cout << "Case #" << tt << ": ";
		cout << ans << endl;

	}
	return 0;
}