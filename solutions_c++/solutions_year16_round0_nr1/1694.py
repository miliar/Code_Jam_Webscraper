#include <iostream>
#include <fstream>
#include <string>

void GetTestCases(std::string in_line, int &num_test_case) {
  num_test_case = atoi(in_line.c_str());
}

void GetNumber(std::string in_line, int &n) {
  n = atoi(in_line.c_str());
}

void SolveA(int &n) {
  if (n == 0) {
	std::cout << "INSOMNIA" << std::endl;
	return;
  }
  // initialize digit_array
  bool digit_array[10];
  for (int i = 0; i < 10; i++) {
    digit_array[i] = false;
  }
  int last_num = n; 

  while (true) {
    // Update Digits
    int temp_num = last_num;
    while (temp_num) {
      digit_array[temp_num % 10] = true;
	  temp_num = temp_num / 10;
    }
	// Check All Digits called
    bool in_sleep_flag = true;
    for (int i = 0; i < 10; i++) {
	  if (digit_array[i] == false) {
	    in_sleep_flag = false;
		break;
	  }
	}    
	if (in_sleep_flag == true) {
	  std::cout << last_num << std::endl;
      return;
	}

	last_num += n;
  }    
}

int main() {
  std::ifstream in_file("A-large.in");
  std::string in_line;
  // Get Test Case T 
  std::getline(in_file, in_line);
  int num_test_case;
  GetTestCases(in_line, num_test_case);
  // std::cout << num_test_case << std::endl;
  // Get n
  int n;
  int cnt = 0;
  while (std::getline(in_file, in_line)) {
    GetNumber(in_line, n);
	printf("Case #%d: ", ++cnt);
	SolveA(n);
	// std::cout << n << std::endl;
  }
  return 0;
}