#include <iostream>
#include <map>
#include <vector>
#include <deque>
#include <string>
#include <cstdio>
#include <cstdlib>

bool all_happy(const std::string& stack) {
  std::size_t found = stack.find("-");
  return found == std::string::npos;
}


int entropia(const std::string& stack) {
  std::size_t sz = stack.size();
  int e = 0;
  for (int i = 1; i < sz; ++i) {
    if (stack[i-1] != stack[i]) e++;
  }
  return e;
}

std::string flip(std::string stack, int pos) {
  //std::cout << "flip: " << stack << " at " << pos << std::endl;
  for(int i = 0; i < pos; ++i, --pos) {
    char aux = stack[pos - 1];
    stack[pos - 1] = stack[i]  == '+' ? '-' : '+';
    stack[i] = aux == '+' ? '-' : '+';
  }
  //std::cout << " = " << stack << std::endl;
  return stack;
}

int minflips(std::string& stack, int flips) {
  //std::cout << "minflips: " << stack << " " << flips << std::endl;
  if (all_happy(stack)) return flips;
  //int v;
  //std::cin >>v;
  
  std::string min_stack = stack;
  int min_ent = entropia(min_stack);
  std::size_t sz = stack.size();
  for(int i = 1; i <= sz; ++i) { 
    std::string new_stack = flip(stack, i); 
    int ent = entropia(new_stack);
    if (ent <= min_ent) {
      min_stack = new_stack;
      min_ent = ent;
    } 
  }
  return minflips(min_stack, flips+1);
}

int solve() {
  std::string stack;
  std::cin >> stack;
  return minflips(stack, 0);
}

int main(int argc, char* argv[]) {
  int T;
  std::cin >> T;
  for(int t = 1; t <= T; ++t) {
    
    int response = solve();
    std::cout << "Case #" << t << ": " << response << std::endl;
  }
  return 0;
}
