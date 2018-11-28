#include <cmath>

#include <iostream>
#include <queue>
#include <tuple>
#include <vector>

using namespace std;

struct Vector3D {
  long long x, y, z;

};

long long distanceSquare(const Vector3D& lhs, const Vector3D& rhs) {
  long long dx = lhs.x - rhs.x;
  long long dy = lhs.y - rhs.y;
  long long dz = lhs.z - rhs.z;
  return dx * dx + dy * dy + dz * dz;
}

void solve() {
  int n, s;
  cin >> n >> s;
  vector < Vector3D > asteroids(n);
  for(int i = 0; i < n; ++i){
    int tmp;
    cin >> asteroids[i].x >> asteroids[i].y >> asteroids[i].z >> tmp >> tmp >> tmp;
  }
  priority_queue < tuple < long long, int > > q;
  q.push(make_tuple(0, 0));
  vector < long long > res(n, 1000000000);
  res[0] = 0;
  vector < int > used(n, 0);
  while(!q.empty()){
    long long distSqr;
    int v;
    tie(distSqr, v) = q.top();
    distSqr = -distSqr;
    q.pop();
    if(used[v]) continue;
    used[v] = 1;
    for(int i = 0; i < n; ++i){
      long long newDistSqr = max(distSqr, distanceSquare(asteroids[v], asteroids[i]));
      if(newDistSqr < res[i]){
        q.push(make_tuple(-newDistSqr, i));
        res[i] = newDistSqr;
      }
    }
  }
  cout << sqrt(res[1]) << endl;
}

int main() {
  cout.precision(12);
  int tests;
  cin >> tests;
  for(int test = 1; test <= tests; ++test){
    cout << "Case #" << test << ": ";
    solve();
  }
}
