#include <bits/stdc++.h>

using namespace std;

const int MAX_N = 111;
const int ITER = 10000;
const int MAX_M = 10;

vector<int> children[MAX_N];
string letters;
string words[MAX_M];

void print_answer(int case_id, const vector<double> &answer) {
  cout << "Case #" << case_id << ": ";

  for (double x : answer) {
    cout << x << " ";
  }
  cout << "\n";
}

double get_random_double() {
  return 1.0 * rand() / RAND_MAX;
}

string random_merge(const string &a, const string &b) {
  int n = a.size() + b.size();
  int k = a.size();

  int ptr_a = 0;
  int ptr_b = 0;

  string result = "";
  while (n > 0) {
    if (get_random_double() < 1.0 * k / n) {
      result += a[ptr_a];
      k -= 1;
      ptr_a += 1;
    } else {
      result += b[ptr_b];
      ptr_b += 1;
    }

    n -= 1;
  }

  return result;
}

string get_random_string(int v) {
  string result = "";
  for (int u : children[v]) {
    result = random_merge(result, get_random_string(u));
  }

  result = letters[v] + result;
  return result;
}

void solve(int case_id) {
  int n; cin >> n;
  for (int i = 0; i <= n; i++) {
    children[i].clear();
  }

  for (int i = 1; i <= n; i++) {
    int p; cin >> p;
    children[p].push_back(i);
  }

  cin >> letters;
  letters = "*" + letters;
  int m; cin >> m;
  for (int i = 0; i < m; i++) {
    cin >> words[i];
  }

  vector<double> answer(m);
  for (int it = 0; it < ITER; it++) {
    string s = get_random_string(0);

    for (int i = 0; i < m; i++) {
      if (s.find(words[i]) != string::npos) {
        answer[i] += 1;
      }
    }
  }

  for (int i = 0; i < m; i++) {
    answer[i] /= ITER;
  }

  print_answer(case_id, answer);
}

int main() {
  srand(time(NULL));
  cout << fixed << setprecision(10);
  cerr << fixed << setprecision(10);

  int cases; cin >> cases;

  for (int i = 1; i <= cases; i++) {
    solve(i);
  }

  return 0;
}