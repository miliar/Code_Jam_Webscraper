#include <algorithm>
#include <cstddef>
#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <math.h>
#include <iomanip>
#include <vector>

#define SSTR( x ) static_cast< ostringstream & >( \
        ( ostringstream() << dec << x ) ).str()

using namespace std;

const int N_BASES = 9;
int BASES[N_BASES];

vector<int> sieveOfSundaram(int inputNumber) {
  int totalPrimes = 0; 
  int TheseArePrime = 0;
     int n = inputNumber / 2;
 
     int isPrime [inputNumber]; 
     vector<int> result = vector<int>();
 
     for (int i = 0; i < inputNumber; i++)
     {
        isPrime[i] = i + 1;
     }
 
     for (int i = 1; i < n; i++)
     {
         for (int j = i;  j<= (n-i)/(2*i+1); j++)
         {
            isPrime[i + j + 2 * i * j] = 0;
         }
     }
        if (inputNumber >= 2)
        {
            isPrime[TheseArePrime++] = 2;
            totalPrimes++;
        }
 
         for (int i = 1; i < n; i++)
        {
            if (isPrime[i] != 0)
            {
                isPrime[TheseArePrime++]=i*2+1;
                totalPrimes++;
            }
        }
 
        for (int x = 0; x < totalPrimes; x++)
        {
            if (isPrime[x]!= 0)
            {
                result.push_back(isPrime[x]);
            }
            else
            {
                break;
            }
        }

        return result;
}

int readInt() {
  int result;
  cin >> result;

  return result;
}

void printCaseResult(int caseNo) {
  cout << "Case #" << caseNo << ":" << endl;
}

class JamcoinGen {
  int m_length;
  long long m_curr;
  long long m_max;
  int* m_divisors;

  string nextJamcoinCandidate() {
    stringstream result("");
    result << 1;
    int position = m_length;
    long currentNumber = m_curr;
    while (position-- > 0) {
      result << (char)(48 + (currentNumber & 1));
      currentNumber >>= 1;
    }

    result << 1;
    if (m_curr++ > m_max) {
      cout << "Did not find next jamcoin candidate!";
      throw NULL;
    }

    return result.str();
  }

  static int getFirstNonTrivialDivisor(long long number) {
    for(vector<int>::const_iterator it = primes.begin();
        it != primes.end();
        it++) {
      int prime = *it;
      if (prime > number)       return -1;
      if (number % prime == 0)  return prime;
    }

    return -1;
  }

  static bool getJamcoinNonTrivialDivisors(string jamcoin, int* result) {
    const char* cstr = jamcoin.c_str();
    for (int i = 0; i < N_BASES; i++) {
      int base = BASES[i];
      long long jamcoinValueInBase = strtoll(cstr, 0, base);
      int divisor = getFirstNonTrivialDivisor(jamcoinValueInBase);
      if (divisor == -1) return false;

      result[i] = divisor;
    }

    return true;
  };


  public:
    JamcoinGen(int length): 
      m_length(length-2), 
      m_curr(0),
      m_max(1 << (length - 2)),
      m_divisors(new int[N_BASES]) {}

    ~JamcoinGen() {
      delete[] m_divisors;
    }

    string nextJamcoin() {
      string candidate;
      do {
        candidate = nextJamcoinCandidate();
      } while (!getJamcoinNonTrivialDivisors(candidate, m_divisors));

      ostringstream result("");
      result << candidate;
      for (int i = 0; i < N_BASES; i++) {
        result << " " << m_divisors[i];
      }

      return result.str();
    };

    static const vector<int> primes;
};

const vector<int> JamcoinGen::primes = sieveOfSundaram(20000);


void solveCase(int caseNo) {
  int jamcoinLength = readInt();
  int numberOfJamcoins = readInt();
  JamcoinGen gen(jamcoinLength);
  printCaseResult(caseNo);
  while(numberOfJamcoins-- > 0) {
    cout << gen.nextJamcoin() << endl;
  }
}


int main() {
  for (int i = 0; i < N_BASES; i++) {
    BASES[i] = i+2;
  }

  const int totalCases = readInt();
  int casesLeft = totalCases;


  while (casesLeft-- > 0) {
    solveCase(totalCases - casesLeft);
  }

  return 0;
}
