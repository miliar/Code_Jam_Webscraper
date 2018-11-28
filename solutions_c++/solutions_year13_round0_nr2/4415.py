#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<map>
using namespace std;

int main(){
  int T;
  cin >> T;
  for(int z=1; z<=T; ++z){
    int n,m;
    cin >> n >> m;
    map<int,int> h_cnt;

    vector<vector<int> > in(n, vector<int>(m));
    for(int i=0; i<n; ++i){
      for(int j=0; j<m; ++j){
        cin >> in[i][j];
        h_cnt[in[i][j]]++;
      }
    }

    bool ok = true;
    for(map<int,int>::iterator it = h_cnt.begin(); it!=h_cnt.end(); ++it){
      int h = it->first;

      for(int i=0; i<n; ++i){
        bool can_cut = true;
        for(int j=0; j<m; ++j){
          if(in[i][j] > h){
            can_cut = false;
            break;
          }
        }
        if(can_cut){
          for(int j=0; j<m; ++j){
            in[i][j] = 0;
          }
        }
      }

      for(int i=0; i<m; ++i){
        bool can_cut = true;
        for(int j=0; j<n; ++j){
          if(in[j][i] > h){
            can_cut = false;
            break;
          }
        }
        if(can_cut){
          for(int j=0; j<n; ++j){
            in[j][i] = 0;
          }
        }
      }

      for(int i=0; i<n; ++i){
        ok &= count(in[i].begin(), in[i].end(), h) == 0;
      }
      if(!ok){
        break;
      }
    }

    if(ok)
      cout << "Case #" << z << ": " << "YES" << endl;
    else
      cout << "Case #" << z << ": " << "NO" << endl;
  }
}