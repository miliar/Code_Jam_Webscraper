#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <iomanip>

using namespace std;

typedef long long int s64;

map<string, double> cached;

double solve(string s) {
  if(cached.find(s) == cached.end()) {
    //cerr<<"?  "<<s<<endl;
    int N = s.length();
    double profit = 0;

    for(int i=0;i<N;++i) {
      int wait = 0;
      int j=i;
      string ss = s;
      for(;;++wait,++j) {
        if(j >= N) {
          j-=N;
        }
        if(ss[j]=='.') {
          ss[j] = 'X';
          break;
        }
      }
      profit += (N-wait) + solve(ss);
    }

    cached[s] = profit*1.0/N;
    //cerr<<"+  "<<s<<" "<<cached[s]<<endl;
  }
  return cached[s];
}

int main(int argc, char** argv) {

  string final;
  for(int i=1;i<=200;++i) {
    final=final+"X";
    cached[final]=0;
  }

  int T;
  cin>>T;

  for(int t=0;t<T;++t) {
    string s;
    cin>>s;
    double sol = solve(s);
    cout<<"Case #"<<(t+1)<<": "<<std::setprecision(20)<<sol<<endl;
  }

  return 0;
}
