/* Opgave: C */
// 7+8+7=22 includes
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <climits>
#include <cassert>

#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <list>
#include <set>
#include <map>
#include <string>

#include <iostream>
#include <sstream>
#include <utility>
#include <functional>
#include <limits>
#include <numeric>
#include <algorithm>

using namespace std;
int N;
int A[2000];
int B[20000];
int X[20000];
int RA[20];
int RB[20];
bool used[20];

bool dfs(int d) {
  if(d == N)
    return true;
  for(int i = 0; i < N; ++i) {
    if(used[i]) continue;
    used[i] = true;
    X[d] = i;
    RA[d] = RB[d] = 1;
    for(int j = 0; j < d; ++j)
      if(X[j] < X[d])
	RA[d] = max(RA[d], RA[j] + 1);
      else
	RB[d] = max(RB[d], RB[j] + 1);

    if(A[d] == RA[d] && dfs(d+1))
      return true;
    used[i] = false;
  }
  return false;
}
void doit (int t) {
  cin >> N;
  for(int i = 0; i < N; ++i)
    cin >> A[i];
  for(int j = 0; j < N; ++j)
    cin >> B[j];
  for(int i = 0; i < N; ++i) X[i] = -1;
  for(int i = 0; i < N; ++i) {
    int l = 1;
    for(int j = 0; j < N; ++j) {
      
      RA[j] = l;
      if(X[j] >= 0)l = max(l, A[j] + 1);
    }
    int r = 1;
    for(int j = N-1; j >= 0; --j) {
      
      RB[j] = r;
      if(X[j] >= 0) r = max(r, B[j] + 1);
    }
    vector<int> p;
    for(int j = 0; j < N; ++j) {
      //cout << j << " " << RA[j] << " " << RB[j] << endl;
      if(RA[j] == A[j] && RB[j] == B[j] && X[j] < 0) {
	
	p.push_back(j);
      }
    }

    vector<bool> usable(p.size(), true);
    for(int j = 0; j +1 < p.size() ; ++j) {
      if(A[p[j]] +1 > A[p[j+1]]) usable[j] = false;
      if(B[p[j+1]] + 1 > B[p[j]]) usable[j+1] = false;
    }
    for(int j = 0; j < p.size(); ++j) {
      if(usable[j]) {
	X[p[j]] = i;
	break;
      }
    }
  }
  cout << "Case #" << t << ":";
  for(int i = 0; i < N; ++i)
    cout << ' ' << (X[i] + 1);
  cout << endl;
}

int main () {
	int t;
	cin >> t; //scanf ("%d ", &t);
	for (int i = 0; i < t; i++) {
		doit (i+1);
	}
	return 0;
}
/* Opgave: C */
