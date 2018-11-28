#include <iostream>
#include <string>
#include <algorithm>
#include <cassert>

std::string lastWord(const std::string& word)
{
  if (word.empty()) {
    return word;
  }

  const std::string last = lastWord(word.substr(0, word.size() - 1));
  const std::string letter = std::string(1, word.back());
  return std::max(last + letter, letter + last);
}

int main()
{
  int cases = 0;
  std::cin >> cases;

  for (int i = 1; i <= cases; ++i) {
    std::string word;
    std::cin >> word;
    
    std::cout << "Case #" << i << ": " << lastWord(word) << std::endl;
  }
  
  return 0;
}
