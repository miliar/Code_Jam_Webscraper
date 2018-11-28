#include <iostream>
#include <string>
#include <cmath>
#include <vector>

using namespace std;

// N - length of jamcoin ( 2^14 because first is a 1 and last is a 1)
// J - can we produce J different jamcoins (J <= 50)
// total number of jamcoins : 2^N ; or 2^14 = 16384

int primes[2090000] = {};

int total_primes = 2;

int currentJ = 0;

string A;

void generate_primes() {
  primes[0] = 2;
  primes[1] = 3;

  for (int i=2; i<34000000; i++)
    for (int j=2; j*j<=i; j++)
    {
        if (i % j == 0)
            break;
        else if (j+1 > sqrt(i)) {
          total_primes++;
          primes[total_primes-1] = i;
        }
    }
}

long long convert_to_base(string S, int base) {
  long long result = 0;
  long long pow = 1;

  for (int i=S.size()-1; i>=0; i--) {
    if (S[i] == '1') {
      result += pow;
    }

    pow *= base;
  }

  return result;
}

void inspect(string B) {
  int i;

  vector<int> divisors;

  for (i=2; i<=10; i++) {
    long long currentVal = convert_to_base(B, i);

    bool found = false;

    // try to divide by all primes
    for (int j=0; j<total_primes && primes[j] < currentVal; j++) {
      if (currentVal % primes[j] == 0) {
        divisors.push_back(primes[j]);
        found = true;
        break;
      }
    }

    if (!found) {
      break;
    }
  }

  if (i == 11) {
    currentJ++;

    cout << B << " ";

    for (int k=0; k<divisors.size(); k++) {
      cout << divisors[k] << " ";
    }

    cout << endl;
  }
}

void binary(int n, int J)
{
    if (J == currentJ) {
      return;
    }

    if (n < 1) {
      inspect("1" + A + "1");
    }
    else
    {
        A[n-1] = '0';
        binary(n-1, J);
        A[n-1] = '1';
        binary(n-1, J);
    }
}

void solve(int N, int J, int case_num) {
  cout << "Case #" << case_num << ":" << endl;

  // iterate all jamcoins
  binary(N-2, J);
}

int main() {
  generate_primes();

  int T;
  cin >> T;

  for (int i=0; i<T; i++) {
    currentJ = 0;

    int N;
    int J;

    cin >> N >> J;

    A = string(N-2, 'x');

    solve(N, J, i+1);
  }

  return 0;
}

