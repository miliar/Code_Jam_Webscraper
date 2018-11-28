#include <bits/extc++.h>
#include <iostream>

using namespace std;

//#define NDEBUG
#ifdef NDEBUG
#define DEBUG if (false)
#else
#define DEBUG if (true)
#endif
#define WRITE(x) DEBUG { cout << (x) << endl; }
#define WATCH(x) DEBUG { cout << #x << " = " << (x) << endl; }
//#define ALL(x) (x).begin(), (x).end()
//#define FORN(i, a, b) for(typeof(b) i = (a); i < (b); ++i)
//#define FOREACH(i, c) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)

typedef long long ll;

typedef vector<vector<pair<long long, int> > > Graph;

const long long INF = numeric_limits<long long>::max() / 100;

void dijkstra(Graph& g, int start, vector<long long>& distances){
	for(int i = 0; i < g.size(); i++) distances[i] = INF;
	distances[start] = 0;
	set<pair<long long, int> > q;
	q.insert(make_pair(distances[start], start));
	while(not q.empty()){
		int u = q.begin()->second;
		long long distance = q.begin()->first;
		q.erase(q.begin());
		
		for(int i = 0; i < g[u].size(); i++){
			int v = g[u][i].second;
			long long w = g[u][i].first;
			long long new_distance = distance + w;
			if(new_distance < distances[v]){
				if(distances[v] < INF){
					q.erase(make_pair(distances[v], v));
				}
				q.insert(make_pair(new_distance, v));
				distances[v] = new_distance;
			}
		}
	}
}

void print(vector<long long>& v){
	return;
	for(const auto& x : v) cout << x << ' ';
	cout << endl;
}

long long dst(long long x0a, long long y0a, long long x1a, long long y1a,
		long long x0b, long long y0b, long long x1b, long long y1b){
		vector<long long> xa, ya, xb, yb;
		xa.reserve(8);
		ya.reserve(8);
		xb.reserve(8);
		yb.reserve(8);
		long long dist = numeric_limits<long long>::max();
		xa.push_back(x0a);
		xa.push_back(x1a);
		ya.push_back(y0a);
		ya.push_back(y1a);
		xb.push_back(x0b);
		xb.push_back(x1b);
		yb.push_back(y0b);
		yb.push_back(y1b);
		
		for(const auto& x : xa){
			if(x >= x0b and x <= x1b){
				xb.push_back(x);
			}
		}
		for(const auto& y : ya){
			if(y >= y0b and y <= y1b){
				yb.push_back(y);
			}
		}
		for(const auto& x : xb){
			if(x >= x0a and x <= x1a){
				xa.push_back(x);
			}
		}
		for(const auto& y : yb){
			if(y >= y0a and y <= y1a){
				ya.push_back(y);
			}
		}

		print(xa);
		print(ya);
		print(xb);
		print(yb);

		for(const auto& xai : xa){
			for(const auto& yai : ya){
				for(const auto& xbi : xb){
					for(const auto& ybi : yb){
						dist = min(dist, max(llabs(xai - xbi), llabs(yai - ybi)));
					}
				}
			}
		}


		return dist - 1;


}

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int ntc;
	cin >> ntc;
	for(int tc = 0; tc < ntc; tc++){
		int w, h, b;
		cin >> w >> h >> b;
		b += 2;
		vector<int> x0(b), y0(b), x1(b), y1(b);
		x0[0] = -1;
		y0[0] = 0;
		x1[0] = -1;
		y1[0] = h - 1;
		x0[1] = w;
		y0[1] = 0;
		x1[1] = w;
		y1[1] = h - 1;
		for(int i = 2; i < b; i++){
			cin >> x0[i] >> y0[i] >> x1[i] >> y1[i];
		}
		vector<vector<pair<long long, int>>> g(b);
		for(int i = 0; i < b; i++){
			for(int j = 0; j < b; j++){
				if(i != j){
					g[i].push_back(make_pair(dst(x0[i], y0[i], x1[i], y1[i], x0[j], y0[j], x1[j], y1[j]), j));
					//cout << g[i].back().first << '\t';
				}else{
					//cout << "0\t";
				}
			}
			//cout << endl;
		}

		vector<long long> res(b);
		dijkstra(g, 0, res);
		long long sol = res[1];
		cout << "Case #" << (tc + 1) << ": " << sol << "\n";
	}
}
