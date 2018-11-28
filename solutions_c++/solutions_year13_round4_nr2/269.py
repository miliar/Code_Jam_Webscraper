#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

pair<long long int, long long int> solve() {

  long long int N;
  long long int P;
  cin>>N>>P;
  long long int NN = 1LL<<N;

  if(P==NN) {
    return pair<long long int, long long int>(NN-1, NN-1);
  }

  long long int canwin = 0;
  long long int bound = 0;
  for(int w=1;w<=N;++w) {
    bound = (1LL<<(N+1-w))-1;
    if(bound<P) {
      break;
    }
    canwin = (1LL<<(N))-(1LL<<(w));
    //cout<<bound<<" "<<P<<" "<<canwin<<endl;
  }

  long long int mustwin = 0;
  bound = 1;
  for(int w=1;w<=N;++w) {
    bound += 1LL<<(N-w);
    if(bound>P) {
      break;
    }
    mustwin = (1LL<<(w+1))-2;
    //cout<<bound<<" "<<P<<" "<<mustwin<<endl;
  }


  return pair<long long int, long long int>(mustwin,canwin);
}

int main(int argc, char** argv) {
  int T;
  cin>>T;

  for(int t=0;t<T;++t) {
    pair<long long int,long long int> sol = solve();
    cout<<"Case #"<<(t+1)<<": "<<sol.first<<" "<<sol.second<<endl;
  }

  return 0;
}
