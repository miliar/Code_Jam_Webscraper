// Enjoy your stay.

#include <bits/stdc++.h>

#define EPS 1e-9
#define INF 1070000000LL
#define MOD 1000000007LL
#define fir first
#define foreach(it,X) for(auto it=(X).begin();it!=(X).end();it++)
#define ite iterator
#define mp make_pair
#define mt make_tuple
#define rep(i,n) rep2(i,0,n)
#define rep2(i,m,n) for(int i=m;i<(n);i++)
#define pb push_back
#define sec second
#define sz(x) ((int)(x).size())

using namespace std;

typedef istringstream iss;
typedef long long ll;
typedef pair<ll,ll> pi;
typedef stringstream sst;
typedef vector<int> vi;

int c[88],N;
vi g[88];
int s1, s2;
int dist[88][88];

bool onway(int v1, int v2, int v){
	return dist[v1][v] + dist[v][v2] == dist[v1][v2];
}

int f(int p1, int p2, int turn, int pre1, int pre2, int stayed1, int stayed2){
	int canMove1, canMove2;
	int dist1 = dist[s1][p1], dist2 = dist[s2][p2];

	int res;

	if(turn == 1){
		res = -INF;
		rep(i,sz(g[p1])){
			int to = g[p1][i];
			if(to == pre1)continue;
			bool p1on = onway(s2, p2, p1);
			int toon = onway(s2, p2, to);
			if(p1on && toon) continue;
			int get = toon ? 0 : c[to];
			res = max(res, get + f(to, p2, 2, p1, pre2, 0, stayed2));
		}
		if(res == -INF){
			if(stayed2) res = 0;
			else res = f(p1, p2, 2, pre1, pre2, 1, stayed2);
		}
	}else{
		res = +INF;
		rep(i,sz(g[p2])){
			int to = g[p2][i];
			if(to == pre2)continue;
			bool p2on = onway(s1, p1, p2);
			int toon = onway(s1, p1, to);
			if(p2on && toon) continue;
			int get = toon ? 0 : -c[to];
			res = min(res, get + f(p1, to, 1, pre1, p2, stayed1, 0));
		}
		if(res == +INF){
			if(stayed1) res = 0;
			else res = f(p1, p2, 1, pre1, pre2, stayed1, 1);
		}
	}

	return res;
}

void main2(){
	cin>>N;
	rep(i,N)cin>>c[i];
	rep(i,N)rep(j,N)dist[i][j] = i == j ? 0 : INF;
	rep(i,N)g[i].clear();
	rep(i,N-1){
		int j;
		cin>>j;
		j--;
		g[i].pb(j);
		g[j].pb(i);
		dist[i][j] = dist[j][i] = 1;
	}
	rep(k,N)rep(i,N)rep(j,N)dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
	int ans = -INF;
	rep(i,N){
		s1 = i;
		int res = INF;
		rep(j,N){
			//cout<<i<<" "<<j<<endl;
			s2 = j;
			int init;
			if(i != j) init = c[i] - c[j];
			else init = c[i];
			res = min(res, init + f(s1,s2,1, -1, -1, 0, 0));
		}
		ans = max(ans, res);
	}
	cout<<ans<<endl;
}

int main(){
	cin.tie(0);
	ios_base::sync_with_stdio(0);
	
	
	
	int T;
	cin>>T;
	time_t start=clock(),pre=start;
	rep(tc,T){
		cout<<"Case #"<<tc+1<<": ";
		main2();
		time_t now=clock();
		cerr<<tc+1<<"/"<<T<<": "<<(double)(now-pre)/CLOCKS_PER_SEC<<endl;
		if(tc==T-1){
			cerr<<"Total: "<<(double)(now-start)/CLOCKS_PER_SEC<<endl;
			cerr<<"  Ave: "<<(double)(now-start)/CLOCKS_PER_SEC/T<<endl;
		}
		pre=now;
	}
}
