#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <ctime>
#include <cstdio>
#include <cstring>
#include <map>
#include <vector>
#include <set>
using namespace std;
#define pb push_back
#define mp make_pair
typedef double db;

typedef long long LL;
typedef unsigned int uint;
#define rep(i,n) for(int i=0;i<n;++i)
#define mp make_pair

const int MAXN = 11111;
const db EPS = 1e-9;
const db PI = acos(-1.0);
int sign(db x){return x < - EPS ? - 1 : x > EPS ; }
const int P = 1000002013;

typedef pair< pair< int ,int > , int > Node ;

Node S[ MAXN ];

bool sort_f( Node a, Node b) {
	return a.first.first < b.first.first;
}
bool sort_s( Node a, Node b) {
	return a.first.second < b.first.second;
}

int n, m ;

LL cost( LL d) {
	return ((2*(LL)n-d+1)*d/2) % P;
}

int MOD( LL a) {
	a %= P;
	return a<0?a+P:a;
}

pair<LL ,LL > L[MAXN],R[MAXN] ;

int main(){
	freopen("/Users/AekdyCoin/Desktop/A-small-attempt0 (1).in","r", stdin);
	freopen("/Users/AekdyCoin/Desktop/A-small-attempt0 (1).out","w", stdout);

	int T; cin >> T;
	for(int cas = 1; cas <= T; ++ cas) {
		cin >> n >> m;
		for(int i=0;i<m;++i) {
			cin >> S[i].first.first >> S[i].first.second >> S[i].second ;
		}
		sort( S, S + m);
		LL ori = 0, now = 0;
		for(int i=0;i<m;++i) {
			ori = (ori + cost(S[i].first.second - S[i].first.first)*S[i].second) % P;
		}
		for(int i = 0; i < m; ++ i ) {
			int hi = S[i].first.second;
			int j=i;
			for(;j<m;++j) {
				int l=S[j].first.first, r = S[j].first.second;
				if(l <= hi) {
					hi = max( hi, r );
				}else break;
			}
			int ii = --j;
			//cout << i <<" ::: " << j << endl;
			int l, r;
			l = r = 0;
			for(int k=i;k<=j;++k) {
				L[l++]=mp(S[k].first.first, S[k].second);
				R[r++]=mp(S[k].first.second, S[k].second);
			}
			sort(L,L+l); sort(R,R+r);

			int cl = r-1;
			for(int k=l-1;k>=0;--k) {
				while(cl > 0 && R[cl-1].first >= L[k].first) -- cl;
				int who = cl;
				while(L[k].second) {
					LL cnt = min(L[k].second , R[who].second);
					now = (now + cost(R[who].first - L[k].first) * cnt % P) % P;
					R[who].second -= cnt;
					who++;
					L[k].second -= cnt;
				}
			}
			i=ii;
		}
		//cout << ori <<" " << now << endl;
		printf("Case #%d: %d\n", cas , (int)MOD(ori - now));
	}
	return 0;
}

/*
5 2
2 5 1
1 2 2
 * */
