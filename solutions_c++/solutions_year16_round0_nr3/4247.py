#include <iostream>
#include <sstream>
#include <vector>
#include <cmath>


using namespace std;

class CoinJam {

  vector<long long> currentOrder;

  long long currentJamCount;
  long long maxJamCount;

  long long powerMod(long long b, long long e, long long m)
  {
    long long remainder;
    long long x = 1;

    while (e != 0)
    {
      remainder = e % 2;
      e= e/2;

      if (remainder == 1)
        x = (x * b) % m;
      b= (b * b) % m;
    }
    return x;
  }

  bool isPrime(long long p){
    long long size = (long long)sqrt(p);
    for (long long i = 2; i < size; ++i) {
      if (p % i == 0){
        return false;
      }
    }
    return true;
  };

  long long getFactor(long long p) {
    long long size = (long long)sqrt(p);
    for (long long i = 2; i < size; ++i) {
      if (p % i == 0){
        return i;
      }
    }
    return -1;
  }

  bool isJam() {
    for (long long i = 2; i <= 10; ++i) {
      if(isPrime(getKBasedNum(i))){
        return false;
      }
    }
    cout << getKBasedNum(10);
    for (long long i = 2; i <= 10; ++i) {
      cout << " " << getFactor(getKBasedNum(i));
    }
    cout << endl;
    return true;
  }

  long long getKBasedNum(long long k) {
    long long result = 0;
    for (long long i = 0; i < currentOrder.size(); ++i) {
      long long factor = 1;
      for (long long j = (long long) currentOrder.size() - i - 1; j > 0; --j) {
        factor *= k;
      }
      stringstream ss;
      long long digit = 0;
      ss << currentOrder[i];
      ss >> digit;
      result += factor * digit;
    }
    return result;
  }

 public:

  void getAllSituations() {
    currentOrder[0] = 1;
    currentOrder.back() = 1;
    dfs(0, 1);
  }

  bool dfs(long long lineIndex, long long bit) {

    currentOrder[lineIndex] = bit;

    if (currentJamCount >= maxJamCount) {
      return true;
    }

    if (lineIndex == currentOrder.size() - 1 ) {
      if (currentOrder.back() == 1) {
        if (isJam()) {
          currentJamCount++;
        }
      }
      return false;
    }

    if (dfs(lineIndex + 1, 0)) {
      return true;
    }
    if (dfs(lineIndex + 1, 1)) {
      return true;
    }
    return false;
  }

  CoinJam(size_t originLength, long long maxCount)
      :currentOrder(originLength, 0),
       maxJamCount(maxCount),
       currentJamCount(0)
  {}
};

int main() {
  long long caseNum;
  cin >> caseNum;
  for (long long i = 1; i <= caseNum; ++i) {
    long long n, m;
    cin >> n >> m;
    cout << "Case #" << i << ":" << endl;
    CoinJam(n, m).getAllSituations();
  }
  return 0;
}