#include <fstream>
#include <iostream>
#include <algorithm>
#include <utility>

char buffer[101];

void flip(char* first, char* last) {
  
  while(first < last) {
    *first = (*first == '+') ? '-' : '+';
    *last = (*last == '+') ? '-' : '+';
    
    std::swap(*first++, *last--);
  }
  
  if(first == last) {
    *first = (*first == '+') ? '-' : '+';
  }
}

size_t Solve(size_t num) {
  
  char* last_diff = buffer;
  size_t count = 0;
  
  while(last_diff != (buffer + num)) {
    
    last_diff = std::find_if(buffer, buffer + num, 
                             [=](char c){ return c != buffer[0]; });
    
    if(last_diff != (buffer + num)) {
      flip(buffer, last_diff - 1);
      ++count;
    }
  }
  
  return count + (buffer[0] == '-' ? 1 : 0);
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
  infile.ignore(1,'\n');
  
  while (case_num <= num_cases) {
    
    size_t num_bytes = 0;
    infile.getline(buffer, sizeof(buffer) / sizeof(char));
    num_bytes = infile.gcount() - 1;
    
    size_t result = Solve(num_bytes);
    
    outfile << "Case #" << case_num++ << ": ";
    outfile << result << "\n";
    
  }
  
}