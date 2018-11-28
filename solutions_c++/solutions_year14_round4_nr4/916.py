#include <iostream>
#include <algorithm>
#include <utility>
#include <vector>
#include <string>
#include <iostream>

using namespace std;

bool next_b(vector<int> &b, int m){
  bool cool = false;
  for(int i=0;i<b.size();i++){
    if (b[i] < m-1){
      b[i] += 1;
      cool = true;
      break;
    }
    else{
      b[i]=0;
    }
  }
  return cool;
}

int main(){
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int T;
  cin >> T;
  for(int t=0; t<T;t++){
    int n,m;
    int mx=0, nm=0;
    cin >> n >> m;
    vector<string> a(n);
    for (int i=0;i<n;i++){
      cin >> a[i];
    }
    vector<int> b(n);
    do{
      vector<string> prs[4];
      for (int i=0;i<n;i++){
        int serv = b[i];
        for (int j = 0; j <= a[i].size();j++){
          string ss = a[i].substr(0,j);
          prs[serv].push_back(ss);
        }
      }
      int s = 0;
      for(int i=0;i<m;i++){
        sort(prs[i].begin(),prs[i].end());
        int nds = unique(prs[i].begin(), prs[i].end()) - prs[i].begin();
        s+=nds;
      }
      if (s>mx){
        mx = s;
        nm = 0;
      }
      if (s == mx){
        nm++;
      }
    }while(next_b(b,m));
    cout << "Case #" << t+1 << ": " << mx << " " << nm << endl;
    cerr << t << endl;
  }
  return 0;
}
