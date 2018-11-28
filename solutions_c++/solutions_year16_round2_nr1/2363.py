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
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>

using namespace std;

inline int toInt(string s) {int v; istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}

template<class T> inline T sqr(T x) {return x*x;}

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef long long LL;

#define ALL(a)  (a).begin(),(a).end()
#define RALL(a) (a).rbegin(), (a).rend()
#define PB push_back
#define MP make_pair
#define SZ(a) int((a).size())
#define EACH(i,c) for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); ++i)
#define EXIST(s,e) ((s).find(e)!=(s).end())
#define SORT(c) sort((c).begin(),(c).end())

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n)  FOR(i,0,n)

#define CLR(a) memset((a), 0 ,sizeof(a))

#define dump(x)  cerr << #x << " = " << (x) << endl;
#define debug(x) cerr << #x << " = " << (x) << " (L" << __LINE__ << ")" << " " << __FILE__ << endl;

int main(void){
  int T;
  cin >> T;
  map<char, int> mp;
  int count[10];

  string s, allc = "ZEROONETWOTHREEFOURFIVESIXSEVENEIGHTNINE";
  for(int i=0;i<T;i++){
    cin >> s;
    for(int j=0;j<allc.size();j++){
      mp[allc[j]] = 0;
    }
    for(int j=0;j<s.size();j++){
      mp[s[j]] += 1;
    }

    //ZERO
    count[0] = mp['Z'];
    mp['Z'] -= count[0], mp['E'] -= count[0], mp['R'] -= count[0], mp['O'] -= count[0];

    //TWO
    count[2] = mp['W'];
    mp['T'] -= count[2], mp['W'] -= count[2], mp['O'] -= count[2];

    //SIX
    count[6] = mp['X'];
    mp['S'] -= count[6], mp['I'] -= count[6], mp['X'] -= count[6];

    //EIGHT
    count[8] = mp['G'];
    mp['E'] -= count[8], mp['I'] -= count[8], mp['G'] -= count[8], mp['H'] -= count[8], mp['T'] -= count[8];

    //THREE
    count[3] = mp['T'];
    mp['T'] -= count[3], mp['H'] -= count[3], mp['R'] -= count[3], mp['E'] -= count[3], mp['E'] -= count[3];

    //SEVEN
    count[7] = mp['S'];
    mp['S'] -= count[7], mp['E'] -= count[7], mp['V'] -= count[7], mp['E'] -= count[7], mp['N'] -= count[7];

    //FOUR
    count[4] = mp['R'];
    mp['F'] -= count[4], mp['O'] -= count[4], mp['U'] -= count[4], mp['R'] -= count[4];

    //FIVE
    count[5] = mp['V'];
    mp['F'] -= count[5], mp['I'] -= count[5], mp['V'] -= count[5], mp['E'] -= count[5];

    count[1] = mp['O'];
    count[9] = mp['I'];

    cout << "Case #" << i+1 << ": ";
    for(int j=0;j<10;j++){
      for(int k=0;k<count[j];k++) cout << j;
    }
    cout << endl;
  }
    return 0;
}
