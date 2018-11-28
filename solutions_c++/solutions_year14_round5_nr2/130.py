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
#include <limits>
#include <iterator>
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

int P, Q, N;
int H[100], G[100];
int memo[101][2001];

//この時点でtowerのターンとする
int rec(int i, int myshots) {
	int &r = memo[i][myshots];
	if(r != -1) return r;
	if(i == N) return r = 0;
	r = 0;
	//このモンスターを諦める
	int towerturns = (H[i] + Q - 1) / Q;
	amax(r, rec(i+1, myshots + towerturns));
	//このモンスターを自分が最後に撃つ。
	//shots回撃つ。前のターンまでにbefore回撃ってあるとする。
	for(int before = 0; before <= myshots; before ++) {
		int h = max(0, H[i] - before * P);
		//shots回交互にtower,herの順番で撃つ
		for(int shots = 0; ; shots ++) {
			int g = max(0, h - shots * (Q + P));
			if(g == 0) {
				if(shots == 0 || h - (shots-1) * (Q + P) > Q) {
					amax(r, G[i] + rec(i+1, myshots - before));
				}
				break;
			}
			int turns = (g + Q - 1) / Q;
			if(turns >= 2 && g - (turns - 1) * Q <= P) {
				amax(r, G[i] + rec(i+1, myshots - before + (turns - 2)));
			}
			if(g == 0) break;
		}
		if(h == 0) break;
	}
	return r;
}

int main() {
	int T;
	scanf("%d", &T);
	rep(ii, T) {
		scanf("%d%d%d", &P, &Q, &N);
		rep(i, N) scanf("%d%d", &H[i], &G[i]);
		mset(memo, -1);
		int ans = rec(0, 1);
		printf("Case #%d: %d\n", ii+1, ans);
	}
    return 0;
}
