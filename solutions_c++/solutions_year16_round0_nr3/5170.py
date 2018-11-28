/*
*  multibyte_sieve.cpp
*  Generate a table of primes, and use it to factorize numbers.
*
*  Created by David Krauss on 10/12/10.
*
*/

#include <cmath>
#include <bitset>
#include <limits>
#include <memory>
#include <vector>
#include <fstream>
#include <sstream>
#include <iostream>
#include <iterator>
#include <stdint.h>
#include <inttypes.h>
using namespace std;

char const primes_filename[] = "primes";
enum { encoding_base = (1 << numeric_limits< unsigned char >::digits) - 2 };

template< typename It >
unsigned decode_gap(It &stream) {
  unsigned gap = static_cast< unsigned char >(*stream++);

  if (gap) return 2 * gap; // only this path is tested

  gap = (decode_gap(stream) / 2 - 1) * encoding_base; // deep recursion
  return gap + decode_gap(stream); // shallow recursion
}

template< typename It >
void encode_gap(It &stream, uint32_t gap) {
  unsigned len = 0, bytes[4];

  gap /= 2;
  do {
    bytes[len++] = gap % encoding_base;
    gap /= encoding_base;
  } while (gap);

  while (--len) { // loop not tested
    *stream++ = 0;
    *stream++ = bytes[len + 1];
  }
  *stream++ = bytes[0];
}

template< uint64_t lim >
void generate_primes() {
  auto_ptr< bitset< lim / 2 > > sieve_p(new bitset< lim / 2 >);
  bitset< lim / 2 > &sieve = *sieve_p;

  ofstream out_f(primes_filename, ios::out | ios::binary);
  ostreambuf_iterator< char > out(out_f);

  size_t count = 0;

  size_t last = sqrtl(lim) / 2 + 1, prev = 0, x = 1;
  for (; x != last; ++x) {
    if (sieve[x]) continue;
    size_t n = x * 2 + 1; // translate index to number
    for (size_t m = x + n; m < lim / 2; m += n) sieve[m] = true;
    encode_gap(out, (x - prev) * 2);
    prev = x;
  }

  //auto xx = lim;

  for (; x != lim / 2; ++x) {
    if (sieve[x]) continue;
    encode_gap(out, (x - prev) * 2);
    prev = x;
  }

  cout << prev * 2 + 1 << endl;
}

template< typename I >
vector<I> factorize(I n) {
  ifstream in_f(primes_filename, ios::in | ios::binary);
  if (!in_f) {
    cerr << "Could not open primes file.\n"
      "Please generate it with 'g' command.\n";
    return vector<I>();
  }

  vector<I> factors;

  while (n % 2 == 0) {
    n /= 2;
    //cout << "2 ";
    factors.push_back(2);
  }
  unsigned long factor = 1;

  for (istreambuf_iterator< char > in(in_f), in_end; in != in_end;) {
    factor += decode_gap(in);

    while (n % factor == 0) {
      n /= factor;
      //cout << factor << " ";
      factors.push_back(factor);
    }

    if (n == 1) goto finish;
  }

  factors.push_back(n);

finish:
  //cout << endl;
  return factors;
}

template <size_t numBits>
bitset<numBits> nextCoin(bitset<numBits> coinIni, vector<uint64_t>& divisorsOut)
{
  auto coinToBase = [](bitset<numBits>& coin, int base)
  {
    uint64_t result = 0;
    uint64_t baseMul = 1;
    for (int i = 0; i < numBits; ++i)
    {
      result += coin[i] * baseMul;
      baseMul *= base;
    }
    return result;
  };

  auto checkCoinForBase = [&](bitset<numBits>& coin, int base, uint64_t& divisorOut)
  {
    auto coinInBase = coinToBase(coin, base);
    auto factorization = factorize(coinInBase);
    if (factorization.size() == 1 && factorization[0] == coinInBase)
      return false;

    divisorOut = factorization.back();
    return true;
  };

  auto isValidCoin = [](bitset<numBits>& coin)
  {
    return coin[0] && coin[numBits - 1];
  };


  auto coinVal = coinIni.to_ullong() + 1;
  while (true)
  {
    bitset<numBits> coin(coinVal);

    if (isValidCoin(coin))
    {
      divisorsOut.clear();

      for (int base = 2; base <= 10; ++base)
      {
        uint64_t divisor;
        if (checkCoinForBase(coin, base, divisor))
        {
          divisorsOut.push_back(divisor);
        }
      }

      if (divisorsOut.size() == 9)
      {
        return coin;
      }
    }

    coinVal += 1;
  }
}

int main(int argc, char *argv[])
{
  //auto print_help = [&]()
  //{
  //  cerr << "Usage:\n\t" << argv[0] << " <number> -- factorize number.\n"
  //    "\t" << argv[0] << " g -- generate primes file in current directory.\n";
  //  return 0;
  //};
  //

  //if (argc != 2) return print_help();

  //uint64_t n;
  //if (argv[1][0] == 'g') {
  //  generate_primes< (1ull << 32) >();
  //}
  //else if ((istringstream(argv[1]) >> n).rdstate() == ios::eofbit)
  //  factorize(n);
  //else goto print_help;

  //n = (1ull << 32) - 1;
  //factorize(n);

  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);

  int numTestCases, jamCoinLength, numJamCoins;
  scanf("%d%d%d", &numTestCases, &jamCoinLength, &numJamCoins);

  auto coinPrev = bitset<16>(0);
  while (numJamCoins)
  {
    if (coinPrev.all())
    {
      printf("FAIL");
      return 0;
    }
      

    vector<uint64_t> divisors;
    auto coin = nextCoin<16>(coinPrev, divisors);
    auto coinStr = coin.to_string();
    //std::reverse(coinStr.begin(), coinStr.end());
    cout << coinStr;
    for (int i = 0; i < divisors.size(); ++i)
      printf(" %" SCNu64, divisors[i]);
    printf("\n");

    coinPrev = coin;
    numJamCoins -= 1;

    cerr << numJamCoins << endl;
  }
  

 return 0;
}