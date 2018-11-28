#define _CRT_SECURE_NO_WARNINGS
#include <string>
#include <vector>
#include <algorithm>
#include <numeric>
#include <set>
#include <map>
#include <queue>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <cstring>
#include <cctype>
#include <cassert>
#define rep(i,n) for(int (i)=0;(i)<(int)(n);++(i))
#define rer(i,l,u) for(int (i)=(int)(l);(i)<=(int)(u);++(i))
#define reu(i,l,u) for(int (i)=(int)(l);(i)<(int)(u);++(i))
#if defined(_MSC_VER) || __cplusplus > 199711L
#define aut(r,v) auto r = (v)
#else
#define aut(r,v) typeof(v) r = (v)
#endif
#define each(it,o) for(aut(it, (o).begin()); it != (o).end(); ++ it)
#define all(o) (o).begin(), (o).end()
#define pb(x) push_back(x)
#define mp(x,y) make_pair((x),(y))
#define mset(m,v) memset(m,v,sizeof(m))
#define INF 0x3f3f3f3f
#define INFL 0x3f3f3f3f3f3f3f3fLL
using namespace std;
typedef vector<int> vi; typedef pair<int,int> pii; typedef vector<pair<int,int> > vpii;
typedef long long ll; typedef vector<long long> vl; typedef pair<long long,long long> pll; typedef vector<pair<long long,long long> > vpll;
typedef vector<string> vs; typedef long double ld;
template<typename T, typename U> inline void amin(T &x, U y) { if(y < x) x = y; }
template<typename T, typename U> inline void amax(T &x, U y) { if(x < y) x = y; }

int N;
int segt[1024*2*2];
void add(int id, int left, int right, int i) {
	if(left > i || right < i) return;
	if(left == right && left == i) {
		segt[id]=1;
		return;
	}
	int mid = (left + right) / 2;
	add(id*2+1, left, mid, i);
	add(id*2+2, mid+1, right, i);
	segt[id] = segt[id*2+1] + segt[id*2+2];
}
int sum(int id,int left,int right,int l,int r) {
	if(left > r || right < l) return 0;
	if(l <= left && r >= right) return segt[id];
	int mid = (left+right)/2;
	return sum(id*2+1,left,mid,l,r)+sum(id*2+2,mid+1,right,l,r);
}


int A[1000];
int main() {
	int T;
	scanf("%d", &T);
	rep(ii, T) {
		scanf("%d", &N);
		rep(i, N) scanf("%d", &A[i]);
		mset(segt, 0);
		vpii v;
		rep(i, N) v.pb(mp(-A[i], i+1));
		sort(all(v));
		long long sol = 0;
		int i=0;
		while(i < N) {
			int t = -v[i].first;
			int j = i;
			while(i < N) {
				if(-v[i].first!=t) break;
				sol += min(sum(0,1,N,1,v[i].second),sum(0,1,N,v[i].second,N));
				i ++;
			}
			while(j < i) {
				add(0,1,N,v[j].second);
				j ++;
			}
		}
		printf("Case #%d: %lld\n", ii+1, sol);
	}
	return 0;
}
