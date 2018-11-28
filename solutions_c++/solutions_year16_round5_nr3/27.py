#include<queue>
#include<set>
#include<cmath>
#include<vector>
#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;

const int N = 1005;

int n;

int s;

int x[N], y[N], z[N], vx[N], vy[N], vz[N];

double sqr(double x) {
	return x * x;
}

double dis(int i, int j, double t) {
	int dx = x[i] - x[j], dy = y[i] - y[j], dz = z[i] - z[j],
		dvx = vx[i] - vx[j], dvy = vy[i] - vy[j], dvz = vz[i] - vz[j];
	return sqrt(sqr(dx + dvx * t) + sqr(dy + dvy * t) + sqr(dz + dvz * t));
}

pair<double, double> able[N][N];

const double INF = 1e100, EPS = 1e-9;

struct Event {
	double t;
	int u, v, flag;

	Event(double t, int u, int v, int flag) : t(t), u(u), v(v), flag(flag) {}

	bool operator < (const Event &that) const {
		return t < that.t;
	}
};

int dgr[N];

double last[N];

set<int> to[N];

double cur;

bool alive(int u) {
	if (dgr[u] == 0) {
		return last[u] + s + EPS > cur;
	} else {
		return last[u] > 0;
	}
}

int stamp, vis[N];

void markLive(int u) {
	queue<int> q;
	q.push(u);
	++stamp;
	vis[u] = stamp;
	while (q.size()) {
		int u = q.front();
		last[u] = INF;
		q.pop();
		for (set<int>::iterator it = to[u].begin(); it != to[u].end(); ++it) {
			int v = *it;
			if (vis[v] != stamp) {
				q.push(v);
				vis[v] = stamp;
			}
		}
	}
}

bool check(double bar) {
	for (int i = 0; i < n; ++i) {
		for (int j = i + 1; j < n; ++j) {
			int dx = x[i] - x[j], dy = y[i] - y[j], dz = z[i] - z[j],
				dvx = vx[i] - vx[j], dvy = vy[i] - vy[j], dvz = vz[i] - vz[j];
			if (dvx == 0 && dvy == 0 && dvz == 0) {
				//the edge does not change
				if (sqrt(sqr(dx) + sqr(dy) + sqr(dz)) <= bar) {
					able[i][j] = able[j][i] = make_pair(0, INF);
				} else {
					able[i][j] = able[j][i] = make_pair(-1, -1);
				}
			} else {
				if (dx * dvy - dy * dvx == 0 &&
					dy * dvz - dz * dvy == 0 &&
					dz * dvx - dx * dvz == 0) {
					//linear
					double A = sqrt(sqr(dvx) + sqr(dvy) + sqr(dvz)),
						   B = sqrt(sqr(dx) + sqr(dy) + sqr(dz));
					if (dx * dvx + dy * dvy + dz * dvz < 0) {
						//meet at some point
						double mt = B / A;
						if (B > bar) {
							able[i][j].first = able[j][i].first = (B - bar) / A;
						} else {
							able[i][j].first = able[j][i].first = 0;
						}
						able[i][j].second = able[j][i].second = mt + bar / A;
					} else {
						//does not meet
						if (B > bar) {
							//never
							able[i][j] = able[j][i] = make_pair(-1, -1);
						} else {
							able[i][j].first = able[j][i].first = 0;
							able[i][j].second = able[j][i].second = (bar - B) / A;
						}
					}
				} else {
					//quad
					double A = sqr(dvx) + sqr(dvy) + sqr(dvz),
						   B = 2 * dx * dvx + 2 * dy * dvy + 2 * dz * dvz,
						   C = sqr(dx) + sqr(dy) + sqr(dz);
					double BB = B / A, CC = (C - sqr(bar)) / A;
					if (sqr(BB) - 4 * CC >= 0) {
						double delta = sqrt(sqr(BB) - 4 * CC);
						double t1 = (-BB - delta) / 2, t2 = (-BB + delta) / 2;
						t1 = max(t1, 0.0);
						if (t1 < t2) {
							able[i][j] = able[j][i] = make_pair(t1, t2);
						} else {
							able[i][j] = able[j][i] = make_pair(-1, -1);
						}
					} else {
						able[i][j] = able[j][i] = make_pair(-1, -1);
					}
				}
			}
		}
	}
	vector<Event> evt;
	for (int i = 0; i < n; ++i) {
		for (int j = i + 1; j < n; ++j) {
			if (able[i][j].first < able[i][j].second) {
				evt.push_back(Event(able[i][j].first, i, j, 1));
				if (able[i][j].second < 1e99) {
					evt.push_back(Event(able[i][j].second, i, j, -1));
				}
			}
		}
	}
	for (int i = 0; i < n; ++i) {
		last[i] = -INF;
		dgr[i] = 0;
		to[i].clear();
	}
	last[0] = 0;
	sort(evt.begin(), evt.end());
	for (int i = 0; i < (int)evt.size(); ++i) {
		cur = evt[i].t;
		int u = evt[i].u, v = evt[i].v, type = evt[i].flag;
		if (type == 1) {
			bool result = alive(u) || alive(v);
			if (!result) {
				if (dgr[u] == 0) {
					last[u] = -INF;
				}
				if (dgr[v] == 0) {
					last[v] = -INF;
				}
			} else {
				if (dgr[u] == 0) {
					last[u] = INF;
				} else {
					if (!alive(u)) {
						markLive(u);
					}
				}
				if (dgr[v] == 0) {
					last[v] = INF;
				} else {
					if (!alive(v)) {
						markLive(v);
					}
				}
			}
			to[u].insert(v);
			to[v].insert(u);
			++dgr[u], ++dgr[v];
		} else {
			to[u].erase(v);
			to[v].erase(u);
			--dgr[u], --dgr[v];
			if (last[u] > 0 && dgr[u] == 0) {
				last[u] = cur;
			}
			if (last[v] > 0 && dgr[v] == 0) {
				last[v] = cur;
			}
		}
		if (alive(1)) {
			return true;
		}
	}
	return false;
}

int main() {
	int T;
	scanf("%d", &T);
	while (T--) {
		static int id = 0;
		printf("Case #%d: ", ++id);
		scanf("%d%d", &n, &s);
		for (int i = 0; i < n; ++i) {
			scanf("%d%d%d%d%d%d", x + i, y + i, z + i, vx + i, vy + i, vz + i);
		}
		double l = 0, r = dis(0, 1, 0);
		cerr << id << endl;
		for (int i = 0; i < 40; ++i) {
			double m = (l + r) / 2;
			if (check(m)) {
				r = m;
			} else {
				l = m;
			}
		}
		printf("%.12f\n", (l + r) / 2);
	}
	return 0;
}
