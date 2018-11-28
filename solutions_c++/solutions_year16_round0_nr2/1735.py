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

void GCJA() {
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
  return;
}

void GetCakes(std::string in_line, int &num_cakes, bool *cakes) {
  num_cakes = in_line.size();
  for (int i = 0; i < num_cakes; i++) {
    cakes[i] = (in_line[i] == '-'?0:1);
  }  
}

void SolveB(const int &num_cakes, bool *cakes) {
  // Initialize temp cakes
  bool temp_cakes[100];
  for (int i = 0; i < num_cakes; i++) temp_cakes[i] = cakes[i];
  int num_flips = 0;
  while (true) {
    // Check all happy
    bool is_all_happy = true;
	int flip_pos = 0;
	for (int i = 0; i < num_cakes; i++) {
	  if (temp_cakes[num_cakes - 1 - i] == false) {
	    is_all_happy = false;
		flip_pos = num_cakes - 1 - i;
		break;
	  }
	}
	/*
    for (int i = 0; i < num_cakes; i++) {
	  std::cout << temp_cakes[i] << ", ";
	}
	std::cout << std::endl;
	*/
	if (is_all_happy == true) {
	  std::cout << num_flips << std::endl;
	  return;
	}

	for (int i = 0; i <= flip_pos; i++) {
      temp_cakes[i] = !temp_cakes[i];	  
	}
	num_flips++;
  }
}

void GCJB() {
  std::ifstream in_file("B-large.in");
  std::string in_line;
  // Get Test Case T 
  std::getline(in_file, in_line);
  int num_test_case;
  GetTestCases(in_line, num_test_case);
  // std::cout << num_test_case << std::endl;
  // Get n
  int num_cakes;
  bool cakes[100];
  int cnt = 0;
  while (std::getline(in_file, in_line)) {
    GetCakes(in_line, num_cakes, cakes);
	printf("Case #%d: ", ++cnt);
	SolveB(num_cakes, cakes);
  }
  return;
}


int main() {  
  //GCJA();
  GCJB();
  return 0;
}