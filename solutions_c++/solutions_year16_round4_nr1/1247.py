#include <iostream>
#include <vector>

using namespace std;

string generate_lineup(char type, int depth) {
  if (depth == 0) {
    string s = "";
    s += type;
    return s;
  }
  string s1, s2;
  if (type == 'R') {
    s1 = generate_lineup('R', depth - 1);
    s2 = generate_lineup('S', depth - 1);
  } else if (type == 'S') {
    s1 = generate_lineup('S', depth - 1);
    s2 = generate_lineup('P', depth - 1);
  } else { // type == 'P' 
    s1 = generate_lineup('P', depth - 1);
    s2 = generate_lineup('R', depth - 1);
  }
  if (s1 < s2) {
    return s1 + s2;
  }
  return s2 + s1;
}

int main() {
  int T; cin >> T;
  for (int test_case = 1; test_case <= T; test_case++) {
    printf("Case #%d: ", test_case);
    int N, R, P, S; cin >> N >> R >> P >> S;
    vector<int> C1(3), C2(3);
    C1[0] = 1; C1[1] = 0; C1[2] = 0;
    for (int i = 0; i < N; i++) {
      C2[0] = C1[0] + C1[1];
      C2[1] = C1[1] + C1[2];
      C2[2] = C1[2] + C1[0];
      C1 = C2;
    }
    if (C2[0] == R && C2[1] == P && C2[2] == S) {
      printf("%s\n", generate_lineup('R', N).c_str());
      continue;
    } 
    if (C2[0] == P && C2[1] == S && C2[2] == R) {
      printf("%s\n", generate_lineup('P', N).c_str());
      continue;
    }
    if (C2[0] == S && C2[1] == R && C2[2] == P) {
      printf("%s\n", generate_lineup('S', N).c_str());
      continue;
    }
    printf("IMPOSSIBLE\n");    
  }
  return 0;
}
