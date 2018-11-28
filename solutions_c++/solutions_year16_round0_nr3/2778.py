

#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
#include <algorithm>
#include <vector>

using namespace std;  // since cin and cout are both in namespace std, this saves some text

bool IsPrime(uint64_t uNum, uint64_t& divisor)
{
  static unsigned int vuPrimes55[] = { 2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,
    73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,
    181,191,193,197,199,211,223,227,229,233,239,241,251,257 };

  unsigned uMaxTest = std::min((unsigned)uNum / 2, (unsigned)55);
  for(unsigned i = 0; i < uMaxTest; i++)
    if(uNum % vuPrimes55[i] == 0){
      if(uNum == vuPrimes55[i])
        return true;
      divisor = vuPrimes55[i];
      return false;
    }

  uMaxTest = static_cast<unsigned>(sqrt((double)uNum));
  for(unsigned u = 2; u < uMaxTest; u += 2){
    if(uNum % u == 0){
      divisor = u;
      return false;
    }
  }
  return true;
}

int main()
{
  int t;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');//for removing trailing spaces to endof line
  for(int i = 1; i <= t; ++i) {
    int N, J;
    cin >> N >> J;
    cout << "Case #" << i << ":"<< endl;
    uint64_t k[11] = { 0 };
    for(int b = 2; b <= 10; ++b){
      k[b] = 1 + static_cast<uint64_t>(pow(b, N - 1));//fisrt/last bits in base
    }
    int j = 0;
    for(uint32_t bits = 0; j<J;++bits){
      uint64_t vDivisors[11];
      bool bFound = true;
      uint64_t val[11] = { 0 };
      for(int b = 2; bFound && b <= 10; ++b){
        val[b] = k[b];
        uint64_t mult = b;
        for(uint32_t x = bits; x; x >>= 1){
          val[b] += (x & 1)*mult;
          mult *= b;
        }
        uint64_t divis=0;
        if(IsPrime(val[b], divis)){
          bFound = false;
        } else{
          vDivisors[b] = divis;
        }
      }
      if(bFound){
        cout << '1';
        for(int idx = N - 3; idx >= 0; idx--)
          cout << ((bits >> idx)&1);
        cout << '1';
        j++;
        for(unsigned d = 2; d <= 10; ++d)
          cout << " " << vDivisors[d];
        cout << endl;
        int dbg=0;
      }
    }
  }

  return 0;
}

