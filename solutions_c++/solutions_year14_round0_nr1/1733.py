/*
 * MagicTrick.C
 *
 *  Created on: Apr 11, 2014
 *      Author: Abhay
 */

#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <list>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <complex>
#include <cstdio>
#include <cassert>
#include <cmath>

#if defined (__GNUC__) && (__GNUC__ <= 2)
#include <hash_map>
#include <hash_set>
#else
#include <ext/hash_map>
#include <ext/hash_set>
using namespace __gnu_cxx;
#endif
using namespace std;

#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;i++)
#define REP(i,n) FOR(i,0,(n)-1)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define sz size()
template<class T> inline int size(const T& c) { return c.sz; }
#define FORA(i,c) REP(i,size(c))

#define itype(c) __typeof((c).begin())
#define FORE(e,c) for(itype(c) e=(c).begin();e!=(c).end();e++)
#define pb push_back
#define X first
#define Y second
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define SORT(x) sort(all(x))
#define REVERSE(x) reverse(all(x))
#define CLEAR(x,c) memset(x,c,sizeof(x))

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
LL s2i(string s) { istringstream i(s); LL x; i>>x; return x; }
template<class T> string i2s(T x) { ostringstream o; o << x; return o.str(); }


//ifstream fin("C:\\Users\\Abhay\\Eclipse-Indigo-CPP\\HelloWorld\\src\\data.in");
//#define cin fin

static const std::string BadMagician = "Bad magician!";
static const std::string CheatVolunteer = "Volunteer cheated!";
int main()
{
  int T;
  cin>>T;
  for(int C=1;C<=T;++C)
  {
    int row1, row2;
    int first[4],second[4];
    cin>>row1;
    REP(i,4){
        if(i+1==row1)
        {
          cin>> first[0] >> first[1] >> first[2] >> first[3];
        }
        else
        {
          int temp;
          REP(j,4){
            cin>>temp;
          }
        }
    }
    cin>>row2;
    REP(i,4){
        if(i+1==row2)
        {
          cin>> second[0] >> second[1] >> second[2] >> second[3];
        }
        else
        {
          int temp;
          REP(j,4){
            cin>>temp;
          }
        }
    }

    int matched = 0;
    int count = 0;
    REP(i,4)
    {
      REP(j,4)
        if(first[i] == second[j])
        {
          matched = first[i];
          ++count;
          break;
        }
    }
    if(count ==0)
      cout<<"Case #"<<C<<": "<<CheatVolunteer<<endl;
    else if(count ==1)
      cout<<"Case #"<<C<<": "<<matched<<endl;
    else
      cout<<"Case #"<<C<<": "<<BadMagician<<endl;
  }
  return 0;
}


