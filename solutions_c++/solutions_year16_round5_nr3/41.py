#include <bits/stdc++.h>

using namespace std;

const int MAX_N = 1010;
const int ITER = 50;

int sq(int x) {
  return x * x;
}

struct Point {
  int x;
  int y;
  int z;

  int vx;
  int vy;
  int vz;

  int distance_to(const Point &another) const {
    int dx = x - another.x;
    int dy = y - another.y;
    int dz = z - another.z;

    return sq(dx) + sq(dy) + sq(dz);
  }
};

Point points[MAX_N];
bool is_visited[MAX_N];

void print_answer(int case_id, double answer) {
  cout << "Case #" << case_id << ": " << answer << "\n";
}

bool check(int n, double x) {
  memset(is_visited, false, sizeof(is_visited));
  queue<int> q;

  q.push(0);
  is_visited[0] = true;
  while (q.size()) {
    int v = q.front(); q.pop();

    for (int i = 0; i < n; i++) {
      if (is_visited[i] || x * x < points[v].distance_to(points[i])) {
        continue;
      }

      is_visited[i] = true;
      q.push(i);
    }
  }

  return is_visited[1];
}

void solve(int case_id) {
  int n, s; cin >> n >> s;
  for (int i = 0; i < n; i++) {
    Point &point = points[i];
    cin >> point.x >> point.y >> point.z >> point.vx >> point.vy >> point.vz;
  }

  double left = 0.0;
  double right = 3000.0;

  for (int it = 0; it < ITER; it++) {
    double middle = (left + right) / 2.0;

    if (check(n, middle)) {
      right = middle;
    } else {
      left = middle;
    }
  }

  print_answer(case_id, left);
}

int main() {
  cout << fixed << setprecision(10);
  cout << fixed << setprecision(10);

  int cases; cin >> cases;

  for (int i = 1; i <= cases; i++) {
    solve(i);
  }

  return 0;
}