#include<iostream>
#include<string>

int main(int argc, char** argv){
  std::string input;
  std::getline(std::cin, input);
  int num_input = std::atoi(input.c_str());

  for (int i = 0; i != num_input; ++i){
    std::getline(std::cin, input, ' ');
    int smax = std::atoi(input.c_str());
    std::getline(std::cin, input);
    const char* people = input.c_str();
    int num_standing = 0;
    int num_needed = 0;
    for (int j = 0; j != smax+1; ++j){
      while (num_standing < j){
        ++num_needed;
        ++num_standing;
      }
      num_standing += people[j] - '0';
    }
    std::cout << "Case #" << i+1 << ": " << num_needed << "\n";
  }



}