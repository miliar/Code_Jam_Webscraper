#include <fstream>
#include <iostream>

#define GIVEN_MAX 1000000

size_t Solve(size_t input) {
  
  bool nums[10] = {};
  char bcount = 0;
  size_t current_val = 0;
  
  if(input == 0) {
    return -1;
  }
  
  while(bcount < 10) {
    
    current_val += input;
    unsigned partial_num = current_val;
    
    while(partial_num > 0) {
      
      unsigned mod = partial_num % 10;
      
      if(!nums[mod]) {
        nums[mod] = true;
        ++bcount;
      }
      
      partial_num /= 10;
    }
  }
  
  return current_val;
}

int main(int argc, char** argv) {
  
  if(argc < 3) {
    std::cout << "insufficient args!" << std::endl;
    return -1;
  }
  
  size_t case_num = 1;
  std::ifstream infile(argv[1]);
  std::ofstream outfile(argv[2]);
  
  if(!infile.is_open() || !outfile.is_open()) {
    std::cout << "unable to open file\n" << std::endl;
    return -1;
  }
  
  size_t num_cases;
  infile >> num_cases;
  
  while (case_num <= num_cases) {
    
    size_t current_input;
    infile >> current_input;
    
    size_t result = Solve(current_input);
    
    outfile << "Case #" << case_num++ << ": ";
    if(result != -1) {
      outfile << result << "\n";
    }
    else {
      outfile << "INSOMNIA\n";
    }
    
  }
  
}