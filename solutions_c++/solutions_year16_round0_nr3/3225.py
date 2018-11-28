#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <unordered_set>
#include <unordered_map>
#include <fstream>
#include <queue>
#include <stack>
#include <list>
#include <sstream>
#include <bitset>
#include <algorithm>
#include <utility>
#include <climits>
using namespace std;

#define gcd(a, b) if (!b) ? return a : return gcd(b, a % b);
#define lcm(n, m) (m * n) / gcd(m, n);

#define print(v) for (int i = 0; i < v.size(); ++i) cout << v[i] << " "; cout << endl;
template <class T>
void printMatrix(vector< vector< T > >& matrix) {
  for (int i = 0; i < matrix.size(); ++i) {
    for (int j = 0; j < matrix[i].size(); ++j) {
      cout << matrix[i][j] << " ";
    }
    cout << endl;
  }
  cout << endl;
}

typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector< ii > vii;

const int UNVISITED = -1;
const int VISITED = 1;
const int INF = 1000000005;

vector<vi> AdjMatrix;
vector<int> dfs_num;

void sieve(vector<bool>& primes) {
  for (int i = 2; i < primes.size(); ++i) {
    if (primes[i]) {
      for (int j = 2 * i; j < primes.size(); j += i)
	primes[j] = false;
    }
  }
}

pair<bool, long long> isPrime(long long k, vector<bool>& primes ) {
  for (int i = 2; i <= sqrt(k) && i < primes.size(); ++i) {
    if (primes[i] && (k % i == 0)) return pair<bool, long long>(false, i);
  }
  return pair<bool, long long>(true, k);
}

vector<int> binary(long long n) {
  vector<int> v;
  while (n) {
    v.push_back(n % 2);
    n /= 2;
  }
  return v;
}

long long convert(vector<int>& v, int base) {
  long long n = 0;
  for (int i = 0; i < v.size(); ++i) {
    if (v[i]) n += pow(base, i);
  }
  return n;
}

pair< bool, vector<int> > isJamcoin(vector<int>& v, vector<bool>& primes) {
  vector<int> divisors;
  for (int i = 2; i <= 10; ++i) {
    long long n = convert(v, i);
    pair<bool, int> check = isPrime(n, primes);
    if (!check.first) divisors.push_back(check.second);
    else return pair <bool, vector<int> >(false, vector<int>());
  }
  return pair<bool, vector<int> >(true, divisors);
}

void findJamcoins(long long start, long long end, vector< pair< vector<int>, vector< int> > >& jamcoins, int total,
		  vector<bool>& primes) {
  for (long long i = start; i < end; ++i) {

    if (!isPrime(i, primes).first) {
      vector<int> b = binary(i);
      if (b[0] && b.back()) {
      pair<bool, vector<int> > check = isJamcoin(b, primes);
      if (check.first) {
	jamcoins.push_back(pair< vector<int>, vector<int> >(b, check.second));
      }
      }
    }
    
    if (total == jamcoins.size()) return;
  }
}

int main() {
  vector<bool> primes(65536, true);
  primes[0] = false;
  primes[1] = false;
  sieve(primes);

  int n, case_num = 1;
  cin >> n;
  while (n--) {
    int a, b;
    cin >> a >> b;

    long long num = 0;
    for (int i = 0; i < a; ++i) {
      if (i == 0 || i == a - 1) {
	num += pow(2, i);
      }
    }
    
    vector< pair< vector<int>, vector<int> > > jamcoins;
    findJamcoins(num, pow(2, a), jamcoins, b, primes);
    
    cout << "Case #" << case_num++ << ":" << endl;
    for (int i = 0; i < jamcoins.size(); ++i) {
      for (int j = jamcoins[i].first.size() - 1; j >= 0; --j) {
	cout << jamcoins[i].first[j];
      }

      cout << " ";
      for (int j = 0; j < jamcoins[i].second.size(); ++j) {
	cout << jamcoins[i].second[j] << " ";
      }

      cout << endl;
    }
  }
}
