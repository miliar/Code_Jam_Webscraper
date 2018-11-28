//============================================================================
// Name        : problems.cpp
// Author      :2shraaf
// Version     :1.0
// Copyright   : Your copyright notice
//============================================================================
#include <bits/stdc++.h>
#include <fstream>
#include <sstream>
#include<string>

using namespace std;

#define REP(i,n) for( (i)=0 ; (i)<(n) ; (i)++ )
#define rep(i,x,n) for( (i)=(x) ; (i)<(n) ; (i)++ )
#define REV(i,n) for( (i)=(n) ; (i)>=0 ; (i)-- )
#define FORIT(it,x) for( (it)=(x).begin() ; (it)!=(x).end() ; (it)++ )
#define foreach(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define rforeach(it,c) for(__typeof((c).rbegin()) it=(c).rbegin();it!=(c).rend();++it)
#define foreach2d(i, j, v) foreach(i,v) foreach(j,*i)
#define aull(x) (x).begin(),(x).end()
#define raull(x) (x).rbegin(),(x).rend()
#define SZ(x) ((int)(x).size())
#define mms(x,n,s) memset(x,n,sizeof(x)*s)
#define mp make_pair
#define pb push_back
#define NX next_permutation
#define UN(x) sort(aull(x)),x.erase(unique(aull(x)),x.end())
#define CV(x,n) count(aull(x),(n))
#define FIND(x,n) find(aull(x),(n))-(x).begin()
#define SET_DIFF(x,y,z) set_difference(aull(x) , aull(y) , back_inserter(z))
#define ACC(x) accumulate(aull(x),0)
#define PPC(x) __builtin_popcount(x)
#define LZ(x) __builtin_clz(x)
#define TZ(x) __builtin_ctz(x)
#define mxe(x) *max_element(aull(x))
#define mne(x) *min_element(aull(x))
#define low(x,i) lower_bound(aull(x),i)
#define upp(x,i) upper_bound(aull(x),i)
#define NXPOW2(x) (1ull << ((int)log2(x)+1))
#define PR(x) cout << #x << " = " << (x) << endl ;
template<typename T, typename U> inline void amin(T &x, U y) {
	if (y < x)
		x = y;
}
template<typename T, typename U> inline void amax(T &x, U y) {
	if (x < y)
		x = y;
}

typedef unsigned long long ull;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int> > vvi;
typedef pair<int, int> pii;
//int Ns = 5000 + 1;
//int check[5000 + 2];
//int prime[1000];
//void shieve() {
//  for (int i = 3; i * i <= Ns; i += 2) {
//      if (!check[i]) {
//          for (int j = i * i; j <= Ns; j += i)
//              check[j] = 1;
//      }
//  }
//  prime[0] = 2;
//  int j = 1;
//  for (int i = 3; i <= Ns; i += 2) {
//      if (!check[i]) {
//          prime[j++] = i;
//      }
//  }
//}
//int ans[1020 + 1];
//int res = 0;
//void fun() {
//  int i, x, j, count = 0;
//  for (i = 30; i <= 2664; i++) {
//      x = 0;
//      for (j = 0; prime[j] <= i; j++) {
//          if (i % prime[j] == 0)
//              x++;
//          if (x == 3) {
//              ans[count++] = i;
//              res++;
//              break;
//          }
//      }
//  }
//
//}
//ll mod(ll a, ll b) {
//  return (a % b + b) % b;
//}
int a[1000 + 1];

int main() {

//	int tc, t, n, ai;
//	scanf("%d", &t);
//	tc = t;
//
//	while (t-- != 0) {
//		for (int i = 0; i <= 1000; i++)
//			a[i] = 0;
//		memset(a, 0, sizeof a);
//		int res = 0;
//		scanf("%d", &n);
//		for (int i = 0; i < n; i++) {
//			scanf("%d", &ai);
//			a[ai]++;
//		}
//		for (int i = 1000; i >= 1; i--) {
//			int ind = i / 2;
//
//			if (a[i] >= i
//					|| (i % 2 == 0 && (a[ind] + (a[i] * 2)) >= ind
//							&& a[i] >= ind)
//					|| (i % 2 == 1 && (a[ind] + a[i]) >= ind && a[i] >= ind)
//					|| (i % 2 == 1 && (a[ind + 1] + a[i]) >= (ind + 1)
//							&& a[i] >= ind + 1)) {
//				res += i;
//				break;
//			} else {
//				if (a[i]) {
//					if (i % 2 == 0) {
//						ind = i / 2;
//						a[ind] += (a[i] * 2);
//					} else {
//						ind = i / 2;
//						a[ind] += a[i];
//						a[ind + 1] += a[i];
//					}
//					res += a[i];
//				}
//
//			}
//		}
//
//		printf("Case #%d: %d\n", (tc - t), res);
//	}

	int tc, t, r, c, x;
	string s;
	scanf("%d", &t);
	tc = t;
	bool b[5][5][5];
	memset(b, 0, sizeof b);

	b[2][1][2] = b[2][2][1] = b[2][1][4] = b[2][4][1] = b[2][2][2] = b[2][2][3] =
			b[2][3][2]=b[2][2][4]=b[2][4][2]=b[2][3][4]=b[2][4][3]=b[2][4][4] = true;
	b[3][2][3]=b[3][3][2]=b[3][3][4]=b[3][4][3]=b[3][3][3]=true;
	b[4][4][4]=b[4][4][3]=b[4][3][4]=true;



	while (t-- != 0) {
		memset(a, 0, sizeof a);
		int res = 0;
		scanf("%d %d %d", &x, &r, &c);
		if (b[x][r][c]||x==1)

			printf("Case #%d: GABRIEL\n", (tc - t));
		else
			printf("Case #%d: RICHARD\n", (tc - t));

	}

	return 0;
}
