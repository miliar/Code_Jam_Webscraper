#include <iostream>
#include <fstream>
#include <string>
#include <queue>

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

void GetParams(const std::string &in_line, int &k, int &c, int &s) {
  char *context = NULL;
  char *temp_in_line = new char [in_line.length() + 1];
  std::strcpy(temp_in_line, in_line.c_str());
  char *token = strtok_s(temp_in_line, " ", &context);  
  k = atoi(token);
  token = strtok_s(NULL, " ", &context);
  c = atoi(token);
  token = strtok_s(NULL, " ", &context);
  s = atoi(token);
}

void SolveD(const int &k, const int &c, const int &s, std::ostream &out_file) {
  // Check Impossible
  if (s < k - (c - 1)) {
    out_file << "IMPOSSIBLE" << std::endl;
	return;
  }
  // For small dataset
  if (s >= k) {
	for (int i = 0; i < s; i++) {
	  out_file << i + 1;
	  if (i != s -1) out_file << " ";
	}
	out_file << std::endl;
	return;
  }  
  // For large dataset
  std::queue<int> fractiles;
  for (int i = 0; i < k; i++) {
	fractiles.push(i);
  }  
  int offset = 0;
  int modified_c = c - 1;
  if (c > k) modified_c = k - 1;
  for (int i = 0; i < modified_c; i++) {
    offset = offset * k + fractiles.front();
	fractiles.pop();
  }
  for (int i = 0; i < s; i++) {
    out_file << offset + fractiles.front() + 1 << " ";
	fractiles.pop();
  }
  out_file << std::endl;
  return;
}

void GCJD() {
  std::ifstream in_file("D-small-attempt1.in");
  std::ofstream out_file("D-small.out");
  std::string in_line;
  // Get Test Case T 
  std::getline(in_file, in_line);
  int num_test_case;
  GetTestCases(in_line, num_test_case);
  // std::cout << num_test_case << std::endl;
  // Get n
  int k, c, s;
  int cnt = 0;
  while (std::getline(in_file, in_line)) {
    GetParams(in_line, k, c, s);
	out_file << "Case #" << ++cnt << ": ";
	SolveD(k, c, s, out_file);
  }
  in_file.close();
  out_file.close();
  return;  
}

int main() {  
  //GCJA();
  //GCJB();
  GCJD(); 
  return 0;
}