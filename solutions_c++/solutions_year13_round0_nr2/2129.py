#include<cstdio>
#include<cassert>

#include<vector>
#include<algorithm>
#include<string>
#include<iostream>

using namespace std;

class Lawnmower{
public:
  Lawnmower(){};

  Lawnmower(vector<vector<int> > grass1){
    grass = grass1;
  }

  bool CanCutGrass(){
    vector<int> col, lin;
    for(int i = 0; i < grass.size(); ++i)
      lin.push_back(0);
    for(int i = 0; i < grass[0].size(); ++i)
      col.push_back(0);

    for(int i = 0; i < grass.size(); ++i)
      for(int j = 0; j < grass[i].size(); ++j){
        lin[i] = max(lin[i], grass[i][j]);
        col[j] = max(col[j], grass[i][j]);
      }

    for(int i = 0; i < grass.size(); ++i)
      for(int j = 0; j < grass[i].size(); ++j)
        if(grass[i][j] < lin[i] && grass[i][j] < col[j])
          return false;

    return true;
  }

private:
  vector<vector<int> > grass;
};

int main(){
  assert(freopen("input.txt", "r", stdin));
  assert(freopen("output.txt", "w", stdout));

  int tests;

  cin >> tests;

  for(int i = 1; i <= tests; ++i){
    int n, m;
    cin >> n >> m;

    vector<vector<int> > grass;

    for(int j = 0; j < n; ++j){
      vector<int> line;

      for(int k = 0; k < m; ++k){
        int aux;
        cin >> aux;
        line.push_back(aux);
      }

      grass.push_back(line);
    }

    Lawnmower t(grass);

    if(t.CanCutGrass())
      cout << "Case #" << i << ": YES\n";
    else
      cout << "Case #" << i << ": NO\n";
  }

  return 0;
}
