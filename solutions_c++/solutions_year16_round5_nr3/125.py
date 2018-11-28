#include <bits/stdc++.h>

using namespace std;


template<class DistType>
using halfpijl = pair<DistType, unsigned>;

template<class DistType>
DistType dijkstra (unsigned s, unsigned t, 
		vector<vector<halfpijl<DistType>>> const& buren) {
	priority_queue <halfpijl<DistType>,
	                vector <halfpijl<DistType>>,
	                greater <halfpijl<DistType>> > q;
	
	vector<DistType> dist(buren.size(), numeric_limits<DistType>::max());

	dist[s] = 0;
	q.push ({dist[s], s});

	while (!q.empty ()) {
		auto cur = q.top ();
		q.pop ();

		if (dist[cur.second] < cur.first) { continue; }

		if (cur.second == t) {
			return dist[t];
		}

		for (auto it = buren[cur.second].begin ();
		     it != buren[cur.second].end ();
		     ++it) {
			if (max(cur.first, it->first) < dist[it->second]) {
				dist[it->second] = max(cur.first, it->first);
				q.push ({dist[it->second], it->second});
			}
		}
	}
	return dist[t];
}

double sqr(double x) { return x*x; }

void doCase(int t) {
	int N, S;
	cin >> N >> S;
	
	vector<double> X(N), Y(N), Z(N);
	vector<double> VX(N), VY(N), VZ(N);
	
	for (int i=0; i<N; i++) {
		cin >> X[i] >> Y[i] >> Z[i] >> VX[i] >> VY[i] >> VZ[i];
	}
	
	vector<vector<halfpijl<double>>> buren(N);
	for (int i=0; i<N; i++) {
		for (int j=0; j<N; j++) {
			if (i == j) continue;
			buren[i].push_back(make_pair(sqrt(sqr(X[i]-X[j])+sqr(Y[i]-Y[j])+sqr(Z[i]-Z[j])), j));
		}
	}
	
	cout << "Case #" << t << ": " << dijkstra(0, 1, buren) << endl;
}

int main() {
	int T;
	cin>> T;
	for (int i=1; i<=T; i++) doCase(i);
	return 0;
}
