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
typedef vector<ll> vi;

#define y0 y0_
#define y1 y1_

typedef pair<int,pi> tri;

int W,H,B;
int x0[1010],y0[1010],x1[1010],y1[1010];
//int a[510][110],dist[510][110];
int dist[1010];

void main2(){
	cin>>W>>H>>B;
	W+=2, H+=2;
	//memset(a,0,sizeof(a));
	rep(i,B){
		cin>>x0[i]>>y0[i]>>x1[i]>>y1[i];
		x0[i]++;y0[i]++;x1[i]++;y1[i]++;
		/*rep2(y,y0[i],y1[i]+1)rep2(x,x0[i],x1[i]+1){
			a[y][x] = 1;
		}*/
	}
	x0[B] = x1[B] = 0;
	y0[B] = 0, y1[B] = H-1;
	x0[B+1] = x1[B+1] = W-1;
	y0[B+1] = 0, y1[B+1] = H-1;
	/*rep(i,H){
		a[i][0] = a[i][W-1] = 1;
	}*/
	//priority_queue<tri,vector<tri>,greater<tri>> Q;
	priority_queue<pi,vector<pi>,greater<pi>> Q;
	//rep(i,H)rep(j,W) dist[i][j] = INF;
	rep(i,B+2)dist[i] = INF;
	/*rep(i,H){
		Q.push(mp(0,mp(i,0)));
		dist[i][0] = 0;
	}*/
	Q.push(mp(0,B));
	dist[B] = 0;
	while(sz(Q)){
		auto t = Q.top(); Q.pop();
		int d = t.fir, b = t.sec;//y = t.sec.fir, x = t.sec.sec;
		if(b == B+1){
			cout<<d<<endl;
			return;
		}
		rep(nb,B+2)if(b!=nb){
			int dy,dx;// = min(y0[i])
			int Y1 = min(y1[b], y1[nb]);
			int Y0 = max(y0[b], y0[nb]);
			int X1 = min(x1[b], x1[nb]);
			int X0 = max(x0[b], x0[nb]);
			if(Y1 >= Y0){
				dy = 0;
			}else{
				if(y1[nb] > y1[b]){
					dy = y0[nb] - y1[b];
				}else{
					dy = y0[b] - y1[nb];
				}
			}
			if(X1 >= X0){
				dx = 0;
			}else{
				if(x1[nb] > x1[b]){
					dx = x0[nb] - x1[b];
				}else{
					dx = x0[b] - x1[nb];
				}
			}
			assert(dy>=0 && dx>=0);
			int nd = d + max(dy, dx) - 1;
			if(nd < dist[nb]){
				//cout<<nb<<" "<<nd<<endl;
				dist[nb] = nd;
				Q.push(mp(nd,nb));
			}
		}
	}
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
