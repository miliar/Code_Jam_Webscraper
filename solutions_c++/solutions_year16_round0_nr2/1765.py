#include <iostream>
#include <vector>
#include <string>

#include <gsl.h>
#include <range/v3/all.hpp>
#include "gcj.h"

namespace rng = ranges::v3;

std::vector<char> read_stack(std::istream& sin)
{
   Expects(sin);
   std::string line = rng::front(rng::getlines(sin));
   std::vector<char> pancakes;
   for (char c : line) {
      Expects(c == '+' || c == '-');
      pancakes.push_back(c);
   }
   return pancakes;
}

bool is_happy(char pancake)
{
   return pancake == '+';
}

bool is_not_happy(char pancake)
{
   return !is_happy(pancake);
}

char flip(char pancake)
{
   return is_happy(pancake) ? '-' : '+';
}

void flip(gsl::span<char> pancakes)
{
   rng::reverse(pancakes);
   rng::action::transform(pancakes, [](char pancake) { return flip(pancake); });
}

int equal_to_len(gsl::span<char> pancakes, char pancake)
{
   int pos = 0;
   for (char p : pancakes) {
      if (p == pancake)
         pos += 1;
      else
         break;
   }
   return pos;
}

gsl::span<char> first_homogeneous_subseq(gsl::span<char> pancakes)
{
   int len = equal_to_len(pancakes, pancakes[0]);
   return pancakes.subspan(0,len);
}

int count_flips(gsl::span<char> pancakes)
{
   int counter {};
   while (rng::any_of(pancakes, is_not_happy)) {
      counter += 1;
      gsl::span<char> equal_pancakes = first_homogeneous_subseq(pancakes);
      flip(equal_pancakes);
   }
   return counter;
}

int main()
{
   for (int test : gcj::test_cases(std::cin)) {
      std::vector<char> pancakes = read_stack(std::cin);
      std::cout << "Case #" << test << ": " <<  count_flips(gsl::as_span(pancakes)) << '\n';
   }
}
