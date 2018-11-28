#include <cstring>
#include <iostream>
#include <set>
#include <vector>

#define CHK(state, idx) ((state) & (1 << (idx)))
#define SET(state, idx) ((state) | (1 << (idx)))

#define TYPES 201

using namespace std;

int keys[TYPES]; // current counts of keys
int req[200]; // key needed to open each chest
vector<int> contains[200]; // list of keys in each chest

//set<unsigned int> explored;
bool explored[1 << 20];
int k, n;

bool bfs(unsigned int state, vector<int>& solution) {
  if (state == (1 << n) - 1) return true;
  //explored.insert(state);
  explored[state] = true;

  for (int i = 0; i < n; ++i) {
    //if (!CHK(state, i) && !explored.count(SET(state, i)) && keys[req[i]] > 0) {
    if (!CHK(state, i) && !explored[SET(state, i)] && keys[req[i]] > 0) {
      solution.push_back(i);
      keys[req[i]]--;
      for (int j = 0; j < contains[i].size(); ++j) keys[contains[i][j]]++;
      if (bfs(SET(state, i), solution)) return true;
      solution.pop_back();
      keys[req[i]]++;
      for (int j = 0; j < contains[i].size(); ++j) keys[contains[i][j]]--;
    }
  }

  return false;
}

int main() {
  int t; cin >> t;
  for (int test = 1; test <= t; ++test) {
    cout << "Case #" << test << ":";
    cin >> k >> n;
    for (int i = 0; i < TYPES; ++i) keys[i] = 0;
    for (int i = 0; i < k; ++i) {
      int key; cin >> key;
      keys[key]++;
    }
    for (int i = 0; i < n; ++i) {
      int ti, ki; cin >> ti >> ki;
      req[i] = ti;
      contains[i].clear();
      for (int j = 0; j < ki; ++j) {
        int key; cin >> key;
        contains[i].push_back(key);
      }
    }

    for (int i = 0; i < (1 << 20); ++i) explored[i] = false;
    //explored.clear();
    vector<int> solution;
    if (bfs(0, solution)) {
      for (int i = 0; i < solution.size(); ++i) {
        cout << " " << (solution[i] + 1);
      }
      cout << endl;
    } else {
      cout << " IMPOSSIBLE" << endl;
    }
  }
  return 0;
}