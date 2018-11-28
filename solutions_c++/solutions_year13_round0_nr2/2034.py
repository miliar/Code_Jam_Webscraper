#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#define loop(a,b,c) for (int a = b; a < c; a++)

using namespace std;

int main() {
  int n;
  cin >> n;
  loop(c,0,n) {
    int h,w;
    cin >> h >> w;
    bool dirs[h][w][4];
    int map[h][w];
    loop (i,0,h) {
      loop (j,0,w) {
        cin >> map[i][j];
        loop(k,0,4) { dirs[i][j][k] = true; }
      }
    }
    loop (i,0,h) {
      int max[4] = {0,0,0,0};
      loop (j,0,w) {
        if (max[0] > map[i][j]) { dirs[i][j][0] = false; }
        else max[0] = map[i][j];
        if (max[2] > map[i][w-1-j]) { dirs[i][w-1-j][2] = false; }
        else max[2] = map[i][w-1-j];
      }
    }
    loop (i,0,w) {
      int max[4] = {0,0,0,0};
      loop (j,0,h) {
        if (max[1] > map[j][i]) { dirs[j][i][1] = false; }
        else max[1] = map[j][i];
        if (max[3] > map[h-1-j][i]) { dirs[h-1-j][i][3] = false; }
        else max[3] = map[h-1-j][i];
      }
    }
    bool doable = true;
    loop (i,0,h) {
      loop (j,0,w) {
        if (dirs[i][j][0] && dirs[i][j][2]) {}
        else if (dirs[i][j][1] && dirs[i][j][3]) {}
        else { doable = false; }
        //cout << dirs[i][j][0] << dirs[i][j][1] << dirs[i][j][2] << dirs[i][j][3] << " ";
      }
      //cout << "\n";
    }
    //cout << h << " " << w << "\n";
    loop (i,0,h) {
      loop (j,0,w) {
    //    cout << map[i][j] << " ";
      }
    //  cout << "\n";
    }
    cout << "Case #" << (c+1) << (doable ? ": YES\n" : ": NO\n");
  }
}
