#include "stdio.h"
#include "iostream"
#include "vector"
#include "queue"
#include "algorithm"
#include "deque"
using namespace std;

string output = "";
string deal[15][5];

int ppp(int n) {
  deal[n][1] = min(deal[n-1][1] + deal[n-1][2] , deal[n-1][2] + deal[n-1][1]);
  deal[n][2] = min(deal[n-1][2] + deal[n-1][3] , deal[n-1][3] + deal[n-1][2]);
  deal[n][3] = min(deal[n-1][1] + deal[n-1][3] , deal[n-1][3] + deal[n-1][1]);
}

int main() {
  cout.sync_with_stdio(false);
  int T;
  cin>>T;
  deal[0][1] = "P";
  deal[0][2] = "R";
  deal[0][3] = "S";
  for (int i = 1; i<=12; i++) {
    ppp(i);
    // cout << deal[i][1] << endl;
  }
  for (int cs = 1; cs<= T;cs++) {
    cout <<"Case #"<<cs<<": ";
    int n,p,r,s;
    cin >> n;
    cin >> r>> p>>s;
    output = "";
    for (int i = 1; i<=3; i++) {
      int cr=0, cp=0, cs=0;
      for (int j = 0; j<deal[n][i].length();j++) {
        if (deal[n][i][j]=='R') {
          cr++;
        }
        if (deal[n][i][j]=='P') {
          cp++;
        }
        if (deal[n][i][j]=='S') {
          cs++;
        }
      }
      if (cr==r && cp==p && cs==s) {
        if (output == "") {
          output = deal[n][i];
        }
        else {
          output = min(output, deal[n][i]);
        }
      }
    }
    if (output == "") {
      cout<<"IMPOSSIBLE"<<endl;
    }
    else {
      cout << output << endl;
    }
  }
  return 0;
}
