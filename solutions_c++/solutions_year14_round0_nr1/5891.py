#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <iomanip>
#include <iterator>

using namespace std;

#define TWO(x) (x)*(x)
#define MAX(x,y) {if(x<(y)) x=(y);}
#define MIN(x,y) {if(x>(y)) x=(y);}
#define ALL(x) (x).begin(), (x).end()

int arr1[4][4];
int arr2[4][4];
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  
  int tc;
  cin >> tc;
  int first;
  int second;
  
  for(int t=0;t<tc;++t) {
    cin >> first;
    --first;
    for(int i = 0; i < 4; ++i) 
      for(int j = 0; j < 4; ++j)
        cin >> arr1[i][j];
    cin >> second;
    --second;
    for(int i = 0; i < 4; ++i) 
      for(int j = 0; j < 4; ++j)
        cin >> arr2[i][j];
    
    int cc = 0;
    int lasteq = -1;
    for(int i = 0; i < 4; ++i) 
      for(int j = 0; j < 4; ++ j)  {
        if(arr2[second][j] == arr1[first][i]) {
          ++cc;
          lasteq = arr1[first][i];
        }
      }
    cout << "Case #" << t + 1 << ": ";
    if(cc==0) 
      cout << "Volunteer cheated!" << endl;
    else if(cc==1)
      cout << lasteq << endl;
    else 
      cout << "Bad magician!" << endl;
  }
  return 0;
}


