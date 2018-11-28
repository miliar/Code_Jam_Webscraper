#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
int n,m;
int f[111][111];
int h[111],w[111];
int main(void){
  int t;
  cin >> t;
  for(int k = 1; k <= t; k++){
    memset(h,0,sizeof(h));
    memset(w,0,sizeof(w));
    cin >> n >> m;
    for(int i = 0; i < n; i++){
      for(int j = 0; j < m; j++){
	cin >> f[i][j];
	h[i] = max(h[i],f[i][j]);
	w[j] = max(w[j],f[i][j]);
      }
    }
    bool flag = true;
    for(int i = 0; flag && i < n; i++){
      for(int j = 0; j < m; j++){
	if(h[i] > f[i][j] && w[j] > f[i][j]){
	  flag = false;
	  break;
	}
      }
    }
    cout << "Case #" << k << ": ";
    if(flag) cout << "YES" << endl;
    else cout << "NO" << endl;
  }
}
