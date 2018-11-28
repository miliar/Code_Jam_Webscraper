#include <iostream>
#include <string>
#include <fstream>

std::string flipit(char *n);

int main(int argc, const char *argv[])
{
  std::ifstream infile(argv[1]);
  int num;
  char stack[100];

  infile >> num;
  for (int i = 0; i < num; i++){
    infile >> stack;
    std::cout << "Case #" + std::to_string(i + 1) + ": " + flipit(stack) << std::endl;
  }

  return 0;
}

std::string flipit(char* pancakes) {
  char *curr = pancakes;
  char *next = pancakes++;
  int flips = 0;
  while(*next != '\0'){
    if(*next != *curr){
      flips++;
    }
    curr = next;
    next++;
  }
  if (*curr == '-'){
    flips++;
  }
  return std::to_string(flips);
}
