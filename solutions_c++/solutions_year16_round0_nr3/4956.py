#include <iostream>
#include <vector>
#include <set>
#include <math.h>
using namespace std;

uint64_t base_vals[9][16] =
  {{1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768},
   {1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323, 4782969, 14348907},
   {1, 4, 16, 64, 256, 1024, 4096, 16384, 65536, 262144, 1048576, 4194304, 16777216, 67108864, 268435456, 1073741824},
   {1, 5, 25, 125, 625, 3125, 15625, 78125, 390625, 1953125, 9765625, 48828125, 244140625, 1220703125, 6103515625, 30517578125},
   {1, 6, 36, 216, 1296, 7776, 46656, 279936, 1679616, 10077696, 60466176, 362797056, 2176782336, 13060694016, 78364164096, 470184984576},
   {1, 7, 49, 343, 2401, 16807, 117649, 823543, 5764801, 40353607, 282475249, 1977326743, 13841287201, 96889010407, 678223072849, 4747561509943},
   {1, 8, 64, 512, 4096, 32768, 262144, 2097152, 16777216, 134217728, 1073741824, 8589934592, 68719476736, 549755813888, 4398046511104, 35184372088832},
   {1, 9, 81, 729, 6561, 59049, 531441, 4782969, 43046721, 387420489, 3486784401, 31381059609, 282429536481, 2541865828329, 22876792454961, 205891132094649},
   {1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000, 100000000000, 1000000000000, 10000000000000, 100000000000000, 1000000000000000}};

void print_result(vector<bool> &jamcoin, vector<uint64_t> &divisor) {
  for (int i = jamcoin.size() - 1; i >= 0; i--)
    cout << (jamcoin[i]? "1":"0");
  for (auto div : divisor)
    cout << " " << div;

  cout << endl;
}

void find_divisor(vector<uint64_t> &values, vector<uint64_t> &divisor) {
  set<uint64_t> div_set;
  for (auto v : values) {
    uint64_t div = 2;
    for (; div <= sqrt(v); div++) {
      if ((v % div) == 0 && div_set.find(div) == div_set.end()) {
        div_set.insert(div);
        divisor.push_back(div);
        break;
      }
    }
    if (div == v)
      return;
  }
}

void get_jamcoin(vector<bool> &jamcoin, int n, int &j) {
  if (j == 0)
    return;
  if (n == 0) {
    vector<uint64_t> divisors;
    vector<uint64_t> values(9, 0);
    int idx = 0;
    for (int i = 0; i < jamcoin.size(); i++) {
      for (int base = 2; base <= 10; base++) {
        values[base-2] += jamcoin[i]? base_vals[base-2][i] : 0;
      }
    }
    find_divisor(values, divisors);
    if (divisors.size() == values.size()) {
      print_result(jamcoin, divisors);
      j--;
    }
    return;
  }

  get_jamcoin(jamcoin, n-1, j);
  jamcoin[n] = !jamcoin[n];
  get_jamcoin(jamcoin, n-1, j);
  jamcoin[n] = !jamcoin[n];
}

int main() {
  int t = 1;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    cout << "Case #" << i << ": " << endl;
    int n, j;
    cin >> n >> j;
    vector<bool> jamcoin(n, false);
    jamcoin[n-1] = jamcoin[0] = true;
    get_jamcoin(jamcoin, n-2, j);
  }
}
