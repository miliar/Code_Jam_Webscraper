#include <bits/stdc++.h>

using namespace std;

string WinnerLine(char winner, int n) {
  if (n == 0) {
    return string(1, winner);
  }

  if (winner == 'R') {
    string a = WinnerLine('R', n - 1);
    string b = WinnerLine('S', n - 1);
    if (a < b) {
      return a + b;
    } else {
      return b + a;
    }
  } else if (winner == 'P') {
    string a = WinnerLine('P', n - 1);
    string b = WinnerLine('R', n - 1);
    if (a < b) {
      return a + b;
    } else {
      return b + a;
    }
  } else {
    string a = WinnerLine('P', n - 1);
    string b = WinnerLine('S', n - 1);
    if (a < b) {
      return a + b;
    } else {
      return b + a;
    }
  }
}

bool Check(const string& S, int r, int p, int s) {
  for (char c : S) {
    if (c == 'R') {
      r--;
    } else if (c == 'P') {
      p--;
    } else {
      s--;
    }
  }

  return r == 0 && p == 0 && s == 0;
}

void Solve() {
  int N, R, P, S;
  cin >> N >> R >> P >> S;

  string res = "";

  string winners = "PRS";
  for (char winner : winners) {
    string winnerLine = WinnerLine(winner, N);
    if (!Check(winnerLine, R, P, S)) continue;
    if (res == "" || res > winnerLine) {
      res = winnerLine;
    }
  }

  if (res == "") {
    res = "IMPOSSIBLE";
  }

  cout << res;
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
