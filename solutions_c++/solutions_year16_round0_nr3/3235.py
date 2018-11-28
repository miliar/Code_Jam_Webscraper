#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<int> eratostenes;

void initPrimes(int length) {
  eratostenes = vector<int>(length, 0);
  for (long long int i = 2; i*i < length; ++i) {
    if (eratostenes[i] == 0) {
      for (long long int j = 2*i; j < length; j+=i) {
        eratostenes[j] = i;
      }
    }
  }
}

bool isPrimeE(int n) {
  if (eratostenes.size() <= n) initPrimes(2*n);
  return eratostenes[n] == 0;
}

bool isPrime(long long int n) {
  for (long long int i = 2; i*i < n; ++i) {
    if (n%i == 0) return false;
  }
  return true;
}

int getDivisor(long long int n) {
  for (int i = 2; i*i < n; ++i) {
    if (n%i == 0) return i;
  }
  return 0;
}

int getDivisorE(int n) {
  return eratostenes[n];
}

long long int value(string s, int base) {
  long long int sum = 0;
  long long int positionValue = 1;
  for (int i = s.length() - 1; i >= 0; --i) {
    int coef = s[i] - '0';
    sum += coef*positionValue;
    positionValue*=base;
  }
  return sum;
}

string toBinary(int num) {
  string res = "";
  if (num == 0) return "0";
  while(num > 0) {
    res = to_string(num%2) + res;
    num /=2;
  }
  return res;
}

string formatJamcoin(int innerBits10, int length) {
  string innerBits = toBinary(innerBits10);
  int prefixLength = length - innerBits.length() - 2;
  return '1' + string(prefixLength, '0') + innerBits + '1';
}


int main(int argc, char** argv) {
  int T;
  cin >> T;
  int t = 0;
  for (int t = 1; t <= T; ++t) {
    int J, N;
    cin >> N >> J;
    vector<string> answers;
    vector<vector<int> > answersDivisors;
    bool done = false;
    for (int jamcoin10Candidate = 0; not done; ++jamcoin10Candidate) {
      string candidate = formatJamcoin(jamcoin10Candidate, N);
      // cout << "candidate: " << candidate <<  endl;
      bool isJamcoin = true;
      vector<int> divisors;
      for (int base = 2; base <= 10 && isJamcoin; ++base) {
        long long int val = value(candidate, base);
        if (isPrime(val)) {
          //cout << "  is prime in base " << base << ", val = " << val << endl;
          isJamcoin = false;
        } else {
          //cout << " val, div " << val << ", " << getDivisor(val) << endl;
          divisors.push_back(getDivisor(val));
        }
      }
      if (isJamcoin) {
        answers.push_back(candidate);
        answersDivisors.push_back(divisors);
      }
      if (answers.size() == J) done = true;
      if (jamcoin10Candidate == value(string(N-2,'1'), 2)) done = true;
    }
    cout << "Case #" << t << ":" << endl;
    for(int i = 0; i < answers.size(); ++i) {
      cout << answers[i] << " ";
      for (int j = 0; j < answersDivisors[i].size(); ++j) {
        cout << answersDivisors[i][j] << " ";
      }
      cout << endl;
    }
  }
  return 0;
}