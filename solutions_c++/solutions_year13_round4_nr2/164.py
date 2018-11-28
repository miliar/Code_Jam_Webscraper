#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<cstring>
#include<cmath>
#include<ctime>
#include<map>
#include<string>
#include<vector>
#include<set>

using namespace std;
#define For(i,l,r) for (lint i = l; i <= r; ++i)
#define Cor(i,l,r) for (lint i = l; i >= r; --i)
#define Fill(a,b) memset(a,b,sizeof(a))
#define FI first
#define SE second
#define MP make_pair
#define PII pair<int,int>
#define flt double
#define INF (0x3f3f3f3f)
#define MaxN 1020304
#define MaxNode 1020304
#define MD 1000000007
#define lint long long

lint n,m,p;
lint Cal(lint x,lint p,lint w) {
	if (!w) {
		lint t = x, tp = m;
		for (; t > 0; t = (t - 1) >> 1) {
			tp >>= 1;
			if (p <= tp) return false;
			p -= tp;
		}
		return true;
	} else {
		lint t = m - x - 1, tp = m;
		for (; t > 0; t = (t - 1ll) >> 1) {
			tp >>= 1;
		}
		return p >= tp;
	}
}

int main() {
	freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);
	lint T; cin >> T;
	For(TTT,1,T) { printf("Case #%I64d: ",TTT); cerr << TTT << endl;
		if(TTT==30){
			int z=TTT;
		}
		cin >> n >> p;
		m = 1ll << n;
		
		For(w,0,1) {
			lint l = 0, r = m - 1;
			while (l < r) {
				lint mid = l + r + 1 >> 1;
					if(w&&l==255){
						int z=l;
					}
				if (Cal(mid,p,w)) l = mid; else r = mid - 1;
			}
			cout << l << ' ';
		}
		puts("");
	}
	return 0;
}

