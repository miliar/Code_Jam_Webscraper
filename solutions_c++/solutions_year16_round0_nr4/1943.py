#include<bits/stdc++.h>
using namespace std;
#define IO ios_base::sync_with_stdio(false);cin.tie(NULL);

#define endl '\n'
#define D(x) cout << #x << " = " << (x) << endl;

int main(){ IO;
  int t;
  cin >> t;

  for(int ncase = 1; ncase <= t; ++ncase){
    cout << "Case #" << ncase << ":";
    
    int k, c, s;
    cin >> k >> c >> s;

    long long b = 1;
    for(int i = 1; i < c; ++i) b *= k;
    
    for(int i = 0; i < k; ++i){
      long long index = i * b + 1;
      cout << " " << index;
    }
    cout << endl;
  }

  return 0;
}
