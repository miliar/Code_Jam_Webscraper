// C++11, boost with gmp library
#include <iostream>
#include <bitset>
#include <cmath>
#include <algorithm>
#include <cstdlib>
#include <stdint.h>
#include <boost/multiprecision/cpp_int.hpp>
#include <boost/multiprecision/gmp.hpp>

using namespace std;

#define SAMPLE_TEST 0
#define SMALL_TEST 1
#define LARGE_TEST 2
#define OTHER_TEST 3

#define TEST_MODE OTHER_TEST

#if TEST_MODE == SAMPLE_TEST
constexpr int N = 6;
constexpr int J = 3;
#elif TEST_MODE == SMALL_TEST
constexpr int N = 16;
constexpr int J = 50;
#elif TEST_MODE == OTHER_TEST
constexpr int N = 16;
constexpr int J = 500;
#else
constexpr int N = 32;
constexpr int J = 500;
#endif
constexpr int N2 = N*2;






//typedef long long int lli;
//typedef long long int lli_n;

typedef int64_t lli;
typedef int64_t lli_n;

constexpr lli LIMIT = pow(10, N/2);

vector<lli> primes_list;

vector<string> small_solutions;
vector<vector<lli> > small_divisors;

int num = 0;

int num_j = 0;


/// @file     segmented_sieve.cpp
/// @author   Kim Walisch, <kim.walisch@gmail.com>
/// @brief    This is a simple implementation of the segmented sieve of
///           Eratosthenes with a few optimizations. It generates the
///           primes below 10^9 in 0.9 seconds (single-threaded) on an
///           Intel Core i7-4770 CPU (3.4 GHz) from 2013.
/// @license  Public domain.
/// http://primesieve.org/segmented_sieve.html

/// Set your CPU's L1 data cache size (in bytes) here
const int L1D_CACHE_SIZE = 32768;


/// Generate primes using the segmented sieve of Eratosthenes.
/// This algorithm uses O(n log log n) operations and O(sqrt(n)) space.
/// @param limit         Sieve primes <= limit.
/// @param segment_size  Size of the sieve array in bytes.
///
vector<lli> generate_primes_segmented_sieve(int64_t limit, int segment_size = L1D_CACHE_SIZE)
{
  lli_n sqrt_l = (lli_n) std::sqrt((double) limit);
  int64_t count = (limit < 2) ? 0 : 1;
  int64_t s = 2;
  int64_t n = 3;
  vector<lli> all_primes =  (limit < 2) ? vector<lli>{} : vector<lli>{2};


  // vector used for sieving
  std::vector<char> sieve(segment_size);

  // generate small primes <= sqrt
  std::vector<char> is_prime(sqrt_l + 1, 1);
  for (lli_n i = 2; i * i <= sqrt_l; i++)
    if (is_prime[i])
      for (lli_n j = i * i; j <= sqrt_l; j += i)
        is_prime[j] = 0;

  std::vector<lli_n> primes;
  std::vector<lli_n> next;

  for (int64_t low = 0; low <= limit; low += segment_size)
  {
    std::fill(sieve.begin(), sieve.end(), 1);

    // current segment = interval [low, high]
    int64_t high = std::min(low + segment_size - 1, limit);

    // store small primes needed to cross off multiples
    for (; s * s <= high; s++)
    {
      if (is_prime[s])
      {
        primes.push_back((lli_n) s);
          next.push_back((lli_n)(s * s - low));
      }
    }
    // sieve the current segment
    for (std::size_t i = 1; i < primes.size(); i++)
    {
      lli_n j = next[i];
      for (lli_n k = primes[i] * 2; j < segment_size; j += k)
        sieve[j] = 0;
      next[i] = j - segment_size;
    }

    for (; n <= high; n += 2)
      if (sieve[n - low]){ // n is a prime
        count++;
        all_primes.push_back(n);
      }
  }

  std::cerr << count << " primes found." << std::endl;

  return all_primes;
}


/**
 * Fast integer exponentiation using exponentiation by squaring
 * @brief ipow
 * @param base
 * @param exp
 * @return
 */
template<typename T>
int ipow(T base, T e)
{
    T result = 1;
    while (e)
    {
        if (e & 1)
            result *= base;
        e >>= 1;
        base *= base;
    }

    return result;
}


