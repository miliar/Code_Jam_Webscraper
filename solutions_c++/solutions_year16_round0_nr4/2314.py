#include<iostream>
#include<vector>


using namespace std;
typedef unsigned long long ull;

vector<ull> solve(ull K, ull C, ull S) {
  ull total = 1;
  for(int i=0 ; i < C; ++i) {
    total *= K;
  }

  //cout<<total<<endl;
  vector<ull> result;
  ull tile = 1;
  result.push_back(1);
  for(int i=1 ; i < K; ++i ) {
    tile += (total / K); 
    result.push_back(tile);
  }
  return result;
}

int main() {
  int T;
  cin >> T;
  for(int t=0;t < T; ++t) {
    int K,C,S;
    cin >> K >> C >> S;
    vector<ull> result = solve(K,C,S);
    cout<<"Case #" << t + 1 << ":";
    if(result.size() == 0) {
      cout << " IMPOSSIBLE";
    } else {
      for(auto v : result) {
        cout << " " <<v ;
      }
    }
    cout << endl;
  }
}
