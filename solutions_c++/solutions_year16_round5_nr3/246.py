#include <bits/stdc++.h>
using namespace std;
#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define TRACE(x) cerr << "TRACE(" #x ")" << endl;
#define DEBUG(x) cerr << #x << " = " << (x) << endl;

typedef long long LL;
typedef unsigned long long ULL;
const int INF = 1000000000; const LL INFLL = LL(INF) * LL(INF);
template<class T> inline int size(const T&c) { return c.size(); }

struct Vector {
  double x,y,z;
  Vector(double xx=0.0, double yy=0.0, double zz=0.0) : x(xx), y(yy), z(zz) {}
};

inline Vector operator-(const Vector &a, const Vector &b) {
  return Vector(a.x-b.x, a.y-b.y, a.z-b.z);
}

inline double operator*(const Vector &a, const Vector &b) {
  return a.x*b.x + a.y*b.y + a.z*b.z;
}

struct Planet {
  Vector r0;
  Vector v;
};

struct TimeRange {
  bool infinite;
  bool always;
  double t0;
  double t1;
  TimeRange(bool alw) : infinite(true), always(alw), t0(0), t1(0) {
    if(alw) {
      t0 = -1e100;
      t1 = 1e100;
    } else {
      t0 = t1 = -1e100;
    }
  }
  TimeRange(double a, double b) : infinite(false), always(false), t0(a), t1(b) {}
};

struct Vertex {
  int planet;
  TimeRange timeRange;
  vector<int> neighbors; // planets
  Vertex() : planet(-1), timeRange(false) {}
  Vertex(int p, const TimeRange &tr) : planet(p), timeRange(tr) {}
};

int N;
vector<Planet> planets;
double sleepLimit;

void ReadInput() {
  cin >> N; planets.resize(N);
  cin >> sleepLimit;
  for(Planet &p : planets) {
    cin >> p.r0.x >> p.r0.y >> p.r0.z;
    cin >> p.v.x >> p.v.y >> p.v.z;
  }
}

vector<vector<TimeRange>> timeRanges;  // [source][destination] -> TimeRange
vector<Vertex> vertices;
double jumpLimit;

inline bool After(const Vertex &v, int planet, double t) {
  if(v.planet != planet) return v.planet > planet;
  return v.timeRange.infinite || v.timeRange.t1 >= t;
}

int FindVertex(int planet, double t) {
  int a = -1, b = size(vertices);
  while(b-a>1) {
    int c = (a+b)/2;
    if(After(vertices[c], planet, t)) b=c; else a=c;
  }
  if(b==size(vertices)) return -1;
  const Vertex &v = vertices[b];
  if(v.planet != planet) return -1;
  if(!v.timeRange.infinite && t + sleepLimit < v.timeRange.t0) return -1;
  return b;
}

TimeRange ComputeTimeRange(const Planet &A, const Planet &B) {
  Vector r0 = B.r0 - A.r0;
  Vector v = B.v - A.v;
  double a = v*v;
  double b = 2.0 * (r0*v);
  double c = r0 * r0 - jumpLimit * jumpLimit;
  if(a==0) {
    return TimeRange(c <= 0.0);
  } else {
    double delta = b*b - 4*a*c;
    if(delta<0) return TimeRange(false);
    double sdelta = sqrt(delta);
    return TimeRange((-b-sdelta)/(2*a), (-b+sdelta)/(2*a));
  }
}

void AddVertices(int planetIdx) {
  bool seenInfinity = false;
  vector<pair<int,TimeRange>> vec;
  REP(i, N) {
    const TimeRange &tr = timeRanges[planetIdx][i];
    if(tr.infinite) {
      if(tr.always) {
        vec.push_back({i, tr});
        seenInfinity = true;
      }
    } else {
      vec.push_back({i, tr});
    }
  }
  Vertex v;
  v.planet = planetIdx;
  if(seenInfinity) {
    v.timeRange = TimeRange(true);
    for (const auto &p : vec) {
      v.neighbors.push_back(p.first);
    }
    vertices.push_back(v);
  } else {
    sort(vec.begin(), vec.end(), [](const pair<int,TimeRange>&a, const pair<int,TimeRange> &b) {
        return a.second.t0 < b.second.t0;
        });
    v.timeRange = TimeRange(false);
    v.neighbors.clear();
    for(const auto &pp : vec) {
      if(v.timeRange.infinite) {
        v.neighbors.push_back(pp.first);
        v.timeRange = pp.second;
      }
      else if(pp.second.t0 > v.timeRange.t1 + sleepLimit) {
        vertices.push_back(v);
        v.neighbors.clear();
        v.neighbors.push_back(pp.first);
        v.timeRange = pp.second;
      } else {
        v.neighbors.push_back(pp.first);
        v.timeRange.t1 = max(v.timeRange.t1, pp.second.t1);
      }
    }
    if(!v.timeRange.infinite) vertices.push_back(v);
  }
}

struct Entry {
  int vertex;
  double t;
};

bool operator<(const Entry &a, const Entry &b) {
  return a.t > b.t;
}

bool Dijkstra() {
  int curTime = 0.0;
  int curVertex = FindVertex(0, curTime);
  if(curVertex == -1) return false;

  vector<char> done(size(vertices), false);
  priority_queue<Entry> que;
  que.push({curVertex, 0.0});
  while(!que.empty()) {
    Entry entry = que.top(); que.pop();
    curVertex = entry.vertex;
    curTime = entry.t;
    if(done[curVertex]) continue;
    done[curVertex] = true;

    const Vertex &v = vertices[curVertex];
    if(v.planet==1) return true;

    for(int p : v.neighbors) {
      const TimeRange &tr = timeRanges[v.planet][p];
      if(tr.infinite && !tr.always) continue;
      double tp = curTime;
      if(!tr.infinite) {
        if(curTime > tr.t1) continue;
        if(tr.t0 > tp) tp = tr.t0;
      }
      int v2 = FindVertex(p, tp);
      assert(v2 != -1);
      que.push(Entry{v2, tp});
    }
  }
  return false;
}

bool OK(double jumpLimit1) {
  jumpLimit = jumpLimit1;
  timeRanges.clear(); timeRanges.resize(N);
  REP(i, N) REP(j,N) {
    if(i!=j) {
      timeRanges[i].push_back(ComputeTimeRange(planets[i], planets[j]));
    } else {
      timeRanges[i].push_back(TimeRange(false));
    }
  }

  vertices.clear();
  REP(i,N) AddVertices(i);

  return Dijkstra();
}

double Calc() {
  double alpha = 0.0;
  double beta = 1.0;
  while(!OK(beta)) {
    alpha = beta; beta *= 2;
    if (beta > 1e10) return 17.0; // TODO
  }
  REP(i,40) {
    double gamma = (alpha+beta)/2;
    if(OK(gamma)) beta=gamma; else alpha=gamma;
  }
  return alpha;
}

int main(int argc, char **argv) {
  int ntc; cin >> ntc;
  FOR(tc,1,ntc) {
    ReadInput();
    if(argc==2 && tc!=atoi(argv[1])) continue;
    double res = Calc();
    printf("Case #%d: %.16e\n", tc, res);
  }
}