///* this function calculates (a*b)%c taking into account that a*b might overflow */
//lli mulmod(lli a,lli b,lli c){
//    lli x = 0,y=a%c;
//    while(b > 0){
//        if(b%2 == 1){
//            x = (x+y)%c;
//        }
//        y = (y*2)%c;
//        b /= 2;
//    }
//    return x%c;
//}

// uint64_t
lli mulmod(lli a, lli b, lli m) {
    lli res = 0;
    while (a != 0) {
        if (a & 1) res = (res + b) % m;
        a >>= 1;
        b = (b << 1) % m;
    }
    return res;
}

/**
 * This function calculates (a**b)%c
 * @brief modulo_exponentiation
 * @param a
 * @param b
 * @param c
 * @return
 */
int modulo_exponentiation(lli a,lli b,lli c){
    lli x=1,y=a; // long long is taken to avoid overflow of intermediate results
    while(b > 0){
        if(b%2 == 1){
            //x=(x*y)%c;
            x = mulmod(x, y, c);
        }
        //y = (y*y)%c; // squaring the base
        y = mulmod(y, y, c); // squaring the base
        b /= 2;
    }
    return x%c;
}

/**
 * Possibility of overflow for large integer??
 * Check this code https://rosettacode.org/wiki/Miller%E2%80%93Rabin_primality_test#Deterministic_up_to_341.2C550.2C071.2C728.2C321
 * which also seems to be prone to overflow error.
 * Test if it correctly finds that this number 1011111111111 is prime if interpreted as base 10 or 9.
 * Miller-Rabin deterministic primality test
 * https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test#Deterministic_variants_of_the_test
 * @brief is_prime_Miller_Rabin
 * @return
 */
bool is_prime_Miller_Rabin(lli n){

    if(n%2 == 0) return false;

    // Write n-1 as (2**s)*d
    lli d = n-1;
    lli s = 0;
    while(d%2 == 0){

        d /= 2;
        s++;
    }

    lli two = 2;
    lli one = 1;

    vector<lli> as;

    if(n < 2047){
        as = {2};
    } else if(n < 1373653){
        as = {2,3};
    } else if(n < 9080191){
        as = {31,73};
    } else if(n < 25326001){
        as = {2,3, 5};
    } else if(n < 3215031751){
        as = {2,3, 5, 7};
    } else if(n < 4759123141){
        as = {2,7, 61};
    } else if(n < 1122004669633){
        as = {2, 13, 23, 1662803};
    }
    else if(n <  2152302898747){
        as = {2,3, 5, 7, 11};
    } else if(n <  3474749660383){
        as = {2,3, 5, 7, 11, 13};
    } else if(n <  341550071728321){
        as = {2,3, 5, 7, 11, 13, 17};
    } else if(n <  3825123056546413051){
        as = {2,3, 5, 7, 11, 13, 17, 19, 23};
    } else if(n <  18446744073709551616.){
        as = {2,3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37};
    } else{
        as = vector<lli>(0, min(n-1, (lli)ceil(two*pow(log(n), 2)))-1);
        iota(as.begin(), as.end(), 2);
    }




    //for(lli a = two; a <= min(n-1, (lli)ceil(two*pow(log2(n), 2))); a++){
    for(auto& a:as){

        lli count = 0;

        //bool first_cond = (modulo_exponentiation(a, d, n) != 1);

        bool first_cond = (modulo_exponentiation(a, d, n)-1)%n != 0;

        auto y = d;

        for(lli r=0; r<=s-1; r++){

            //auto mod = modulo_exponentiation(a, (ipow(two, r))*d, n) ;
            auto mod = modulo_exponentiation(a, y, n) ;

            //if((first_cond && (mod != n-1) && (mod != -1))){
            if((first_cond && ((mod+1)%n != 0))){

                  count++;

            }

            y *= 2;
        }

        if(count == s) return false;
    }

    return true;

}


lli get_one_divisor(lli n){

    lli sqrt_n = (lli) std::sqrt((double) n) + 1;

    for(auto&prime: primes_list){
        if(prime > sqrt_n) return -1;
        if(n%prime == 0) return prime;
    }
}


