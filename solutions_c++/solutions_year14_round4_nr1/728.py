#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <list>
#include <queue>
using namespace std;

#define rep(i,N) for((i) = 0; (i) < (N); (i)++)
#define rab(i,a,b) for((i) = (a); (i) <= (b); (i)++)
#define Fi(N) rep(i,N)
#define Fj(N) rep(j,N)
#define Fk(N) rep(k,N)
#define sz(v) (v).size()
#define all(v) (v).begin(),(v).end()

int min_disc(vector<int> v, int X) {
	sort(all(v));
	int i,j;
	int c = 0;

	i = 0, j = sz(v) - 1;

	while(i < j) {
		if(v[i] + v[j] <= X) {
			i++,j--;
			c++;
		} else {
			j--;
			c++;
		}
	}
	if(i == j) c++;

	return c;
}

int main() {
	int T,cs;
	int N,X;
	int i,k;
	vector <int> v;

	scanf("%d",&T);

	rab(cs,1,T) {
		scanf("%d %d",&N,&X);
		v.clear();

		Fi(N) {
			scanf("%d",&k);
			v.push_back(k);
		}

		printf("Case #%d: %d\n",cs,min_disc(v,X));
	}

	return 0;
}
