#include<iostream>
#include<vector>

using namespace std;

void input(vector<int>& v, int row){
  v.resize(4);
  for(int i = 0; i < 4; i++)
    for(int j = 0; j < 4; j++){
      int in;
      cin >> in;
      if(i == row-1) v[j] = in;
    }
}

int main(){
  int T;
  cin >> T;
  
  for(int tc = 0; tc < T; tc++){
    vector<int> cand[2];
    for(int i = 0; i < 2; i++){
      int n;
      cin >> n;
      input(cand[i], n);
    }
    vector<int> v;
    for(int i = 0; i < 4; i++)
      for(int j = 0; j < 4; j++)
	if(cand[0][i] == cand[1][j]) v.push_back(cand[0][i]);

    cout << "Case #" << tc+1 << ": ";
    if(v.size() == 0) cout << "Volunteer cheated!" << endl;
    if(v.size() == 1) cout << v[0] << endl;
    if(v.size() >= 2) cout << "Bad magician!" << endl;
  }
  return 0;
}
