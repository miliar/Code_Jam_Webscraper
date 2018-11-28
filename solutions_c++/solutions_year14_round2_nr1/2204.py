#include <cstdio>
#include <vector>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

int N;
string x[100];
string y[100];
vector<int> z[100];

void reduce() 
{
  for(int i = 0; i < N; ++i) {
    char c = x[i][0];
    int  nb = 1;
    for(int j = 1; j < x[i].size(); ++j) {
      if(x[i][j] != c) {
        y[i].push_back(c);
        z[i].push_back(nb);
        c = x[i][j];
        nb = 1;
      } else {
        ++nb;
      }
    }
    y[i].push_back(c);
    z[i].push_back(nb);
  }
}

bool compare()
{
  for(int i = 1; i < N; ++i) {
    if(y[i] != y[0]) {
      return false;
    }
  }
  return true;
}

int getActions()
{
  int ss = 0;
  for(int i = 0; i < z[0].size(); ++i) {
    int t = 0;
    for(int j = 0; j < N; ++j) {
      t += z[j][i];
    }
    int m = static_cast<int>((static_cast<double>(t)/N + 0.5));
    int s = 0;
    for(int j = 0; j < N; ++j) {
      s += abs(z[j][i] - m);
    }
    ss += s;
  }
  return ss;
}

int main() {
  int T;
  cin >> T;
  for (int times = 1; times <= T; ++times) {
    cin >> N;
    for (int i = 0; i < N; ++i) {z[i].clear();x[i].clear();y[i].clear();};
    for (int i = 0; i < N; ++i) cin >> x[i];
    reduce();
    if(!compare()) {
      cout << "Case #" << times << ": " << "Fegla Won" << endl;
    } else {
      cout << "Case #" << times << ": " << getActions() << endl;
    }
  }
  return 0;
}
