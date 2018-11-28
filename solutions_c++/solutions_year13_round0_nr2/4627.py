#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<vector<int> > target;
vector<vector<int> > lawn;

void initLawn(){
  lawn.clear();
  for(int i = 0; i < target.size(); i++){
    vector<int> V;
    for(int j = 0; j < target[i].size(); j++){
      V.push_back(100);
    }
    lawn.push_back(V);
  }
}

int findColMaxHeight(int c){
  int maximum = 0;
  for(int i = 0; i < target[c].size(); i++)
    maximum = max(maximum, target[c][i]);
  return maximum;
}

int findRowMaxHeight(int r){
  int maximum = 0;
  for(int i = 0; i < target.size(); i++)
    maximum = max(maximum, target[i][r]);
  return maximum;
}

void cutColByHeight(int c, int h){
  for(int i = 0; i < lawn[c].size(); i++)
    lawn[c][i] = min(lawn[c][i], h);
}

void cutRowByHeight(int r, int h){
  for(int i = 0; i < lawn.size(); i++)
    lawn[i][r] = min(lawn[i][r], h);
}

bool ans(){
  initLawn();

  for(int i = 0; i < target.size(); i++)
    cutColByHeight(i, findColMaxHeight(i));
  for(int i = 0; i < target[0].size(); i++)
    cutRowByHeight(i, findRowMaxHeight(i));

  /*
  cout << "-----target-----" << endl;
  for(int i = 0; i < target.size(); i++){
    for(int j = 0; j < target[i].size(); j++)
      cout << target[i][j] << ' ';
    cout << endl;
  }
  cout << "-----lawn-----" << endl;
  for(int i = 0; i < lawn.size(); i++){
    for(int j = 0; j < lawn[i].size(); j++)
      cout << lawn[i][j] << ' ';
    cout << endl;
  }
  */

  bool f = 1;
  for(int i = 0; i < target.size() && f; i++)
    for(int j = 0; j < target[i].size() && f; j++)
      if(target[i][j] != lawn[i][j])
        f = 0;
  return f;
}

int main(){
  int T;
  cin >> T;

  for(int t = 0; t < T; t++){
    target.clear();
    int n, m;
    cin >> n >> m;
    for(int i = 0; i < n; i++){
      vector<int> V;
      for(int j = 0; j < m; j++){
        int a;
        cin >> a;
        V.push_back(a);
      }
      target.push_back(V);
    }

    cout << "Case #" << t + 1 << ": " << (ans() ? "YES" : "NO") << endl;
  }
  return 0;
}
