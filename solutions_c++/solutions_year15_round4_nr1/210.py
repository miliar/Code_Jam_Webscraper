// -*- compile-command: "g++ -Wall -Wextra x.cpp -o x && ./x <test.in" -*-
#include <algorithm>
#include <cassert>
#include <cstdio>
#include <cstdio>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <utility>
#include <vector>
using namespace std;
typedef long long in;
#define PB push_back
#define MP make_pair
#define sz(v) (in)(((v).size()))
#define forn(i,n) for(int i=0;i<(n);i++)
#define forv(i,v) forn(i,sz(v))
typedef vector<in> VI;

  in R,C;
  vector<string> M;

in ddx(char c) {
  if(c=='^') return -1;
  if(c=='>') return 0;
  if(c=='v') return 1;
  if(c=='<') return 0;  
  return 0;
}
in ddy(char c) {
  if(c=='^') return 0;
  if(c=='>') return 1;
  if(c=='v') return 0;
  if(c=='<') return -1;  
  return 0;
}

bool check(in x, in y) {
  in cnt = 0;
  forn(i,R) {
    forn(j,C) {
      if(x==i || y==j) {
        if(M[i][j] != '.') cnt++;
      }
    }
  }
  return cnt > 1;
}

void test() {
  cin >> R >> C;
  M = vector<string>(R);
  forn(i,R) {
    cin >> M[i];
  }

  // check if all free:
  forn(i,R) {
    forn(j,C) {
      if(M[i][j]!= '.' && !check(i,j)) {
        cout << "IMPOSSIBLE" << endl;
        return;
      }
    }
  }

 
  in res = 0;
   // count numbers to fix
  forn(i,R) {
    forn(j,C) {
      if(M[i][j] != '.') {
        in x=i, y=j;
        in dx = ddx(M[i][j]);
        in dy = ddy(M[i][j]);
        x+=dx; y+=dy;
        bool found = false;
        while(0<=x && x<R && 0<=y && y<C) {
          if(M[x][y] != '.') {
            found = true;
            break;
          }
          x+=dx; y+=dy;
        }
        if(!found) {
          // cout << "no other from " << M[i][j] << " at " << i << " " << j << endl;
          res++;
        }
      }
    }
  }

  cout << res << endl;
}
int main(){
  std::ios::sync_with_stdio(false); // remove this if you use printf/scanf
  std::cin.tie(0);

  in T; cin >> T;
  forn(t,T) {
    cout << "Case #" << t+1 << ": ";
    test();
  }

  return 0;  
}