template<typename T>
void generate_all_combination(bitset<N>&b, T& func, int pos){

    if(num_j >= J) return;

    if(pos == N-1){

        func(b.to_string());
        return;
    }

    b.set(pos);
    generate_all_combination(b, func, pos+1);
    b.reset(pos);
    generate_all_combination(b, func, pos+1);

}






void solve_small(string b){

    for(int base = 2; base <= 10; base++){

        lli jamcoin = stoll(b, nullptr, base);

        if(is_prime_Miller_Rabin(jamcoin)){
            num++;
            //cerr<<"Prime: "<< jamcoin<<"\t";
            return;
        }
    }

    vector<lli> divisors(11, -1);

    for(int base = 2; base <= 10; base++){
        lli jamcoin = stoll(b, nullptr, base);
        divisors[base] = get_one_divisor(jamcoin);
        // This should never happens but it is happening due to error in is_prime_Miller_Rabin
        if(divisors[base] == -1) return;
    }

    num_j ++;

    // Filling solution for small input
    vector<lli> sol(9, -1);

    for(int i=2; i<= 10; i++){
        sol[i-2] = divisors[i];
    }
    small_solutions.push_back(b);
    small_divisors.push_back(sol);

    #if TEST_MODE == SMALL_TEST
    cout<<stoll(b, nullptr, 10);

    for(int base = 2; base <= 10; base++){
        //lli jamcoin = stoll(b, nullptr, base);
        cout<<" "<<divisors[base];
    }
    cout<<endl;
    #endif

}

void test_small(){

    int t,n,j;
    cin>>t>>n>>j;
    cout<<"Case #1:"<<endl;

    bitset<N> b;
    b.set(0);
    b.set(N-1);
    generate_all_combination(b, solve_small, 1);
    cerr<<"num prime " <<num<<endl;
    cerr<<"num jamcoin found "<<num_j<<endl;
}

void test_big(){
    test_small();
    int num_failures = 0;
    for(int i=0; i<small_solutions.size(); i++){


        string s = small_solutions[i];
        s = s + s;
        cout<<s;
        //auto us = bitset<N2>(s).to_ullong();

        for(int base=2; base<=10; base++){

            //auto us = stoull(s, nullptr, base);
            //boost::multiprecision::int128_t us(s.c_str(), base);
            //boost::multiprecision::cpp_set_str(2);

            boost::multiprecision::mpz_int us;
            mpz_set_str(us.backend().data(), s.c_str(), base );

            boost::multiprecision::mpz_int bb = small_divisors[i][base-2];

            boost::multiprecision::mpz_int big_zero = 0;
            if(i == 0) cerr<<us<<endl;

            if(us%bb == big_zero){
                cout<<" "<<small_divisors[i][base-2];
            } else {
                //cout<<" "<<small_divisors[i][base-2];
                //if(i== 0) cerr<<us%bb<<endl;
                cout<<" -1";
                num_failures++;
            }
        }
        cout<<endl;
    }

    cerr<<" failures "<<num_failures<<endl;
}



int main()
{

    cerr<<"Is 1001011111111111 prime? "<<is_prime_Miller_Rabin(1001011111111111)<<endl;
    cerr<<"Is 15 prime? "<<is_prime_Miller_Rabin(15)<<endl;
    cerr<<"Is 12 prime? "<<is_prime_Miller_Rabin(12)<<endl;

    string b = "1000000000000001";
    for(int base = 2; base <= 10; base++){

        lli jamcoin = stoll(b, nullptr, base);

        if(is_prime_Miller_Rabin(jamcoin)){
            cerr<<"IPrime: "<< jamcoin<<"\t";
        }
    }
    //cerr<<"Is 1001011111111111 prime is_prime_mr? "<<is_prime_mr(1001011111111111)<<endl;

    primes_list = generate_primes_segmented_sieve(LIMIT);
    //sort(primes_list.begin(), primes_list.end());
//    for(auto prime:primes_list){
//        cerr<<prime<<"\t";
//    }
//    cerr<<endl;

    #if TEST_MODE == SMALL_TEST
    test_small();
    #endif

    test_big();
    //cerr<<"Is 11 prime? "<<is_prime_Miller_Rabin(5)<<endl;

    return 0;
}

