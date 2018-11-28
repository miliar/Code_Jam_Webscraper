#include <iostream>
#include <string>
#include <set>
#include <vector>
#include <algorithm>
#include <stack>
#include <map>

using namespace std;

int solve() {
  map<int, long> res;

  int M, N;
  long comb=1;
  cin>>M>>N;
  vector<string> list;
  for(int i=0;i<M;++i) {
    string s;
    cin>>s;
    list.push_back(s);
    comb*=N;
  }

  for(long i=0;i<comb;++i) {
    //cerr<<"Combination "<<i<<endl;
    vector<set<string>> alloc(N);
    long base=1;
    for(int b=0;b<M;++b,base*=N) {
      int server = (i/base)%N;
      string s = list[b];
      for(int l=0;l<=s.size();++l) {
        string ss = s.substr(0, l);
        alloc[server].insert(ss);
        //cerr<<server<<" "<<ss<<endl;
      }
    }
    long count=0;
    for(int j=0;j<N;++j) {
      count += alloc[j].size();
      //cerr<<"Server "<<j<<" size "<<alloc[j].size()<<endl;
    }
    res[count] = res[count]+1;
  }

  int wc = 0;
  long ways = 0;
  for(auto i = res.begin(); i != res.end(); ++i) {
    if(i->first > wc) {
      wc = i->first;
      ways = i->second;
    }
  }
  cout<<wc<<" "<<ways<<endl;
}

int main(int argc, char** argv) {
  int ntc;
  cin>>ntc;
  for(int tc=1;tc<=ntc;++tc) {
    cout<<"Case #"<<tc<<": ";
    solve();
  }
}
