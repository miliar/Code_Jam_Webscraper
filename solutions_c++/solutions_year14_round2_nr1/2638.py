#include <iostream>
#include <fstream>
#include <vector>
#include <array>
#include <iomanip>
#include <algorithm>
#include <string>
#include <cmath>

int main(int argc, char *argv[]) {
  // std::ifstream in("test_input");
  std::ifstream in("A-small-attempt0.in");
  if (!in.is_open())
    std::cout << "error opening file in" << std::endl;
  // std::ofstream out("test_output");
  std::ofstream out("output");
  if (!out.is_open())
    std::cout << "error opening file out" << std::endl;

  unsigned test_count = 0;
  in >> test_count;
  for(unsigned test_index = 1; test_index <= test_count; ++test_index) {
    unsigned N = 0;
    in >> N;
    std::vector<std::string> strings(N);
    std::vector<unsigned> pointers(N, 0);
    unsigned opt_operations_count = 0;
    
    for (unsigned i = 0; i < N; ++i) {
      in >> strings[i];
    }

    for (auto && str : strings)
      std::cout << str << std::endl;

    std::cout << "p" << pointers[0] << std::endl;

    bool end = false;
    while (!end) {
      std::vector<unsigned> block_size(N, 0);
      char block_sym = strings[0][pointers[0]];
      std::cout << "p" << pointers[0] << std::endl;
      bool different = false;
      unsigned sum_bs = 0;

      std::cout << block_sym << " " << N << std::endl;

      for (unsigned i = 0; i < N; ++i) {
	// std::cout << "in" << std::endl;

	if (block_sym != strings[i][pointers[i]]) {
	  // std::cout << block_sym << " " << strings[i][pointers[i]] << std::endl;
	  different = true;
	  break;
	}
	while (strings[i][pointers[i]] == block_sym && 
	       pointers[i] != strings[i].size()) {
	  // std::cout << "in1" << std::endl;
	  ++block_size[i];
	  ++sum_bs;
	  ++pointers[i];
	}
	if (pointers[i] == strings[i].size()) {
	  // std::cout << "end" << std::endl;
	  end = true;
	}
      }
      
      // std::cout << "in3" << std::endl;

      if (!different) {
	sum_bs /= N;
	std::cout << "sum_bs" << sum_bs << std::endl;
	for (unsigned i = 0; i < N; ++i) {
	  std::cout << abs(sum_bs - block_size[i]) << std::endl;

	  opt_operations_count += abs(sum_bs - block_size[i]);
	}
      } else {
	break;
      }
    }

    bool on_end = true;
    for (unsigned i = 0; i < N; ++i) {
      if (pointers[i] != strings[i].size()) {
	// std::cout << "###" << (pointers[i]) << " " << &strings[i][strings[i].size()-1] << std::endl;
	on_end = false;
	break;
      }
    }

    if (on_end) {
      out << "Case #" << test_index << ": " << opt_operations_count << std::endl;
    } else {
      std::cout << "on_end_fail" << std::endl;

      out << "Case #" << test_index << ": Fegla Won" << std::endl;
    }
  }
  return 0;
}
