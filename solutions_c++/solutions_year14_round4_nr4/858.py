/*
ID: Plagapong
LANG: C++
TASK: D
*/

#include<iostream>
#include<fstream>
#include<algorithm>
#include<string>
#include<set>
#define INF 999999999
#define MOD 1000000007

using namespace std;
int m, n;
char a[1002][102];

void preprocess() {
  // Preprocess
  
}

void clearVars() {
  // Clear variables
  for (int i = 0; i < 1002; i++) for (int j = 0; j < 102; j++) a[i][j] = 0;
}

////////////////////////////////////////////////////////////////

int worst = 0, worstCount = 0;
int assignments[10];
set<string> myset;

int counter(int u) {
  myset.clear();
  for (int i = 0; i < m; i++) {
    if (assignments[i] != u) continue;
    int j = 0;
    while (1) {
      myset.insert(string(a[i], j));
      if (!a[i][j]) break;
      j++;
    }
  }
  return myset.size();
}

void check() {
  // Must have at least one string in each server
  int count[10];
  for (int i = 0; i < n; i++) count[i] = 0;
  for (int i = 0; i < m; i++) count[assignments[i]]++;
  for (int i = 0; i < n; i++) if (!count[i]) return;
  //for (int i = 0; i < m; i++) { cout << assignments[i]; } cout << endl;
  // Count prefixes
  int answer = 0;
  for (int i = 0; i < n; i++) answer += counter(i);
  if (answer > worst) {
    worst = answer;
    worstCount = 1;
  } else if (answer == worst) {
    worstCount++;
  }
}

void dfs(int i) {
  if (i == m) {
    check();
    return;
  }
  for (int j = 0; j < n; j++) {
    assignments[i] = j;
    dfs(i+1);
  }
}

void naive() {
  worst = worstCount = 0;
  //assignments[0] = 0;
  //dfs(1);
  dfs(0);
  cout << worst << " " << (worstCount % MOD);
}

////////////////////////////////////////////////////////////////

void process() {
  // Code here!
  cin >> m >> n;
  for (int i = 0; i < m; i++) cin >> a[i];
  naive();
}

int main() {
  preprocess();
  int times;
  cin >> times;
  for (int i = 1; i <= times; i++) {
	cout << "Case #" << i << ": ";
	clearVars();
	process();
	cout << endl;
  }
  return 0;
}
