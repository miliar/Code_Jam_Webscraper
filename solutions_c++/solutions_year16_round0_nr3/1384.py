#include <iostream>
#include <sstream>
#include <string>
#include <queue>
#include <deque>
#include <vector>
#include <list>
#include <map>
#include <functional>
#include <algorithm>
#include <iterator>
#include <set>
#include <stack>
#include <limits>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <numeric>


#define LL long long
#define LD long double
#define DD double
#define FORI(i,k,n) for (int i = (k); i < (n); i++)
#define RFORI(i,k,n) for (int i = (k); i > (n); i--)
#define FORLL(i,k,n) for (long long i = (k); i < (n); i++)
#define RFORLL(i,k,n) for (long long i = (k); i > (n); i--)
#define VI vector<int>
#define VPI vector<pair<int,int>>
#define VPL vector<pair<long long,long long>>
#define VB vector<bool>
#define VD vector<double>
#define VL vector<long long>
#define VS vector<string>
#define SZ(x) ((int)x.size())
#define VVI(f,x,y,val) vector<VI> f((x), VI((y), (val)))
#define VVB(f,x,y,val) vector<VB> f((x), VB((y), (val)))
#define VVL(f,x,y,val) vector<VL> f((x), VL((y), (val)))


using namespace std;

class Prob {

  VB prime;
  VI Fact;

  int Length;
  int J;


public:
  map<string, VI> ansMap;

  void calcPrime() {
    prime.resize(10000000, true);
    Fact.resize(10000000, -1);

    prime[2] = true;

    int n = SZ(prime);
    FORI(i, 2, n)
    {
      if (prime[i]) {
        int j = i + i;
        while (j < n) {
          prime[j] = false;
          Fact[j] = i;
          j = j + i;
        }
      }
    }
  }

  bool isPrime(LL val, VI& fact) {
    if (prime[(int)val])
      return true;
    fact.push_back(Fact[(int)val]);
    return false;
  }

  void generate(VS& strings, string prefixStr, string current, int remLen) {

    int n = SZ(current);
    if (remLen < n)
      return;

    FORI(i, 0, remLen - n + 1) {
      string prefix = string(i, '0');
      string suffix = string(remLen - n - i, '0');
      string newStr = prefix + current + suffix;
      strings.push_back(prefixStr+ newStr);
      generate(strings, prefixStr + prefix + current, current, remLen - n - i);
    }

  }

  void addAns(int numDigits, LL N, VI& fact) {
    string prefix;
    FORI(i, 0, numDigits) {
      if (N & (LL)(1 << (LL)i))
        prefix = '1' + prefix;
      else
        prefix = '0' + prefix;
    }

    string suffix = prefix;
    int n = SZ(prefix);

    int remLen = Length - (2*n);
    VS strings;
    generate(strings, "", suffix, remLen);

    string zeroes(remLen, '0');
    if (ansMap.find(prefix + zeroes + suffix) == ansMap.end()) {
      ansMap.insert(make_pair(prefix + zeroes + suffix, fact));
    }

    for (auto str : strings) {
      string newStr = prefix + str + suffix;
      if (ansMap.find(newStr) == ansMap.end()) {
        ansMap.insert(make_pair(newStr, fact));
      }
    }

  }

  void solve(int Length, int J)
  {
    this->Length = Length;
    this->J = J;

    calcPrime();

    FORI(i, 1, 64) {
      int N = 1 + i * 2;
      int numDigits = 0;
      int n = N;
      while (n>0) {
        n = n >>1;
        numDigits++;
      }

      int valid = true;
      VI facts;
      FORI(j, 2, 11) {
        LL val = 0;
        FORI(k, 0, numDigits) {
          if (N & (1<<k))
            val = val + (LL)pow(j, k);
        }
        if (isPrime(val, facts)) {
          valid = false;
          break;
        }
      }
      if (valid) {
        addAns(numDigits, N, facts);
        if ((int)ansMap.size() >= J)
          return;
      }
    }


  }


  void print() {
    int count = 0;
    for (auto p : ansMap) {
      if (count >= J)
        return;
      count++;
      cout << p.first;
      for (auto e : p.second) {
        cout << " " << e;
      }
      cout << endl;
    }
  }

};



int main() {
  int t;
  cin >> t;
  FORI(i,1,t+1) {

    int N, J;
    cin >> N >> J;

    Prob prob;
    prob.solve(N, J);
    cout << "Case #: " << i << endl;

    prob.print();


  }

  return 0;
}


