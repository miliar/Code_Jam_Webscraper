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

vector <int> S1,S2;

int g[10][10];

int main() {
	int T,cs;
	int k,i,j;

	scanf("%d",&T);

	rab(cs,1,T) {
		scanf("%d",&k);
		Fi(4) Fj(4) scanf("%d",&g[i][j]);
		S1.clear();
		Fj(4) S1.push_back(g[k-1][j]);

		scanf("%d",&k);
		Fi(4) Fj(4) scanf("%d",&g[i][j]);
		S2.clear();
		Fj(4) S2.push_back(g[k-1][j]);

		sort(S1.begin(),S1.end());
		sort(S2.begin(),S2.end());

		vector <int> common(4);
		vector<int>::iterator it = set_intersection(all(S1),all(S2),common.begin());
		common.resize(it - common.begin());

		printf("Case #%d: ",cs);
		if(common.size() == 0) {
			printf("Volunteer cheated!\n");
		} else if(common.size() > 1) {
			printf("Bad magician!\n"); 
		} else {
			printf("%d\n",common[0]);
		}
	}

	return 0;
}
