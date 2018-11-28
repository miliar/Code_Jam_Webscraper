#include <cstdlib>
#include <iostream>
#include <bitset>
using namespace std;

int main(void) {
   long t;
   cin >> t ;
   for (long j = 1 ; j <= t ; j++) {
         int n, m;
         cin >> n >> m;
         bool ok = true;
         bool arr[n][m]; // = new bool[n][m];
         for (int i = 0; i < n; i++) {
              for (int k = 0; k < m ;k++) {
                  int v;
                  cin >> v;
                  arr[i][k] = (v==1);
              }
         }
         for (int i = 0; i < n; i++) {
              for (int k = 0; k < m ;k++) {
                  if (arr[i][k]) {
                        bool xok = true;
                        bool yok = true;
			for (int x = 0; x < m ; x++) {
                               xok = xok && arr[i][x];
                        }
			for (int y = 0; y < n ; y++) {
                               yok = yok && arr[y][k];
                        }
                        if ((!xok) && (!yok)) {
                              ok = false;
                              break;
                        }
                  }
              }
         }
   cout << "Case #" << j << ": " << (ok ? "YES" : "NO" ) << endl; 
   
   }
   //cout << "test" << endl;
   return 0;
}
