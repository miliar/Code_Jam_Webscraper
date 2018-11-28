#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string.h>
#include <iostream>

using namespace std;

int N, l;
vector<int> heights[99];

void solve() {
  cin >> N;
  l = 2*N-1;
  int numbers[2501];
  int a;
  for(int i = 0; i <= 2500; i++) numbers[i] = 0;
  for(int i = 0; i < l; i++) {
    for(int j = 0; j < N; j++) {
      cin >> a;
      numbers[a]++;
    }
  }
  vector<int> o;
  for(int i = 0; i <= 2500; i++) {
    if((numbers[i]%2)==1) o.push_back(i);
  }
  cout << o[0];
  for(int i = 1; i < N; i++) {
    cout << " " << o[i];
  }
  cout << endl;
}

int main() {
  int t;
  cin >> t;
  for(int i = 1; i <= t; i++) {
      cout << "Case #" << i << ": ";
      solve();
  }
  return 0;
}
