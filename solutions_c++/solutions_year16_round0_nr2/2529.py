#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <stack>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
#define REP(i,a,n) for(int i=(a); i<(int)(n); i++)
#define rep(i,n) REP(i,0,n)
#define FOR(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)
#define ALLOF(c) (c).begin(), (c).end()
typedef long long ll;

int solve(string seq){
  int ret = 0;
  for(int i=seq.size()-1; i>=0; i--){
    if(seq[i] == '+') continue;
    if(seq[0] == '+'){
      int ii = 0;
      while(ii+1<seq.size() && seq[ii+1]=='+') ii++;
      rep(j,ii+1) seq[j] = '-';
      ret++;
    }
    string nseq = "";
    for(int j=i; j>=0; j--){
      if(seq[j] == '+') nseq += "-";
      else nseq += "+";
    }
    REP(j,i+1,seq.size()) nseq += seq[j];
    seq = nseq;
    ret++;
  }
  return ret;
}


int main(){
  ios::sync_with_stdio(false);
  int T;
  cin >> T;
  rep(t,T){
    string seq;
    cin >> seq;
    int ret = solve(seq);
    cout << "Case #" << t+1 << ": " << ret << endl;
  }
  return 0;
}

