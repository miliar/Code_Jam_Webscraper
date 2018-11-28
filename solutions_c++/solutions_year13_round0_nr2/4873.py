//In the Name of God
#include <iostream>
#include <vector>
#include <cstring>
#include <string>
#include <algorithm>

using namespace std;

const int maxn = 100 + 10;
int t , n , m , x[maxn] , y[maxn] , a[maxn][maxn];

bool f(){
  memset(x , 0 , sizeof x);
  memset(y , 0 , sizeof y);
  for(int i = 0 ; i < n ; i++)
    for(int j = 0 ; j < m ; j++){
      x[i] = max(x[i] , a[i][j]);
      y[j] = max(y[j] , a[i][j]);
    }
  for(int i = 0 ; i < n ; i++)
    for(int j = 0 ; j < m ; j++)
      if(a[i][j] < x[i] && a[i][j] < y[j])
	return false;
  return true;
}

int main(){
  cin >> t;
  for(int z = 0 ; z < t ; z++){
    cin >> n >> m;
    for(int i = 0 ; i < n ; i++)
      for(int j = 0 ; j < m ; j++)
	cin >> a[i][j];
    cout << "Case #" << z + 1 << ": ";
    if(f())
      cout << "YES" << endl;
    else
      cout << "NO" << endl;
  }
  return 0;
}
