#include <bits/stdc++.h>

using namespace std;

const int MAX_N = 1010;

string S;

void Solve() {
  cin >> S;
  int N = S.size();

  string res = "";
  res += S[0];
  for (int i = 1; i < N; i++) {
    if (res[0] <= S[i]) {
      res = S[i] + res;
    } else {
      res = res + S[i];
    }
  }

  printf("%s", res.c_str());
}

int main(int argc, char **argv) {
  (void)argc;
  (void)argv;

  const string problem = "large"; // practice, small, large
  const bool redirectStdoutToFile = true;
  const bool redirectStderrToFile = true;

  string inputFile = "";
  string stdoutFile = "";
  string stderrFile = "./output/A.stderr";

  if (problem == "practice") {
    inputFile  = "./input/A-practice.in";
    stdoutFile = "./output/A-practice.out";
  } else if (problem == "small") {
    inputFile  = "./input/A-small-attempt0.in";
    stdoutFile = "./output/A-small-attempt0.out";
  } else if (problem == "large") {
    inputFile  = "./input/A-large.in";
    stdoutFile = "./output/A-large.out";
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
