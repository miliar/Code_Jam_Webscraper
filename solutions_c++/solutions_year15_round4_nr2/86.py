#include <bits/stdc++.h>

using namespace std;

#define rep(i, a, b) for(int i = (a); i < int(b); ++i)
#define rrep(i, a, b) for(int i = (a) - 1; i >= int(b); --i)
#define trav(it, v) for(typeof((v).begin()) it = (v).begin(); it != (v).end(); ++it)
#define all(v) (v).begin(), (v).end()
#define what_is(x) cerr << #x << " is " << x << endl;

typedef double fl;
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<pii> vpi;

double r[105], c[105];
double same;
vector<pair<double, double> > lov, hiv;

void solve(){
	lov.clear();
	hiv.clear();
	int N;
	double V, X;
	scanf("%d", &N);
	scanf("%lf%lf", &V, &X);
	bool hasSmaller=0, hasLarger=0;
	same=0;
	rep(i,0,N){
		scanf("%lf%lf", r+i, c+i);
		if(c[i] >= X)
			hasLarger=1;
		if(c[i] <= X)
			hasSmaller=1;
		if(c[i] == X){
			same += r[i];
			r[i]=0;
		}
		if(c[i] < X)
			lov.push_back(make_pair(c[i], r[i]));
		else
			hiv.push_back(make_pair(c[i], r[i]));
	}
	sort(lov.begin(), lov.end());
	sort(hiv.begin(), hiv.end());
	if(!hasLarger || !hasSmaller){
		puts("IMPOSSIBLE");
		return;
	}
	double lo=0, hi=1e15F;
	rep(iter,0,100){
		double mid=(lo+hi)/2;
		double need=V-same*mid;
		if(need <= 0){
			hi=mid;
			continue;
		}
		double down=0, up=0;
		rep(i,0,N){
			if(c[i] < X)
				down += (X-c[i])*mid*r[i];
			else
				up += (c[i]-X)*mid*r[i];
		}
		down=min(down, up);
		up=down;
		rrep(i,lov.size(),0){
			double V=mid*lov[i].second;
			if((X-lov[i].first)*V > down)
				V=down/(X-lov[i].first);
			down -= (X-lov[i].first)*V;
			need -= V;
		}
		rep(i,0,hiv.size()){
			double V=mid*hiv[i].second;
			if((hiv[i].first-X)*V > up)
				V=up/(hiv[i].first-X);
			up -= (hiv[i].first-X)*V;
			need -= V;
		}
		if(need < 0)
			hi=mid;
		else
			lo=mid;
	}
	printf("%.8lf\n", (lo+hi)/2);
}

int main(){
	int T;
	scanf("%d", &T);
	for(int t=1; t <= T; ++t){
		printf("Case #%d: ", t);
		solve();
	}
}
