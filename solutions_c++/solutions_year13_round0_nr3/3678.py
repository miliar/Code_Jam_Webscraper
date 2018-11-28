// -*- compile-command:"cd c:/MinGW/bin && g++.exe -std=c++11 c:/Users/Josef/Desktop/gcj/lawn.cc -o c:/Users/Josef/Desktop/gcj/farrisquarry && c:/Users/Josef/Desktop/gcj/farrisquarry < c:/Users/Josef/Downloads/C-attemp0.in" -*-
#include <iostream>
#include <algorithm>
#include <array>
#include <cmath>
#include <string>
#include <sstream>

typedef long long int lint;

std::ostringstream ss;
lint ispalin(lint x)
{
  ss << x; std::string s = ss.str(); ss.str("");
  std::string t = s;
  std::reverse(s.begin(), s.end());
  return s == t;
}

int main() {
  int cases; std::cin >> cases;
  for (int case_=1; case_<=cases; ++case_) {
    lint a, b; std::cin >> a >> b;
    lint i   = std::max((lint)(-5.0 + std::sqrt(a)), 0ll);
    lint end = std::max((lint)(+5.0 + std::sqrt(b)), 0ll); 

    while (end*end > b) --end;
    while (i*i < a) ++i;

    lint count = 0;
    for (; i<=end; ++i) {
      if (ispalin(i) && ispalin(i*i))
	++count;
    }

    std::cout << "Case #" << case_ << ": "<<count<<"\n";
  }
}
