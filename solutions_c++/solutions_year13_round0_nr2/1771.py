#include <iostream>
#include <algorithm>

using namespace std;

int h, w, data[100][100];

string solve(){
  for(int y=0;y<h;y++){
    for(int x=0;x<w;x++){
      bool f1, f2;
      f1 = f2 = false;
      for(int i=0;i<w;i++) if(data[y][x] < data[y][i]) f1 = true;
      for(int i=0;i<h;i++) if(data[y][x] < data[i][x]) f2 = true;
      if(f1 && f2) return "NO";
    }
  }
  return "YES";
}

main(){
  int T;
  cin >> T;
  for(int t=1;t<=T;t++){
    cin >> h >> w;
    for(int i=0;i<h;i++) for(int j=0;j<w;j++) cin >> data[i][j];
    cout << "Case #" << t << ": " << solve() << endl;
  }
}
