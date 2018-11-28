#include <cstdio>
#include <set>
#include <algorithm>
#include <cstring>
#include <string>
#include <iostream>
#include <vector>

using namespace std;

int n, m;
string s[50];

vector <string> V[50];
int best, comb;

void calc (){
  int ret = 0;
  int curr = 0;

  for (int i = 0; i < n; ++i){
    if (V[i].size() == 0) return;
    set <string> S;

    for (int j = 0; j < V[i].size(); ++j)
      for (int k = 0; k < V[i][j].size(); ++k)
	S.insert(V[i][j].substr(0, k+1));

    curr += S.size()+1;
  }

  if (curr == best) ++comb;
  else if (curr > best){
    best = curr;
    comb = 1;
  }
  
}

void rek (int x){
  if (x == m){
    calc();
    return;
  }

  for (int i = 0; i < n; ++i){
    V[i].push_back(s[x]);
    rek(x+1);
    V[i].pop_back();
  }

}

void solve (){
  scanf("%d%d", &m, &n);
  best = comb = 0;
  for (int i = 0; i < m; ++i)
    cin >> s[i];

  rek(0);

  printf("%d %d\n", best, comb);
}

int main (void){
  int tc; scanf ("%d", &tc);
  for (int i = 1; i <= tc; ++i){
    printf("Case #%d: ", i);
    solve();
  }

  return 0;
}


