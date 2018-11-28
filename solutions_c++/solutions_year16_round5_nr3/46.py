#pragma warning(disable:4996)

#include <stdio.h>
#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <cmath>
#include <map>
#include <set>
#include <queue>
#include <complex>
#include <iterator>
#include <random>
#include <time.h>
#include <tuple>
#include <functional>
#include <list>
#include <limits.h>
#define mp make_pair
#define ni(x) scanf("%d", &(x))
#define nii(x,y) scanf("%d%d",&(x),&(y))
#define mul(x,y) ((ll)(x)*(y)%mod)
#define mtp make_tuple
#define add(x,y) ((ll)(x)+(y))%mod
#define F(i,n) for(int i = 0; i < n; i++)
#define FF(i,n) for(int i = 1; i <= n; i++)

using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
const int mod = 1000000007;
const int inf = 2012345678;
const double pi = 3.1415926535897932384626433832795;
//----------------------------------------------------------------------------//

const int N = 1000;
int par[N];
int cnt[N];
int totn;
int find(int i) {
	if (par[i] == i) return i;
	else return par[i] = find(par[i]);
}
void merge(int i, int j) {
	i = find(i); j = find(j);
	if (cnt[i] < cnt[j]) swap(i, j);
	par[j] = i;
	cnt[i] += cnt[j];
	totn--;
}

int coo[N][3];

int main() {
#ifndef __GNUG__
	freopen("C-small-attempt1.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T; ni(T);
	FF(tt, T) {
		printf("Case #%d: ", tt);
		//-----------------------Your code goes here------------------------//
		
		int n; ni(n);
		vector<tuple<int,int,int> > dists;
		totn = n;
		F(i, n) par[i] = i, cnt[i] = 1;
		int S; ni(S);
		F(i, n) {
			nii(coo[i][0], coo[i][1]); ni(coo[i][2]);
			int v, vv, vvv;
			nii(v, vv); ni(vvv);
		}
		F(i, n) {
			F(j, i) {
				int D = 0;
				F(k, 3) {
					int d = coo[i][k] - coo[j][k];
					D += d*d;
				}
				dists.emplace_back(D, i, j);
			}
		}
		sort(dists.begin(), dists.end());
		for (auto &x : dists) {
			merge(get<1>(x), get<2>(x));
			if (find(0)==find(1)) {
				printf("%.15f\n", sqrt(get<0>(x)));
				break;
			}
		}



		//------------------------------------------------------------------//
		fprintf(stderr, "Case %d complete\n", tt);
	}
	return 0;
}
