//
//  main.cpp
//  CodeJam2015_Ovation
//
//  Created by Neurosion on 4/11/15.
//  Copyright (c) 2015 Neurosion Development. All rights reserved.
//

#include <iostream>
#include <fstream>

namespace
{
  void CONSUME_LINE(std::ifstream& f)
  {
    static char buffer[1024];
    f.getline(buffer, 1024);
  }
}
#define TESTING 0

int main(int argc, const char * argv[])
{

  std::ifstream input("/Users/neurosion/Documents/Projects/CodeJam2015_Ovation/CodeJam2015_Ovation/A-large.in.txt");
  #if TESTING
    std::ostream& output = std::cout;
  #else
    std::ofstream file_output("/Users/neurosion/Documents/Projects/CodeJam2015_Ovation/CodeJam2015_Ovation/output_large.dat");
    std::ostream& output = file_output;
  #endif
      
  int test_cases;
  input >> test_cases;
  CONSUME_LINE(input);
      
  for (int i = 1; i <= test_cases; ++i) {
    int shy_max;
    input >> shy_max;
    int standing = 0, added = 0;
    for (int shyness = 0; standing <= shy_max; ++shyness) {
      char this_count_char;
      input >> this_count_char;
      int this_count = this_count_char - '0';
      if (this_count > 0) {
        if (standing < shyness) {
          int needed = shyness - standing;
          added += needed;
          standing += needed;
        }
      }
      standing += this_count;
    }
    output << "Case #" << i << ": " << added << std::endl;
    CONSUME_LINE(input);
  }
  
    return 0;
}

