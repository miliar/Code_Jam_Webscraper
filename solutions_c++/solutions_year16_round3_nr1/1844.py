#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

void foo(){
  int n, x;
  cin >> n;

  int f[26];
  int a[26];

  for(int i=0; i<n; i++){
    cin >> f[i];
    a[i] = i;
  }

  for(int i=1; i<n; i++)
    for(int j=0; j<n-i; j++)
      if(f[j]<f[j+1]){
        swap(f[j], f[j+1]);
        swap(a[j], a[j+1]);
      }

  while(true){
    if(f[0]==0) break;

    if(f[0]>f[1]){
      cout << char('A' + a[0]) << " ";
      --f[0];
      continue;
    }
    if(f[0]==f[1]){
      int j = 1;
      while(j+1<n && f[j+1]==f[j]) ++j;
      int t = 0;

      if(j%2==0){
        cout << char('A' + a[t]) << " ";
        --f[t];
        ++t;
      }
      while(true){
        if(t>j) break;
        cout << char('A' + a[t]);
        --f[t];
        ++t;
        cout << char('A' + a[t]);
        --f[t];
        ++t;
        cout << " "; 
      }
    }
    
  }
}
int main(){
  int T;
  cin >> T;
  for(int i=1; i<=T; i++){
    cout << "Case #" << i << ": ";
    foo();
    cout << endl;
  }
}