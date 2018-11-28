#include<stdio.h>
#include<algorithm>
#include<string>
#include<vector>
#include<queue>
#include<functional>

using namespace std;

typedef long long ll;
typedef pair<double,double> pdd;

const int MX = 105;
pdd D[105];

pdd merge(pdd X, pdd Y){ return pdd(X.first + Y.first, X.second + Y.second); }

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++){
		printf("Case #%d: ", t);
		int N;
		double V, X;
		scanf("%d%lf%lf", &N, &V, &X);
		for(int i = 1; i <= N; i++) scanf("%lf%lf", &D[i].second, &D[i].first);
		sort(D+1, D+N+1);
		double st = 0, en = 1e20, mi, mn, mx;
		for(int tt = 1; tt <= 300; tt++){
			pdd total = pdd(0,0);
			mi = (st+en)/2;
			for(int i = N; i >= 1; i--){
				if( total.second + D[i].second * mi <= V ) total = merge(total, pdd(D[i].first*D[i].second*mi, D[i].second*mi));
				else{
					double rem = V - total.second;
					total = merge(total, pdd(D[i].first*rem, rem) );
				}
			}
			mx = total.first;

			total = pdd(0,0);
			for(int i = 1; i <= N; i++){
				if( total.second + D[i].second * mi <= V ) total = merge(total, pdd(D[i].first*D[i].second*mi, D[i].second*mi));
				else{
					double rem = V - total.second;
					total = merge(total, pdd(D[i].first*rem, rem) );
				}
			}

			mn = total.first;
			if( mn/(X*V) <= 1 + 1e-12 && X*V/mx <= 1 + 1e-12 && abs(total.second - V) < 1e-6) en = mi;
			else st = mi;
		}
		if( en == 1e20 ) printf("IMPOSSIBLE\n");
		else printf("%.10lf\n", mi);
	}
	return 0;
}