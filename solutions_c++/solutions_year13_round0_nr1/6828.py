
/**
 *
 *  Time-stamp:<2013/04/13 20:56:26>
 **/

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <queue>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <fstream>
 
using namespace std;
 
//conversion
//------------------------------------------
inline int toInt(string s) {int v; istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}
 
//typedef
//------------------------------------------
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef long long LL;
 
//container util
//------------------------------------------
#define ALL(a)  (a).begin(),(a).end()
#define RALL(a) (a).rbegin(), (a).rend()
#define PB push_back
#define MP make_pair
#define SZ(a) int((a).size())
#define EACH(i,c) for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); ++i)
#define EXIST(s,e) ((s).find(e)!=(s).end())
#define SORT(c) sort((c).begin(),(c).end())
 
//repetition
//------------------------------------------
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n)  FOR(i,0,n)

#define Debug cout << "LINE: " << __LINE__ << endl

#define MAX_F 4

int t;
VS field;

int main()
{
  cin >> t;

  REP(i, t) {
    field.clear();
    REP(j, MAX_F) {
      string tmp;
      cin >> tmp;
      field.PB(tmp);
    }

    /*
    REP(j, MAX_F) {
      cout << field[j] << endl;
    }
    cout << endl;
    */

    int xw, ow;
    int xh, oh;
    int xs1, os1;
    int xs2, os2;
    int dot;
    bool end = false;

    xw = ow = 0;
    xh = oh = 0;
    xs1 = os1 = 0;
    xs2 = os2 = 0;
    dot = 0;
    REP(j, MAX_F) {
      // w and h
      REP(k, MAX_F) {
        // w
        if (field[j][k]=='X') {
          xw++;
        } else if (field[j][k]=='O') {
          ow++;
        } else if (field[j][k]=='T') {
          xw++;
          ow++;
        } else {
          dot++;
        }

        // h
        if (field[k][j]=='X') {
          xh++;
        } else if (field[k][j]=='O') {
          oh++;
        } else if (field[k][j]=='T') {
          xh++;
          oh++;
        }

        // s1
        if (j==k) {
          if (field[j][k]=='X') {
            xs1++;
          } else if (field[j][k]=='O') {
            os1++;
          } else if (field[j][k]=='T') {
            xs1++;
            os1++;
          }
        }

        // s2
        if (j+k==3) {
          if (field[j][k]=='X') {
            xs2++;
          } else if (field[j][k]=='O') {
            os2++;
          } else if (field[j][k]=='T') {
            xs2++;
            os2++;
          }
        }
        
      }
      /*
      cout << xw << endl;
      cout << xh << endl;
      cout << ow << endl;
      cout << oh << endl;
      */
      if (xw==4 or xh==4) {
        cout << "Case #" << i+1 << ": X won" << endl;
        end = true;
        break;
      } else if (ow==4 or oh==4) {
        cout << "Case #" << i+1 << ": O won" << endl;
        end = true;
        break;
      }
      xw = ow = 0;
      xh = oh = 0;
      
    }
    if (end == true) continue;
    
    if (xs1==4 or xs2==4) {
      cout << "Case #" << i+1 << ": X won" << endl;
    } else if (os1==4 or os2==4) {
      cout << "Case #" << i+1 << ": O won" << endl;
    } else if (dot>0) {
      cout << "Case #" << i+1 << ": Game has not completed" << endl;
    } else {
      cout << "Case #" << i+1 << ": Draw" << endl;
    }
    field.clear();

    
  }

  return 0;
}
