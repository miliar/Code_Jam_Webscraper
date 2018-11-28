#include<iostream>
#include<vector>

using namespace std;

int main() {
  int n; cin >> n;
  for(int i=1;i<=n;++i) {
    vector<string> sq(4);
    cin >> sq[0] >> sq[1] >> sq[2] >> sq[3];
    
    // 縦列を追加
    for(int j=0;j<4;++j) {
      string str = "";
      for(int k=0;k<4;++k) str += sq[k][j];
      sq.push_back(str);
    }
    // 斜め列を追加
    string str = "";
    str += sq[0][0];
    str += sq[1][1];
    str += sq[2][2];
    str += sq[3][3];
    sq.push_back(str);
    str = "";
    str += sq[3][0];
    str += sq[2][1];
    str += sq[1][2];
    str += sq[0][3];
    sq.push_back(str);
    
    int x=0,o=0;
    bool empty = false;
    // 調べる
    for(int j=0;j<10;++j) {
      if(sq[j].find('.')!=string::npos) {
        empty = true;
        continue;
      }
      if(sq[j].find('O')==string::npos) x++;
      else if(sq[j].find('X')==string::npos) o++;
    }
    
    cout << "Case #" << i << ": ";
    if(x==0 and o==0 and empty) cout << "Game has not completed";
    else if(x==0 and o>0) cout << "O won";
    else if(x>0 and o==0) cout << "X won";
    else cout << "Draw";
    cout << endl;
  }
  return 0;
}
