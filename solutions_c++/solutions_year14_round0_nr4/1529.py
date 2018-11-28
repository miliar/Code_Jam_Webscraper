/*
 * DeceitfulWar.C
 *
 *  Created on: Apr 11, 2014
 *      Author: Abhay
 */

/*For War
Naomi plays highest to lowest
If Ken has nothing higher, he plays lowest
Else Ken plays higher

For DeceitfulWar
Naomi plays lowest to highest
If weight lower than Ken's lowest - Says just below highest
Takes it out
Else if below highest Says weight more than highest if at least one less
Else winning streak*/

#include <iostream>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <deque>
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
typedef deque<long> DL;
LL s2i(string s) { istringstream i(s); LL x; i>>x; return x; }
template<class T> string i2s(T x) { ostringstream o; o << x; return o.str(); }


//ifstream fin("C:\\Users\\Abhay\\Eclipse-Indigo-CPP\\HelloWorld\\src\\data.in");
//#define cin fin

int main()
{
  int T;
  cin>>T;
  for(int C=1;C<=T;++C)
  {
    int WarWin =0;
    int DWarWin = 0;
    double tmpWeight =0.0;
    DL nmWeights, knWeights;
    DL nmWeightsDW, knWeightsDW;
    int N = 0;
    cin>>N;
    REP(i,N)
    {
      cin>> tmpWeight;
      nmWeights.push_back(tmpWeight * 100000.0);
      nmWeightsDW.push_back(tmpWeight * 100000.0);
    }
    REP(i,N)
    {
      cin>> tmpWeight;
      knWeights.push_back(tmpWeight * 100000.0);
      knWeightsDW.push_back(tmpWeight * 100000.0);
    }

    sort(nmWeights.begin(),nmWeights.end());
    sort(nmWeightsDW.begin(),nmWeightsDW.end());
    sort(knWeights.begin(),knWeights.end());
    sort(knWeightsDW.begin(),knWeightsDW.end());

/*    cout << endl;
    REP(i,N)
    {
      cout << nmWeightsDW[i] << " ";
    }
    cout << endl;
    REP(i,N)
    {
      cout << knWeightsDW[i] << " ";
    }
    cout << endl;*/

    /*War*/
    while(nmWeights.size() > 0)
    {
      if(nmWeights.back() > knWeights.back())
      {
        ++WarWin;
        knWeights.pop_front();
      }
      else
      {
        knWeights.pop_back();
      }
      nmWeights.pop_back();
    }

    /*Deceitful War */
    while(nmWeightsDW.size() > 0)
    {
      if(nmWeightsDW.front() < knWeightsDW.front())
      {
        nmWeightsDW.pop_front();
        knWeightsDW.pop_back();
      }
      else if(nmWeightsDW.front() > knWeightsDW.front() && nmWeightsDW.front() < knWeightsDW.back())
      {
        nmWeightsDW.pop_front();
        knWeightsDW.pop_front();
        ++DWarWin;
      }
      else
      {
        nmWeightsDW.pop_front();
        knWeightsDW.pop_front();
        ++DWarWin;
      }
    }
    cout<<"Case #"<< C << ": " << DWarWin << " " << WarWin <<endl;
  }
  return 0;
}


