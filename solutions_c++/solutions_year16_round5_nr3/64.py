#include<bits/stdc++.h>
using namespace std;

typedef double ld;

const ld EPS = 1e-6;
const ld INF = 1e9;

const int MAXN = 3000;
const int MAXS = 100;

struct pt {
	ld x, y, z;
	pt(ld a, ld b, ld c) : x(a), y(b), z(c) {}
	pt(): x(0), y(0), z(0) {}
};

inline ld sq(ld a) { return a * a; }
inline ld norm(const pt &p) { return sq(p.x) + sq(p.y) + sq(p.z); }
inline ld abs(const pt &p) { return sqrt(norm(p)); }

pt operator + (const pt &a, const pt &b) {
	return pt(a.x + b.x, a.y + b.y, a.z + b.z);
}
pt operator - (const pt &a, const pt &b) {
	return pt(a.x - b.x, a.y - b.y, a.z - b.z);
}
pt operator * (const pt &a, const ld &v) {
	return pt(a.x * v, a.y * v, a.z * v);
}

pt cross(const pt &a, const pt &b) {
	return pt(
			a.y * b.z - a.z * b.y,
			a.z * b.x - a.x * b.z,
			a.x * b.y - a.y * b.x);
}

ld dot(const pt &a, const pt &b) {
	return a.x * b.x + a.y * b.y + a.z * b.z;
}

int N;
int S;
pt P[MAXN], V[MAXN];

ld M;

ld dist[MAXN];
bool vis[MAXN];
bool dijkstra() {
	for(int i = 0; i < N; i++) {
		dist[i] = INF;
		vis[i] = false;
	}
	dist[0] = 0;
	for(int z = 0; z < N; z++) {
		int cur = 0;
		while(vis[cur]) cur++;
		assert(cur < N);
		for(int i = 0; i < N; i++) {
			if(vis[i]) continue;
			if(dist[i] < dist[cur]) cur = i;
		}
		assert(!vis[cur]);

		if(dist[cur] >= INF) break;

		vis[cur] = true;

		ld l = dist[cur], r = dist[cur] + S;

		for(int nxt = 0; nxt < N; nxt++) {
			if(vis[nxt]) continue;
			pt p = P[nxt] - P[cur], v = V[nxt] - V[cur];
			if(norm(v) < EPS) {
				if(norm(p) <= M) {
					dist[nxt] = min(dist[nxt], dist[cur]);
				}
				continue;
			}

			ld md = - dot(p, v) / norm(v);
			ld sp = M - norm(cross(p, v)) / norm(v);
			if(sp < 0) continue;
			sp /= norm(v);
			sp = sqrt(sp);

			ld a = md - sp, b = md + sp;
			//cerr << norm(p + v * a) - M << '\n';
			//cerr << norm(p + v * b) - M << '\n';
			assert(abs(norm(p + v * a) - M) < EPS);
			assert(abs(norm(p + v * b) - M) < EPS);

			// find first point from l to r which is in a, b

			assert(l <= r);
			assert(a <= b);
			if(b < l || r < a) {
				continue;
			} else {
				dist[nxt] = min(dist[nxt], max(l, a));
			}
		}
	}
	return dist[1] < INF;
}

ld binary_search() {
	ld mi = 0, ma = 1e9;
	for(int i = 0; i < 200; i++) {
		M = (mi + ma) / 2;
		if(dijkstra()) {
			ma = M;
		} else {
			mi = M;
		}
	}
	return sqrt(ma);
}

int main() {
	ios_base::sync_with_stdio(0);
	int T; cin >> T;

	for(int case_num = 1; case_num <= T; case_num ++) {

		cin >> N >> S;
		for(int i = 0; i < N; i++) {
			cin >> P[i].x >> P[i].y >> P[i].z >> V[i].x >> V[i].y >> V[i].z;
		}

		ld res = binary_search();
		
		cout << "Case #" << case_num << ": ";
		cout << fixed << setprecision(7) << res << '\n';
	}

	return 0;
}
