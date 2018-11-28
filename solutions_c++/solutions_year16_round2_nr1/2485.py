//
//  main.cpp
//  codejam2016_round1b
//
//  Created by Raphael Sampaio on 4/30/16.
//  Copyright © 2016 Raphael Sampaio. All rights reserved.
//

#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>

std::vector<int> number;
std::map<char, int> map;

bool has_char(char c) {
  if (map[c] > 0)
    return true;
  else
    return false;
}

bool has_word(char c, std::string word, int n) {
  if (has_char(c)) {
    for (auto &a : word) {
        map[a]--;
    }
    number.push_back(n);
    return true;
  }
  return false;
}

void func(std::string str) {
  
  number.clear();
  map.clear();
  
  for (auto &a : str) {
    map[a]++;
  }
  
  bool condition = true;
  while (condition) {
    condition =
    has_word('Z', "ZERO", 0) ||
    has_word('W', "TWO", 2) ||
    has_word('U', "FOUR", 4) ||
    has_word('X', "SIX", 6) ||
    has_word('G', "EIGHT", 8);
  }
  condition = true;
  while (condition) {
    condition =
    has_word('R', "THREE", 3) ||
    has_word('F', "FIVE", 5);
  }
  condition = true;
  while (condition) {
    condition = has_word('V', "SEVEN", 7);
  }
  condition = true;
  while (condition) {
    condition = has_word('I',"NINE", 9);
  }
  condition = true;
  while (condition) {
    condition = has_word('O', "ONE", 1);
  }
}

int main(int argc, const char * argv[]) {
  int max;
  std::string str;
  std::cin >> max;
  for(int i = 0; i < max; ++i)
  {
    std::cin >> str;
    printf("Case #%d: ", i + 1);
    func(str);
    std::sort(number.begin(), number.end());
    
    for (auto &a : number) {
    printf("%d", a);
    }
    printf("\n");
  }
  return 0;
}