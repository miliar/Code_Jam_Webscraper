#include <string>
#include <iostream>
#include <vector>

struct LastWordFinder
{
  static std::string findWinningWord(const std::string& input);
};

std::string LastWordFinder::findWinningWord(const std::string& input)
{
  std::string output = "";
  char pivot = input[0];
  output += pivot;
  for (int i = 1; i < input.size(); i++) {
    if (input[i] >= output[0]) output = input[i] + output;
    else output += input[i];
  }
  return output;
}

int main()
{
  int size = 0;
  std::cin >> size;
  std::vector<std::string> outputs;
  for (int i = 0; i < size; i++) {
    std::string input;
    std::cin >> input;
    //std::cout << input << std::endl;                                                                                                                                    
    outputs.push_back(LastWordFinder::findWinningWord(input));
  }
  for (int i = 0; i < size; i++) {
    std::cout << "Case " << i+1 << ": " << outputs[i] << std::endl;
  }
}
