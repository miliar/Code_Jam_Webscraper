#include <bits/stdc++.h>

using namespace std;

int N, K;
double P[210];

unsigned Increment(unsigned a) {
  unsigned smallest = a & -a;
  unsigned ripple = a + smallest;
  unsigned ones = a ^ ripple;
  ones = (ones >> 2) / smallest;
  return ripple | ones;
}

double Prob(const vector<double>& set) {
  double res = 0.0;

  unsigned S = 0;
  for (int i = 0; i < K / 2; i++) S |= 1 << i;

  while (S < 1 << K) {
    assert(__builtin_popcount(S) == K / 2);
    double p = 1.0;
    for (int j = 0; j < K; j++) {
      if (S & 1 << j) {
        p *= set[j];
      } else {
        p *= 1.0 - set[j];
      }
    }
    res += p;

    S = Increment(S);
  }

  return res;
}

void Solve() {
  cin >> N >> K;
  for (int i = 0; i < N; i++) cin >> P[i];

  double res = 0.0;
  unsigned S = 0;
  for (int i = 0; i < K; i++) S |= 1 << i;

  while (S < 1 << N) {
    assert(__builtin_popcount(S) == K);
    vector<double> set;
    for (int j = 0; j < N; j++) {
      if (S & 1 << j) {
        set.push_back(P[j]);
      }
    }
    assert(set.size() == K);

    res = max(res, Prob(set));
    S = Increment(S);
  }

  cout << res;
}

int main(int argc, char **argv) {
  (void)argc;
  (void)argv;

  const string problem = "small"; // practice, small, large
  const bool redirectStdoutToFile = true;
  const bool redirectStderrToFile = true;

  string inputFile = "";
  string stdoutFile = "";
  string stderrFile = "./output/B.stderr";

  if (problem == "practice") {
    inputFile  = "./input/B-practice.in";
    stdoutFile = "./output/B-practice.out";
  } else if (problem == "small") {
    inputFile  = "./input/B-small-attempt3.in";
    stdoutFile = "./output/B-small-attempt3.out";
  } else if (problem == "large") {
    inputFile  = "./input/B-large.in";
    stdoutFile = "./output/B-large.out";
  }

  fprintf(stderr, "Read from input: %s\n", inputFile.c_str());
  if (redirectStdoutToFile) fprintf(stderr, "Redirect stdout: %s\n", stdoutFile.c_str());
  if (redirectStdoutToFile) fprintf(stderr, "Redirect stderr: %s\n", stderrFile.c_str());

  assert(freopen(inputFile.c_str(), "r", stdin) != nullptr);
  if (redirectStdoutToFile) freopen(stdoutFile.c_str(), "w", stdout);
  if (redirectStderrToFile) freopen(stderrFile.c_str(), "w", stderr);

  int T = 0;
  string line;
  {
    getline(cin, line);
    istringstream is(line);
    is >> T;
  }

  fprintf(stderr, "# of cases: %d\n", T);

  for (int test_case = 1; test_case <= T; ++test_case) {
    printf("Case #%d: ", test_case);
    Solve();
    printf("\n");

    fprintf(stderr, "Finished: #%d\n", test_case);
  }

  fprintf(stderr, "Finished all test cases\n");

  return 0;
}
