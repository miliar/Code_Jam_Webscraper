#include <iostream>
#include <string>

int FlipNum(std::string str){
  int result = 0;
  char state = '?';
  
  for(const char& letter: str){
    if (state != letter){
      state = letter;
      result++;
    }
  }

  if(state == '+')
    result--;
  
  return result;
}

int main(){
  std::string input_string;

  int num_tests;
  std::cin >> num_tests;
  
  for (int case_num = 1; case_num <= num_tests; case_num++){
    std::cin >> input_string;
    std::cout << "Case #" << case_num << ": " << FlipNum(input_string) << std::endl;
  }
  return 0;
}
