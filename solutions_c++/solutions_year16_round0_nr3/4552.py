#include <iostream>
#include <boost/multiprecision/cpp_int.hpp>
#include <vector>
#include <algorithm>
#include <numeric>
#include <iterator>
#include <cstdint>
#include <deque>
#include <string>
#include <bitset>
#include <cmath>
using ll = boost::multiprecision::uint256_t;

template<typename T>
T to_base(const std::string &str_number, T base) {
  auto f = std::begin(str_number);
  auto l = std::end(str_number);
  if (f == l) return 0;
  l--;
  ll s = *l - 48;
  if (f == l) return s;
  l--;
  ll power = base;
  while(l >= f) {
    s += (*l - 48) * power;
    power *= base;
    l--;
  }
  return s;
}



template<typename T>
T smallest_devisor(T x) {
  T max_devisor = std::min(x, (T)(std::sqrt(std::sqrt(std::sqrt((long double)x))) + 5));
  T devisor = 2;
  while (devisor < max_devisor) {
    if (x % devisor == 0) {
      return devisor;
    } 
    devisor++;
  }
  return x;
}

template<size_t N, typename T>
bool process_number(T x) {
  std::bitset<N> bs(x);
  static std::string string_number;
  string_number = bs.to_string();

  ll numbers[9];
  for (int i = 2; i < 11; i++) {
    numbers[i - 2] = to_base<ll>(string_number, i);
  }
  
  ll factors[9];
  int i = 0;
  for (i = 0; i < 9; i++) {
    auto devisor = smallest_devisor(numbers[i]);
    if (devisor == numbers[i]) {
       break;
    } else {
      factors[i] = devisor;
    }
  
  }
  if (i == 9) {
    std::cout << string_number << " ";
    //for (auto x : numbers) {
    //  std::cout << x << " ";
    //}
    for (auto x : factors) {
      std::cout << x << " ";
    }
    std::cout << std::endl;
    return true;
  }
  return false;
}


template<size_t N>
void iter_over(int j) {
  std::bitset<N> bit_bound;
  bit_bound.set();
  auto max_value = bit_bound.to_ulong();
  std::bitset<N> current_value(0);
  current_value[0] = 1;
  current_value[N-1] =  1;
  int count = 0;
  for (auto current_number = current_value.to_ulong();
       current_number < max_value;
       current_number += 2) {
     if (process_number<N>(current_number)) count++; 
     if (count == j) { break; }
  }
}


int main() {
  int n;
  std::cin >> n;
  std::cout << "Case #1:\n";
  iter_over<32>(500);
  return 0;
}
