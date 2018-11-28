#include <algorithm>
#include <iostream>
#include <random>
#include <string>
#include <vector>

using namespace std;

namespace {

const int kTrials = 10000;
mt19937_64 rng;

vector<int> merge(const vector<int> a, const vector<int> b) {
  vector<int> res;
  int na = a.size();
  int nb = b.size();
  while (na + nb > 0) {
    if (uniform_int_distribution<int>(0, na + nb - 1)(rng) < na) {
      res.push_back(a[--na]);
    } else {
      res.push_back(b[--nb]);
    }
  }
  reverse(res.begin(), res.end());
  return res;
}

vector<double> Solve(vector<int> req, string courses, vector<string> words) {
  const int N = req.size();
  const int M = words.size();
  vector<vector<int>> children(N + 1);
  for (int i = 0; i < N; ++i) {
    children[req[i]].push_back(i + 1);
  }
  function<vector<int>(int)> generate = [&](int n) {
    vector<int> res;
    for (int c : children[n]) {
      res = merge(res, generate(c));
    }
    res.insert(res.begin(), n);
    return res;
  };
  vector<int> counts(M);
  for (int i = 0; i < kTrials; ++i) {
    vector<int> seq = generate(0);
    string hat;
    for (int i = 1; i <= N; ++i) hat += courses[seq[i] - 1];
    for (int i = 0; i < M; ++i) {
      counts[i] += hat.find(words[i]) != string::npos;
    }
  }
  vector<double> res;
  for (int i = 0; i < M; ++i) {
    res.push_back(1.0 * counts[i] / kTrials);
  }
  return res;
}

}

int main(void) {
  int T;
  cin >> T;
  for (int i = 1; i <= T; ++i) {
    int N;
    cin >> N;
    vector<int> req(N);
    for (int j = 0; j < N; ++j) cin >> req[j];
    string courses;
    cin >> courses;
    int M;
    cin >> M;
    vector<string> words(M);
    for (int j = 0; j < M; ++j) cin >> words[j];
    cout << "Case #" << i << ":";
    for (double p : Solve(req, courses, words)) cout << ' ' << p;
    cout << endl;
  }

  return 0;
}
