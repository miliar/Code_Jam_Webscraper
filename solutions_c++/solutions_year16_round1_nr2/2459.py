#include <bits/stdc++.h>

using namespace std;

int N;
vector<vector<int>> A;
vector<vector<int>> cands;
int D[60][60];

void Input() {
  cin >> N;
  A.clear(); A.resize(2 * N - 1);
  for (int i = 0; i < 2 * N - 1; i++) {
    A[i].resize(N);
    for (int j = 0; j < N; j++) {
      cin >> A[i][j];
    }
  }
}

bool Check(const vector<int>& H, const vector<int>& V) {
  memset(D, -1, sizeof(D));
  for (int x = 0; x < N; x++) {
    for (int i = 0; i < H.size(); i++) {
      if (H[i] == -1) continue;
      D[i][x] = A[H[i]][x];
      if (i > 0 && D[i - 1][x] >= D[i][x]) return false;
    }
  }
  for (int y = 0; y < N; y++) {
    for (int i = 0; i < V.size(); i++) {
      if (V[i] == -1) continue;
      if (D[y][i] != A[V[i]][y]) return false;
    }
  }
  return true;
}

void Solve() {
  vector<bool> used(N, false);
  cands.clear(); cands.resize(N);

  for (int i = 0; i < N; i++) {
    int smallest = 2510;
    int smallestCount = 0;
    int smallestIndices[2];
    // find smallest
    {
      for (int j = 0; j < 2 * N - 1; j++) {
        if (used[j]) continue;
        if (smallest == A[j][i]) {
          smallestCount++;
          smallestIndices[1] = j;
        } else if (A[j][i] < smallest) {
          smallest = A[j][i];
          smallestIndices[0] = j;
          smallestCount = 1;
        }
      }
    }

    for (int j = 0; j < smallestCount; j++) {
      used[smallestIndices[j]] = true;
      cands[i].push_back(smallestIndices[j]);
    }
    if (cands[i].size() == 1) cands[i].push_back(-1);
  }

  for (int i = 0; i < 1 << N; i++) {
    vector<int> H, V;
    bool vertical = false;
    int res = -1;
    for (int j = 0; j < N; j++) {
      if (i & 1 << j) {
        H.push_back(cands[j][0]);
        V.push_back(cands[j][1]);
        if (cands[j][1] == -1) {
          vertical = true;
          res = j;
        }
      } else {
        H.push_back(cands[j][1]);
        V.push_back(cands[j][0]);
        if (cands[j][1] == -1) {
          vertical = false;
          res = j;
        }
      }
    }

    if (Check(H, V)) {
      if (vertical) {
        for (int i = 0; i < N; i++) {
          printf("%d", D[i][res]);
          if (i < N) printf(" ");
        }
      } else {
        for (int i = 0; i < N; i++) {
          printf("%d", D[res][i]);
          if (i < N) printf(" ");
        }
      }
      break;
    }
  }
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
    inputFile  = "./input/B-small-attempt1.in";
    stdoutFile = "./output/B-small-attempt1.out";
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
    Input();
    Solve();
    printf("\n");

    fprintf(stderr, "Finished: #%d\n", test_case);
  }

  fprintf(stderr, "Finished all test cases\n");

  return 0;
}
