#include <iostream>
#include <random>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <ctime>
#include <cmath>

using namespace std;

string jamcoinToString(vector<int> j) {
  string jamcoin = "";
  for (unsigned int i = 0; i < j.size(); i++) {
    if (j[i] == 1) {
      jamcoin += "1";
    } else {
      jamcoin += "0";
    }
  }
  return jamcoin;
}

vector<int> generateJamcoin(int N) {
  vector<int> jamcoin {};
  jamcoin.push_back(1);
  for (int k = 0; k < N - 2; k++) {
    jamcoin.push_back( rand() % 2 == 0 );
  }
  jamcoin.push_back(1);
  return jamcoin;
}

vector<int> getJamcoin(signed long long number) {
  if(number <= 1) {
    vector<int> jamcoin {number};
    return jamcoin;
  }
  int remainder = number % 2;
  vector<int> result = getJamcoin(number >> 1);
  result.push_back(remainder);
  return result;
}

signed long long getNumber(vector<int> jamcoin, int radix) {
  signed long long number = 0;
  unsigned int length = jamcoin.size() - 1;
  for (unsigned int i = 0; i < jamcoin.size(); i++) {
    number += pow(radix, i) * jamcoin[length - i];
  }
  return number;
}

// inline bool isPrime(int number) {
//   // if ( ( (!(number & 1)) && number != 2 ) || (number < 2) || (number % 3 == 0 && number != 3) )
//   //   return (false);
//   //
//   // for( int k = 1; 36*k*k-12*k < number;++k)
//   //   if ( (number % (6*k+1) == 0) || (number % (6*k-1) == 0) )
//   //     return (false);
//   // return true;
//
// }

inline signed long long getDivisor(signed long long num) {
  signed long long square_root = (signed long long) sqrt(num) + 1;
  for (signed long long i = 2; i < square_root; i++) {
    if(num % i == 0) {
      return i;
    }
  }
  return -1; // shouldn't be prime
}

vector<int> generateValidJamcoin(int N, vector<signed long long> &usedJamcoins) {
  bool valid = false;
  vector<int> jamcoin;
  signed long long id;
  while(!valid) {
    valid = true;

    jamcoin = generateJamcoin(N);

    id = getNumber(jamcoin, 2);
    // cout << " what? " << id << " " << getDivisor(id) << endl;
    if (getDivisor(id) == -1 || (find(usedJamcoins.begin(), usedJamcoins.end(), id) != usedJamcoins.end())) {
      valid = false;
      continue;
    }
    cout << id << " " << jamcoinToString(getJamcoin(id)) << " " << jamcoinToString(jamcoin) << endl;
    for (int radix = 3; radix <= 10; radix++) {
      signed long long number = getNumber(jamcoin, radix);
      if (getDivisor(number) == -1) {
        valid = false;
        break;
      }
    }
  }
  usedJamcoins.push_back(id);
  return jamcoin;
}

vector<int> getNextValidJamcoin(signed long long &currentPos, int max) {
  bool valid = false;
  vector<int> jamcoin;
  while(!valid) {
    valid = true;

    currentPos += 2;

    if (currentPos > max) break;

    // cout << " what? " << id << " " << getDivisor(id) << endl;
    if (getDivisor(currentPos) == -1) {
      valid = false;
      continue;
    }

    jamcoin = getJamcoin(currentPos);
    // cout << currentPos << " " << jamcoinToString(jamcoin) << endl;

    for (int radix = 3; radix <= 10; radix++) {
      signed long long number = getNumber(jamcoin, radix);
      signed long long divisor = getDivisor(number);
      // cout << number << " " << divisor << endl;
      if (divisor == -1) {
        valid = false;
        break;
      }
    }
  }
  return jamcoin;
}

void printResult(vector<int> jamcoin) {
  cout << jamcoinToString(jamcoin) << " ";
  for (int radix = 2; radix <= 10; radix++) {
    signed long long number = getNumber(jamcoin, radix);
    signed long long divisor = getDivisor(number);
    cout << divisor << " ";
  }
  cout << endl;
}

int main() {
  srand((unsigned)time(0));

  int t;
  cin>>t;

  for (int i = 0; i < t; i++) {

    int N, J;
    cin>>N;
    cin>>J;

    vector<int> minJamcoin {1};
    for (int k = 0; k < N - 2; k++) {
      minJamcoin.push_back(0);
    }
    minJamcoin.push_back(1);

    vector<int> maxJamcoin;
    for (int k = 0; k < N; k++) {
      maxJamcoin.push_back(1);
    }

    signed long long min = getNumber(minJamcoin, 2);
    signed long long max = getNumber(maxJamcoin, 2);
    signed long long currentPos = min - 2;

    // cout << "min: " << min << " max: " << max << endl;

    cout << "Case #" << (i+1) << ": " << endl;
    for (int k = 0; k < J; k++) {
      vector<int> jamcoin = getNextValidJamcoin(currentPos, max);
      printResult(jamcoin);
    }
  }

  return 0;
}
