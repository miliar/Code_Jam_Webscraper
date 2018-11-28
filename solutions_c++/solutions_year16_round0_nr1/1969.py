#include<bits/stdc++.h>
using namespace std;
#define IO ios_base::sync_with_stdio(false);cin.tie(NULL);

#define endl '\n'
#define D(x) cout << #x << " = " << (x) << endl;

int main(){ IO;
  int t;
  cin >> t;

  for(int ncase = 1; ncase <= t; ++ncase){
    cout << "Case #" << ncase << ": ";

    int m;
    cin >> m;

    if(m == 0){
      cout << "INSOMNIA" << endl;
      continue;
    }

    int n = m;
    int cnt = 0;
    vector<int> mark(10, 0);

    while(true){
      int t = n;
      while(t){
        int d = t % 10;
        t /= 10;

        if(mark[d] == 0){
          mark[d] = 1;
          cnt++;
          if(cnt == 10) break;
        }
      }

      if(cnt == 10) break;
      n += m;
    }
    
    cout << n << endl;
  }

  return 0;
}
