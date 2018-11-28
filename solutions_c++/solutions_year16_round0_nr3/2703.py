#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

vector<long long> primes;

void init_sieve() {
  size_t sizee = 1L << 28L;
  vector<long long> ss(sizee + 3, 1);
  ss[0] = ss[1] = 0;
  for (long long i = 4; i <= sizee; i += 2) {
    ss[i] = 0;
  }
  for (long long i = 3; i <= sizee; i += 2) {
    if (ss[i]) {
      long long cc = 2;
      while (i*cc < sizee) {
        ss[i*cc] = 0;
        cc++;
      }
    }
  }
  primes.push_back(2);
  for (long long i = 3; i < sizee; i += 2) {
    if (ss[i])
      primes.push_back(i);
  }
}

bool is_prime(long long val) {
  return binary_search(primes.begin(), primes.end(), val);
}

long long get_in_base(long long num, int base) {
  long long tmp = num;
  long long res = 0;
  long long m = 1;
  while (tmp) {
    res += (tmp%2)*m;
    tmp /= 2;
    m *= base;
  }
  return res;
}

long long get_div(long long v) {
  for (auto i : primes)
    if ((v%i) == 0)
      return i;
  return 0;
}

string getbin(long long v) {
  string res;

  while (v) {
    res = char('0'+(v%2))+res;
    v /= 2;
  }

  return res;
}

void doit() {
  long long N, J;
  cin >> N >> J;
  for (long long i = 0; i < 1<<(N-2); ++i) {
    long long num = (1<<(N-1)) | (i << 1) | 1;

    vector<long long> bases(9);
    for (int b = 2; b <= 10; ++b) {
      bases[b-2] = get_in_base(num, b);
    }
    bool all_complex = true;

    for (auto a : bases) {
      if (is_prime(a)) {
        all_complex = false;
        break;
      }
    }

    if (!all_complex)
      continue;

    vector<long long> asd;

    for (auto a : bases){
      asd.push_back(get_div(a));
    }
    
    bool www = true;
    for (auto a : asd)
      if (a == 0) {
        www = false;
        break;
      }
    
    if (!www) continue;

    cout << getbin(num) << " ";
    for (auto a : asd) {
      cout << a << " ";
    }
    cout << endl;


    J--;
    if (J==0) return;
  }
}

int main() {
  ios::sync_with_stdio(false);
  init_sieve();
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    cout << "Case #"<<t << ":"<<endl;
    doit();
  }
}
