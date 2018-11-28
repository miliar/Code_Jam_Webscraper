#include <iostream>
#include <stdio.h>

using namespace std;
const int n = 4;

int a[11][11];

int cnt;
int b[11];

int main() {
  freopen("in.txt", "rt", stdin);
  freopen("out.txt", "wt", stdout);
  int T; cin >> T;
  for(int t = 1; t <= T; t++) {
    int m;
    cin >> m;
    m--;
    cnt = 0;
    for(int i = 0; i < n; i++) for(int j = 0; j < n; j++) cin >> a[i][j];
    for(int i = 0; i < n; i++)
      b[cnt++] = a[m][i];
    cin >> m;m--;
    for(int i = 0; i < n; i++) for(int j = 0; j < n; j++) cin >> a[i][j];
    
    int ans = 0, out;

    for(int i = 0; i < n; i++)      
      for(int j = 0; j < n; j++)
        if (b[j] == a[m][i])  
          ans++, out = b[j];
    cout << "Case #" << t << ": ";
    if(ans == 1) cout << out;
    if(ans > 1) cout << "Bad magician!";
    if(ans == 0) cout << "Volunteer cheated!";   
    cout << endl;
  } 
}