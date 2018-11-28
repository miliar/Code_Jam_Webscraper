#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool solve() {
  int N, M;
  cin>>N>>M;
  vector<vector<int> > lawn;
  for(int n=0;n<N;++n) {
    vector<int> line;
    for(int m=0;m<M;++m) {
      int h;
      cin>>h;
      line.push_back(h);
    }
    lawn.push_back(line);
  }
  vector<int> nprogram;
  vector<int> mprogram;

  for(int n=0;n<N;++n) {
    int h = 0;
    for(int m=0;m<M;++m) {
      h = max(h, lawn[n][m]);
    }
    nprogram.push_back(h);
  }
  for(int m=0;m<M;++m) {
    int h = 0;
    for(int n=0;n<N;++n) {
      h = max(h, lawn[n][m]);
    }
    mprogram.push_back(h);
  }

  for(int n=0;n<N;++n) {
    for(int m=0;m<M;++m) {
      int h = lawn[n][m];
      if( !(
             (nprogram[n] == h && mprogram[m] >= h) ||
             (nprogram[n] >= h && mprogram[m] == h)
           )
        ) {
        return false;
      }
    }
  }
  return true;
}

int main(int argc, char** argv) {
  int N;
  cin>>N;
  for(int i=0;i<N;++i) {
    bool ok = solve();
    cout<<"Case #"<<i+1<<": ";
    if(ok) {
      cout<<"YES"<<endl;
    } else {
      cout<<"NO"<<endl;
    }
  }
}
