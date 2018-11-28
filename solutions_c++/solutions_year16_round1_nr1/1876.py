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

void GetSubstrings(std::vector<std::string> &overall ,const std::string &prefix, const int size, const std::string &postfix) {
  if (size == 0) return;
  std::string A("1001"); 
  std::string B("1111");   
  for (int i = 0; i <= size - 4; i++) {    
	overall.push_back(prefix + std::string(i, '0') + A + std::string(size - 4 - i, '0') + postfix);
    overall.push_back(prefix + std::string(i, '0') + B + std::string(size - 4 - i, '0') + postfix);
  }
  GetSubstrings(overall, prefix + A, size - 4, postfix);
  GetSubstrings(overall, prefix + B, size - 4, postfix);
  return;
}

void GCJC() {  
  // Base cases length 4
  /*
  const int base_len = 4;
  const int base_cases = 4;
  const int num_interprets = 9;
  int interprets[base_cases][num_interprets];
  int seq[base_cases][base_len];
  int is_valid[base_cases];
  for (int i = 0; i < base_cases; i++) {
    seq[i][0] = 1;
	seq[i][1] = i%2;
	seq[i][2] = i/2;
	seq[i][base_len - 1] = 1; 
    for (int j = 0; j < num_interprets; j++) {
	  interprets[i][j] = 0;
	  for (int k = 0; k < base_len; k++) {
	    interprets[i][j] = (j + 2) * interprets[i][j] + seq[i][base_len - 1 - k];
	  }
	  // std::cout << interprets[i][j] << " ";	  
	}
	// std::cout << std::endl;
  }
  int divisors[num_interprets];
  divisors[0] = 3; divisors[1] = 2; divisors[2] = 5;
  divisors[3] = 2; divisors[4] = 7; divisors[5] = 2;
  divisors[6] = 3; divisors[7] = 2; divisors[8] = 11;
  for (int i = 0; i < base_cases; i++) {
	for (int j = 0; j < num_interprets; j++) {
	  std::cout << interprets[i][j] % divisors[j] << " ";
	}
	std::cout << std::endl;
  }
  */  
  const int num_interprets = 9;
  int divisors[num_interprets];
  divisors[0] = 3; divisors[1] = 2; divisors[2] = 5;
  divisors[3] = 2; divisors[4] = 7; divisors[5] = 2;
  divisors[6] = 3; divisors[7] = 2; divisors[8] = 11;
  std::string seq[2];
  seq[0] = "1001"; 
  seq[1] = "1111";
  // Small
  /*
  std::ofstream out_file("C-small.out");  
  const int n = 16;
  std::string prefix;
  std::string postfix;
  std::vector <std::string> overall;
  for (int i = 0; i < 4; i++) {
    prefix = seq[i/2];
	postfix = seq[i%2];
    GetSubstrings(overall, prefix, n - 8, postfix);
  }
  out_file << "Case #1:" << std::endl;
  for (int i = 0; i < 50; i++) {
    out_file << overall[i] << " ";
	for (int j = 0; j < num_interprets; j++) {
	  out_file << divisors[j] << " ";
	}
	out_file << std::endl;
  }  
  */
  // Large
  std::ofstream out_file("C-large.out");
  const int n = 32;
  std::string prefix;
  std::string postfix;
  std::vector <std::string> overall;
  for (int i = 0; i < 4; i++) {
    prefix = seq[i/2];
	postfix = seq[i%2];
    GetSubstrings(overall, prefix, n - 8, postfix);
  }
  out_file << "Case #1:" << std::endl;
  for (int i = 0; i < 500; i++) {
    out_file << overall[i] << " ";
	for (int j = 0; j < num_interprets; j++) {
	  out_file << divisors[j] << " ";
	}
	out_file << std::endl;
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
  std::cout << k << " " << c << " " << s << std::endl;
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
  long long int offset = 0;
  int modified_c = c - 1;
  if (c > k) modified_c = k - 1;
  for (int i = 0; i < modified_c; i++) {
    offset = offset * k + fractiles.front();
	fractiles.pop();
  }
  for (int i = 0; i < s; i++) {
    if (fractiles.size() == 0) break;
    out_file << offset + fractiles.front() + 1 << " ";
	fractiles.pop();
  }
  out_file << std::endl;
  return;
}


void GCJD() {
  std::ifstream in_file("D-large-practice.in");
  std::ofstream out_file("D-large.out");
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

void GetString(const std::string &in_line, std::string &s) {
  s = in_line;
}


void Solve1A(std::string s, std::ostream &out_file) {  
  std::vector<unsigned char>last_word;
  for (int i = 0; i < s.size(); i++) {
	if (i == 0) {
	  last_word.push_back(s[i]);
	  continue;
	}
    if (s[i] >= last_word.front()) {
	  last_word.insert(last_word.begin(), s[i]);
	} else {
	  last_word.push_back(s[i]);
	}
  }  
  for (int i = 0; i < last_word.size(); i++) {
    out_file << last_word[i];
  }
  out_file << std::endl;
}


void GCJ1A() {
  std::ifstream in_file("A-large.in");
  std::ofstream out_file("A-large.out");
  std::string in_line;
  // Get Test Case T 
  std::getline(in_file, in_line);
  int num_test_case;
  GetTestCases(in_line, num_test_case);
  // std::cout << num_test_case << std::endl;
  // Get n
  std::string s;
  int cnt = 0;
  while (std::getline(in_file, in_line)) {
    GetString(in_line, s);
	out_file << "Case #" << ++cnt << ": ";	
	Solve1A(s, out_file);
  }
  in_file.close();
  out_file.close();
  return;  
}
  

int main() {  
  //GCJA();
  //GCJB();
  //GCJC();
  //GCJD(); 
  GCJ1A();
  return 0;
}