#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <iomanip>

using namespace std;

typedef long long int s64;

double computeProfit(vector<s64> const& bet, int j, s64 fill_to, int k) {
  double profit = 0;
  for(int i=0;i<bet.size();++i) {
    s64 mybet = fill_to - bet[i];
    if(mybet >= 0) {
      profit -= mybet;
      if(i < (j-k) ) {
        profit += mybet * 36./(j-k);
      } else {
        profit--;
      }
    }
    //cerr<<"On number "<<i<<" B="<<mybet<<" P="<<1./j<<" profit="<<profit<<endl;
  }
  return profit;
}

s64 tryFill(vector<s64> const& bet, int j, s64 fill_to, s64 budget) {
  //cerr<<"TryFill "<<j<<" "<<fill_to<<" ";
  for(int i=0;i<j;++i) {
    budget-= (fill_to - bet[i]);
  }
  //cerr<<" B="<<budget<<endl;
  return budget;
}

double solve() {
  s64 B;
  int N;
  cin>>B>>N;
  vector<s64> bet(37, 0);
  vector<double> profit(37, 0);
  vector<s64> events;
  for(int i=0;i<N;++i) {
    s64 xi;
    cin>>xi;
    bet[i]=xi;
  }
  sort(bet.begin(), bet.end());

  for(int i=1;i<37;++i) {
    if(bet[i-1] == bet[i]) {
      continue;
    }
    s64 min_fill = bet[i-1];
    s64 max_fill = bet[i] - 1;
    while( max_fill - min_fill > 1) {
      s64 try_fill = (max_fill+min_fill)/2;
      bool can_fill = tryFill(bet, i, try_fill, B) >= 0;
      if(can_fill) {
        min_fill = try_fill;
      } else {
        max_fill = try_fill-1;
      }
    }
    while(max_fill != min_fill && tryFill(bet, i, min_fill+1, B) >= 0) {
      min_fill++;
    }
    s64 bb = tryFill(bet, i, min_fill, B);
    if(bb >= 0) {
      //cerr<<i<<" "<<min_fill<<endl;
      for(int k=0;k<i&&k<=bb;++k) {
        double pp = computeProfit(bet, i, min_fill, k);
        if(pp>profit[i]) {
          profit[i] = pp;
        }
      }
    }
    if(min_fill != bet[i-1]) {
      min_fill--;
      s64 bb = tryFill(bet, i, min_fill, B);
      if(bb >= 0) {
        //cerr<<i<<" "<<min_fill<<endl;
        for(int k=0;k<i&&k<=bb;++k) {
          double pp = computeProfit(bet, i, min_fill, k);
          if(pp>profit[i]) {
            profit[i] = pp;
          }
        }
      }
    }
  }

  double max_profit = 0;
  for(int i=0;i<profit.size();++i) {
    if(profit[i] > max_profit) {
      max_profit = profit[i];
    }
  }

  return max_profit;
}

int main(int argc, char** argv) {
  int T;
  cin>>T;

  for(int t=0;t<T;++t) {
    double sol = solve();
    cout<<"Case #"<<(t+1)<<": "<<std::setprecision(12)<<sol<<endl;
  }

  return 0;
}
