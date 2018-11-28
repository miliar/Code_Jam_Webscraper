#include <iostream>
#include <string>
#include <set>
#include <vector>
#include <algorithm>
#include <stack>

using namespace std;

int bubble_sort(vector<int> K) {
  int cnt = 0;
  int n = K.size();
  bool sw = true;
  while(sw) {
    sw = false;
    for(int j=0;j<n;++j) {
      if(K[j-1] > K[j]) {
        int t=K[j];
        K[j] = K[j-1];
        K[j-1] = t;
        cnt++;
        sw = true;
      }
    }
  }
  return cnt;
}

bool isok(vector<int> const& K, vector<int> const& V) {
  bool asc = true;
  for(int i=0;i<K.size()-1;++i) {
    if(asc) {
      if(V[K[i]]>V[K[i+1]]) {
        asc = false;
      }
    } else {
      if(V[K[i]]<V[K[i+1]]) {
        return false;
      }
    }
  }
  return true;
}

int solve() {
  int N;
  cin>>N;
  vector<int> V;
  vector<int> K;
  for(int n=0;n<N;++n) {
    int v;
    cin>>v;
    V.push_back(v);
    K.push_back(n);
  }
  int best = N*N;
  do{
    bool ok = isok(K, V);
    if(ok) {
      int bs = bubble_sort(K);
      // cerr<<bs<<endl;
      if(best>bs) {
        best = bs;
      }
    }
  } while(next_permutation(K.begin(), K.end()));
  return best;
}

int main(int argc, char** argv) {
  int ntc;
  cin>>ntc;
  for(int tc=1;tc<=ntc;++tc) {
    cout<<"Case #"<<tc<<": ";
    cout<<solve()<<endl;
  }
}
