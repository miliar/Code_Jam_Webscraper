#include <iostream>
#include <vector>
#include <map>
#include <queue>
#include <list>
#include <set>
#include <algorithm>
#include <climits>
#include <cmath>
#include <string>
using namespace std;

int m, n;
string s[8];
int ssid[4][8];
string ss[4][8];
int pos[4];
int worst, wcount;

// From http://www.cplusplus.com/forum/beginner/83540/
std::string common_prefix( std::string a, std::string b )
{
    if( a.size() > b.size() ) std::swap(a,b) ;
    return std::string( a.begin(), std::mismatch( a.begin(), a.end(), b.begin() ).first ) ;
}

void rec(int spos, int sspos) {
  int i, j, k, tot;
  
  ssid[sspos][pos[sspos]-1] = spos;
  
  if(spos == m-1) {
    // Copy on ss
    for(i=0; i<n; i++) {
      for(j=0; j<pos[i]; j++) {
        ss[i][j] = s[ssid[i][j]];
      }
    }
    
    // Order
    for(i=0; i<n; i++) {
      sort(ss[i], ss[i]+pos[i]);
    }
    
    int ok = 1;
    for(i=0; i<n; i++) {
      if(pos[i] == 0) ok=0;
    }
    
    /*
    for(i=0; i<n; i++) {
      cout << i << ": ";
      for(j=0; j<pos[i]; j++) cout  << ss[i][j] << " ";
      cout << endl;
    }
    */
    
    if(ok) {
      tot = 0;    
      for(i=0; i<n; i++) {
        tot++;
        // Do common prefix with previous
        for(k=0; k<ss[i][0].size(); k++) tot++;
        for(j=1; j<pos[i]; j++) {
          tot += ss[i][j].size() - common_prefix(ss[i][j-1], ss[i][j]).size();
        }
      }
      
      // cout << "TOT: " << tot << endl;
      
      // Check worst
      if(tot > worst) {
        worst = tot;
        wcount = 1;
      } else if(tot == worst) {
        wcount++;
      }
    }
  } else {
    for(i=0; i<n; i++) {
      pos[i]++;
      rec(spos+1, i);
      pos[i]--;
    }
  }

}

void solve(int test) {
  int i;
  
  cin >> m >> n;
  for(i=0; i<m; i++) cin >> s[i];
  worst = 0;
  wcount = 0;
  
  for(i=0; i<n; i++) {
    pos[i]++;
    rec(0, i);
    pos[i]--;
  }

  cout << "Case #" << (test+1) << ": " << worst << " " << wcount << endl;
}


int main() {
  
  int t, T;
  cin >> T;
  for(t=0; t<T; t++) solve(t);
  return 0;
}

