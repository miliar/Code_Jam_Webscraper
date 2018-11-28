#include <fstream>
#include <iostream>
#include <range/v3/all.hpp>
#include <sstream>
#include <gsl.h>
namespace rng = ranges::v3;

const char* const primes_filename = "primes-small.out";

const size_t max = 32000;

std::vector<std::size_t>
read_primes()
{
   std::vector<std::size_t> primes(2050943);
   std::ifstream fin(primes_filename);
   rng::copy(rng::istream_range<std::size_t>(fin), rng::begin(primes));
   return primes;
}

std::string make_jamcoin(std::size_t num, int digits)
{
   std::bitset<30> b(num);
   return "1" + b.to_string().substr(30-digits) + "1";
}

std::string next_jamcoin(std::string jamcoin)
{
   int n = jamcoin.size()-2;
   std::string inner = jamcoin.substr(1, n);
   std::size_t num = std::stoull(inner) + 1;
   std::ostringstream conv;
   std::bitset<32> b(num);
   return "1" + b.to_string().substr(32-n) + "1";
}

std::size_t get_divisor(std::size_t n)
{
   if (!(n % 2))
      return 2;
   for (std::size_t div=3; div*div <= n; div += 2)
      if (!(n % div))
         return div;
   return 0;
}

uint64_t power_mod(int base, int exponent, std::size_t m)
{
   if (exponent == 0)
      return 1;
   else if (exponent == 1)
      return base;

   int fst_half = exponent/2;
   int snd_half = exponent-fst_half;
   return (power_mod(base, fst_half, m) * power_mod(base, snd_half, m))%m;
}

uint64_t jam_mod(std::string const& jamcoin, int base, int m)
{
   std::size_t result = 0;
   int n = gsl::narrow<int>(jamcoin.size());
   for (int i = 1; i <= n; ++i)
      if (jamcoin[n-i] == '1') {
         result = (result + power_mod(base,i-1,m))%m;
      }
   return result;
}

std::size_t get_divisor(std::string const& jamcoin, int base)
{
   if (!(jam_mod(jamcoin, base, 2)))
      return 2;
   for (std::size_t div=3; div <= max; div += 2)
      if (!(jam_mod(jamcoin, base, div)))
         return div;
   return 0;
}

int main()
{
   constexpr int exponent = 30;
   constexpr std::size_t max_digits = std::pow(2,exponent);
   std::array<std::size_t,9> reps;


   std::cout << "Case #1:\n";
   int count = 1;
   for (std::size_t i=0; i < max_digits; ++i) {
      std::string jamcoin = make_jamcoin(i,exponent);
      rng::iota(reps,2);
      auto get_divisors = [&jamcoin](std::size_t base) {
            return get_divisor(jamcoin, base);
      };
      rng::action::transform(reps, get_divisors);
      if (rng::all_of(reps, [](std::size_t rep){ return rep != 0; })) {
         std::cout << jamcoin << ' ';
         rng::copy(reps, rng::ostream_iterator<std::size_t>(std::cout," "));
         std::cout << '\n';
         ++count;
      }
      if (count > 500)
         break;
   }
}
