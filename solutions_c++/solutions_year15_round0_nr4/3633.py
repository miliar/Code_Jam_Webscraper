#include <iostream>

using namespace std;

bool pre[4][4][4];

int main(){
   pre[1][1][1] = 1;
   pre[1][1][2] = 1;
   pre[1][1][3] = 1;
   pre[1][1][4] = 1;
   pre[1][2][2] = 1;
   pre[1][2][3] = 1;
   pre[1][2][4] = 1;
   pre[1][3][3] = 1;
   pre[1][3][4] = 1;
   pre[1][4][4] = 1;
   pre[2][1][1] = 0;
   pre[2][1][2] = 1;
   pre[2][1][3] = 0;
   pre[2][1][4] = 1;
   pre[2][2][2] = 1;
   pre[2][2][3] = 1;
   pre[2][2][4] = 1;
   pre[2][3][3] = 0;
   pre[2][3][4] = 1;
   pre[2][4][4] = 1;
   pre[3][1][1] = 0;
   pre[3][1][2] = 0;
   pre[3][1][3] = 0;
   pre[3][1][4] = 0;
   pre[3][2][2] = 0;
   pre[3][2][3] = 1;
   pre[3][2][4] = 0;
   pre[3][3][3] = 1;
   pre[3][3][4] = 1;
   pre[3][4][4] = 0;
   pre[4][1][1] = 0;
   pre[4][1][2] = 0;
   pre[4][1][3] = 0;
   pre[4][1][4] = 0;
   pre[4][2][2] = 0;
   pre[4][2][3] = 0;
   pre[4][2][4] = 0;
   pre[4][3][3] = 0;
   pre[4][3][4] = 1;
   pre[4][4][4] = 1;
   int t;
   cin >> t;
   for(int j=1; j<=t; j++){
      int x,r,c;
      cin >> x >> r >> c;
      if(pre[x][r][c] || pre[x][c][r])
        cout << "Case #" << j << ": " << "GABRIEL" << endl;
      else
        cout << "Case #" << j << ": " << "RICHARD" << endl;
   }
}
