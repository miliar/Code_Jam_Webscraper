#include <iostream>
#include <string>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;
vector <int> D;
vector <pair<int,int> > DD;
int mult[4][4] = {{0,1,2,3},{1,0,3,2},{2,3,0,1},{3,2,1,0}};
int sign[4][4] = {{1,1,1,1},{1,-1,1,-1},{1,-1,-1,1},{1,1,-1,-1}};

int T, X, L;
string str;

bool test() {
  int n, s;
  n=0; s=1;
  for (int i=0; i<L*X; i++) {
    s *= sign[n][D[i%L]];
    n = mult[n][D[i%L]];
    if (n==1 && s==1) {
      n=0;
      for (int j=i+1; j<L*X-1; j++) {
        s *= sign[n][D[j%L]];
        n = mult[n][D[j%L]];
        if (n==2 && s==1) {
          if (DD[j+1].first==1 && DD[j+1].second==3) {
            return true;
          }
        }
      }
      n=1; s=1;
    }
  }
  return false;
}

int main() {
  int s,n;
  cin >> T;
  
  for (int i=1; i<=T; i++) {
    cin >> L >> X;
    D.clear();
    DD.clear();
    cin >> str;
    for (int j=0; j<L; j++) {
      switch(str[j]) {
      case 'i':
        D.push_back(1);
        break;
      case 'j':
        D.push_back(2);
        break;
      case 'k':
        D.push_back(3);
        break;        
      }
    }
    s=1;n=0;
    for (int z=L*X-1; z>=0; z--) {
      s *= sign[D[z%L]][n];
      n = mult[D[z%L]][n];
      DD.push_back(pair<int,int>(s,n));
    }
    reverse(DD.begin(), DD.end());
    if (test()) {
      cout << "Case #" << i << ": " << "YES" << endl;      
    } else {
      cout << "Case #" << i << ": " << "NO" << endl;      
    }

  }

  return 0;
}
