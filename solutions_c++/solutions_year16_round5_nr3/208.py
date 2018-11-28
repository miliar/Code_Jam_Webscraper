#include <algorithm>
#include <cassert>
#include <cstring>
#include <iostream>
#include <random>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

typedef int64_t i64;
using namespace std;

struct Point {
  double x, y, z;
  Point(double x_, double y_, double z_) : x(x_), y(y_), z(z_) {}

  Point add(Point p) {
    return Point(x + p.x, y + p.y, z + p.z);
  }
  Point sub(Point p) {
    return Point(x - p.x, y - p.y, z - p.z);
  }
  double dot(Point p) {
    return x * p.x + y * p.y + z * p.z;
  }
  double distsq() {
    return dot(*this);
  }
  double dist() {
    return sqrt(dot(*this));
  }
  Point mult(double v) {
    return Point(x * v, y * v, z * v);
  }
};

double sq(double x) {
  return x*x;
}
constexpr double eps = 1e-9;

// todo: is this right?
pair<double, double> overlap(Point p1, Point v1, Point p2, Point v2, double dist) {
  Point p = p2.sub(p1);
  Point v = v2.sub(v1);
  if (v.distsq() < eps) {
    if (p.dist() <= dist)
      return make_pair(0, 1e12);
    else
      return make_pair(-1, -1);
  }

  double t = - p.dot(v) / v.distsq();
  Point c = p.add(v.mult(t));
  double d = c.dist();
  //cout << p.x << " " << p.y << " " << v.x <<" " << v.y << endl;
  //cout << "closest: " << d << " " << t << " " << c.x << " " << c.y << endl;
  if (d > dist)
    return make_pair(-1, -1);
  double x = sqrt(sq(dist) - sq(d));
  double t1 = t - x / v.dist();
  double t2 = t + x / v.dist();
  return make_pair(t1, t2);
}

struct Event {
  i64 a, b;
  double time;
  i64 enter;
  Event(i64 a_, i64 b_, double time_, i64 enter_) : a(a_), b(b_), time(time_), enter(enter_) {}

  bool operator< (const Event& e) const {
    return time < e.time;
  }
};

struct Interval {
  double start, end;
  i64 index;
  Interval(double start_, double end_, i64 index_) : start(start_), end(end_), index(index_) {}
  bool operator< (const Interval& i) const {
    return end < i.end;
  }
};

i64 find(i64 a, vector<i64>& parent) {
  if (parent[a] != a)
    parent[a] = find(parent[a], parent);
  return parent[a];
}
void merge(i64 a, i64 b, vector<i64>& parent) {
  i64 pa = find(a, parent);
  i64 pb = find(b, parent);
  parent[pa] = pb;
}

bool possible(i64 N, i64 S, const vector<Point>& P, const vector<Point>& V, double dist) {
  //cout << "possible: " << dist << endl;
  vector<vector<Event>> E(N);
  vector<vector<Interval>> I(N);
  vector<i64> parent;
  vector<i64> ends;
  for (i64 i = 0; i < N; i++) {
    for (i64 j = 0; j < N; j++) {
      if (i == j)
        continue;
      //cout << "test: " << i << " " << j << endl;
      auto p = overlap(P[i], V[i], P[j], V[j], dist);
      if (p.second < 0)
        continue;
      p.first = max(0.0, p.first);
      //cout << dist << " " << i << " " << j << " " << p.first << " " << p.second << endl;
      E[i].push_back(Event(i, j, p.first, 1));
      E[i].push_back(Event(i, j, p.second, -1));
    }
    E[i].push_back(Event(0, 0, 1e13, 1));
    sort(E[i].begin(), E[i].end());
    i64 overlap = 0;
    double start = -1;
    double prev = -1;
    for (const auto& e : E[i]) {
      if (e.enter == 1) {
        if (overlap == 0 && e.time - prev > S && prev != -1) {
          i64 p = parent.size();
          I[i].push_back(Interval(start, prev, p));
          //cout << "adding interval: " << start << " " << prev << " " << i << " " << p << endl;
          parent.push_back(p);
          if (i == 1) {
            //cout << "is an end: " << p << endl;
            ends.push_back(p);
          }
          start = e.time;
        }
        if (start == -1) {
          start = e.time;
        }
        overlap++;
      } else {
        overlap--;
      }
      prev = e.time;
    }
  }
  for (i64 i = 0; i < N; i++) {
    for (i64 j = 0; j < N; j++) {
      if (i == j)
        continue;
      auto p = overlap(P[i], V[i], P[j], V[j], dist);
      if (p.second < 0)
        continue;
      p.first = max(0.0, p.first);
      Interval i1(0, (p.first + p.second) / 2.0, 0);
      auto it1 = upper_bound(I[i].begin(), I[i].end(), i1);
      if (it1 == I[i].end() || i1.end < it1->start)
        continue;
      auto it2 = upper_bound(I[j].begin(), I[j].end(), i1);
      if (it2 == I[j].end() || i1.end < it2->start)
        continue;
      //cout << "merge: " << it1->index << " " << it2->index << endl;
      //cout << i1.start << " " << it1->start << " " << it1->end << " " << it2->start << " " << it2->end << endl;
      merge(it1->index, it2->index, parent);
    }
  }
  //cout << endl;
  for (const auto& i : I[0]) {
    if (i.start > S)
      continue;
    for (i64 e : ends) {
      //cout << "testing: " << e << " " << find(i.index, parent) << " " << find(e, parent) << endl;
      if (find(i.index, parent) == find(e, parent))
        return true;
    }
  }
  return false;
}

int main() {
  i64 Z;
  cin >> Z;
  for (i64 T = 1; T <= Z; T++) {
    i64 N, S;
    cin >> N >> S;
    vector<Point> P;
    vector<Point> V;
    for (i64 i = 0; i < N; i++) {
      i64 x, y, z;
      i64 vx, vy, vz;
      cin >> x >> y >> z >> vx >> vy >> vz;
      P.push_back(Point(x, y, z));
      V.push_back(Point(vx, vy, vz));
    }
    double low = 0;
    double high = 100000000000.0;
    for (i64 round = 0; round < 100; round++) {
      double mid = (low + high) / 2.0;
      if (possible(N, S, P, V, mid)) {
        high = mid;
      } else {
        low = mid;
      }
    }
    printf("Case #%lld: %.09f\n", T, low);
  }
  return 0;
}
