#include <iostream>
#include <algorithm>
#include <vector>
#include <unordered_map>
#include <sstream>
#include <thread>
using namespace std;

vector<vector<string> > input;
vector<int> output;

void solve() {
  int n;
  cin >> n;

  cin.ignore();

  vector<string> v(n);
  for (int i = 0; i < n; ++i) getline(cin, v[i]);
  input.push_back(v);
}

void solve2(int xx) {
  vector<string> v = input[xx];
  unordered_map<string, int> id;
  for (int j = 0; j < 2; ++j) {
    stringstream ss(v[j]);
    string s;
    while (ss >> s) id[s] |= (j + 1);
  }
  int base = 0;
  for (unordered_map<string, int>::iterator it = id.begin(); it != id.end(); ++it) {
    if (it->second == 3) ++base;
  }

  int solution = 1e9;
  int n = v.size();
  vector<int> kk(1 << (n - 2));
  for (int i = 0; i < (1 << (n - 2)); ++i) {
    unordered_map<string, int> id2;
    int aux = base;
    for (int j = 2; j < n; ++j) {
      stringstream ss(v[j]);
      string s;
      while (ss >> s and aux < solution) {
        if (not id.count(s)) {
          if (id2[s] == 3) continue;

          if ((i >> (j - 2)) & 1) id2[s] |= 1;
          else id2[s] |= 2;

          if (id2[s] == 3) ++aux;
        }
        else {
          if ((i >> (j - 2)) & 1) {
            int x = 1;
            if (id[s] != 3 and (id[s] | x) == 3) {
              if (id2[s] != 3) ++aux;
              id2[s] = 3;
            }
          }
          else {
            int x = 2;
            if (id[s] != 3 and (id[s] | x) == 3) {
              if (id2[s] != 3) ++aux;
              id2[s] = 3;
            }
          }
        }
      }
    }

    solution = min(solution, aux);
  }

  output[xx] = solution;
}

void solve3(int i) {
  for (int j = i; j < output.size(); j += 4) solve2(j);
}

int main() {
  int casos;
  cin >> casos;
  output.resize(casos);
  for (int cas = 1; cas <= casos; ++cas) {
    solve();
  }

  thread t1(solve3, 0), t2(solve3, 1), t3(solve3, 2), t4(solve3, 3);
  t1.join();
  t2.join();
  t3.join();
  t4.join();

  for (int i = 1; i <= casos; ++i) {
    cout << "Case #" << i << ": " << output[i - 1] << endl;
  }
}
