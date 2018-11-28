#include <iostream>
#include <string>
#include <set>
#include <vector>
#include <algorithm>
#include <stack>

using namespace std;

const int INF = -1;

int solve() {
  int N, X;
  vector<int> S;
  cin>>N>>X;
  for(int i=0;i<N;++i) {
    int s;
    cin>>s;
    S.push_back(s);
  }
  sort(S.rbegin(), S.rend());
  
  int res = 0;
  for(int i=0;i<N;++i) {
    if(S[i]==INF) {
      continue;
    }
    for(int j=i+1;j<N;++j) {
      if(S[j]!=INF && S[i]+S[j]<=X) {
        //cerr<<"+"<<S[j]<<"+";
        S[j] = INF;
        break;
      }
    }
    //cerr<<S[i]<<endl;
    res++;
    S[i] = INF;
  }

  return res;
}

int main(int argc, char** argv) {
  int ntc;
  cin>>ntc;
  for(int tc=1;tc<=ntc;++tc) {
    cout<<"Case #"<<tc<<": ";
    cout<<solve()<<endl;
  }
}
