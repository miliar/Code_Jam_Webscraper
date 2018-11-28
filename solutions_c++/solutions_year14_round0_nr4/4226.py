#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <list>
#include <vector>
#include <map>
#include <sstream>
#include <cmath>
#include <bitset>
#include <utility>
#include <set>
#include <numeric>
#include <ctime>
#define INF 2147483647
using namespace std;

struct block{
  double wt;
  int player;
};

int cmp (struct block a, struct block b) {
  return a.wt < b.wt;
}

int main(int argc, const char * argv[]) {

  cin.sync_with_stdio(false);
  cout.sync_with_stdio(false);
  int cases, currCase = 0, n, deceitCnt, trueCnt;
  struct block bl;  
  cin >> cases;
  while(currCase++ < cases) {
    cin >> n;
    vector<struct block> b, c;
    for(int i = 0; i < n; i++ ) {
      cin >> bl.wt;
      bl.player = 1;
      b.push_back(bl);
      c.push_back(bl);      
    }

    for(int i = 0; i < n; i++ ) {
      cin >> bl.wt;
      bl.player = 2;
      b.push_back(bl);
      c.push_back(bl);            
    }

    sort(b.begin(), b.end(), cmp);
    sort(c.begin(), c.end(), cmp);

    trueCnt = 0;
    
    while( 0 < c.size() ) {

      while ( 0 < c.size() && 1 == c[0].player ) {
        c.erase(c.begin());
        for( int i = 0; i < c.size() ; i++ ) {
          if ( 2 == c[i].player ) {
            c.erase(c.begin()+i);
            break;
          }
        }
      }

      while ( 0 < c.size() && 2 == c[0].player ) {
        c.erase(c.begin());
        for( int i = c.size() - 1; i >= 0 ; i-- ) {
          if ( 1 == c[i].player ) {
            c.erase(c.begin()+i);
            trueCnt++;
            break;
          }
        }
      }
      
    }

    deceitCnt = 0;
    
    while( 0 < b.size() ) {

      while ( 0 < b.size() && 2 == b[b.size()-1].player ) {
        b.erase(b.begin()+b.size()-1);
        for( int i = 0; i < b.size(); i++ ) {
          if ( 1 == b[i].player ) {
            b.erase(b.begin()+i);
            break;
          }
        }
      }

      while ( 0 < b.size() && 1 == b[0].player ) {
        b.erase(b.begin());
        for( int i = b.size() - 1; i >= 0 ; i-- ) {
          if ( 2 == b[i].player ) {
            b.erase(b.begin()+i);
            break;
          }
        }
      }

      while( 0 < b.size() && 2 == b[0].player ) {
        b.erase(b.begin());
        for( int i = 0; i < b.size(); i++ ) {
          if ( 1 == b[i].player ) {
            b.erase(b.begin()+i);
            deceitCnt++;
            break;
          }
        }
      }

    }
    cout << "Case #" <<currCase <<": "<< deceitCnt << " " << trueCnt << endl;
  }
  return 0;
}
