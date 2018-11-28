#include <iostream>
#include <stdio.h>
#include <queue>
#include <algorithm>
#include <vector>
#include <list>
#include <set>
#include <math.h>
using namespace std;

//trocar para 0 para desabilitar output
#if 1
#define DEBUG(x) cout << x << endl
#define PAUSE() cin.get(); cin.get()
#else
#define DEBUG(x)
#define PAUSE()
#endif

#define TRACE(x) DEBUG(#x << " = " << x)
#define DEBUGS() DEBUG("***************************")
#define MAX 101

int grass[MAX][MAX];
bool marked[MAX][MAX];
int n, m;

pair<int, int> nxtPos(const pair<int, int> &pos, int id){
  pair<int, int> aux;
  if (id%2){
    aux.second = pos.second;
    if (id == 1) aux.first = pos.first-1;
    else aux.first = pos.first+1;
    if (aux.first < 0) aux.first = 0;
    if (aux.first >= n) aux.first = n-1;
  }
  else{
    aux.first = pos.first;
    if (id == 2) aux.second = pos.second-1;
    else aux.second = pos.second+1;
    if (aux.second < 0) aux.second = 0;
    if (aux.second >= n) aux.second = m-1;
  }
  return aux;
}

void bfs(pair<int, int> pos, int v){
  queue< pair<int, int> > q;
  q.push(pos);
  while (!q.empty()){
    pair<int, int> actual = q.front();
    q.pop();
    if (marked[actual.first][actual.second]) continue;
    marked[actual.first][actual.second] = true;
    for (int i = 0; i < 4; ++i){
      pair<int, int> tmp = nxtPos(actual, i);
      if (!marked[tmp.first][tmp.second] && grass[tmp.first][tmp.second] == v)
	q.push(tmp);
    }
  }
}

bool run(){
  vector<bool> types(MAX, false);
  for (int i = 0; i < n; ++i)
    for (int j = 0; j < m; ++j)
      marked[i][j] = false;
  for (int i = 0; i < n; ++i){
    for (int j = 0; j < m; ++j){
      if (!marked[i][j]){
	if (types[grass[i][j]]) return false;
	types[grass[i][j]] = true;
	bfs(make_pair(i, j), grass[i][j]);
      }
    }
  }
  
  for (int i = 0; i < n; ++i)
    for (int j = 0; j < m; ++j)
      if (!marked[i][j]) return false;
  return true;
}

bool run2(){
  int master = 0;
  for (int i = 0; i < n; ++i)
    for (int j = 0; j < m; ++j)
      master = max(master, grass[i][j]);
  for (int i = 0; i < n; ++i){
    for (int j = 0; j < m; ++j){
      bool ok = true;
      if (master == grass[i][j]) continue;
      for (int k = 0; k < n; ++k)
	if (grass[i][j] < grass[k][j]) ok = false;
      if (!ok)
	for (int k = 0; k < m; ++k)
	  if (grass[i][j] < grass[i][k]) return false;
    }
  }
  return true;
}

int main(){
  int t, p = 0;
  cin >> t;
  while (t--){
    cin >> n >> m;
    for (int i = 0; i < n; ++i)
      for (int j = 0; j < m; ++j)
	cin >> grass[i][j];
    printf("Case #%d: ", ++p);
    if (run2()) puts("YES");
    else puts("NO");
  }
  return 0;
}
