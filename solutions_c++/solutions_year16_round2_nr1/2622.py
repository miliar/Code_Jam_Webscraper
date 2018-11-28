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

void GetCakes(std::string in_line, int &num_cakes, bool *cakes) {
  num_cakes = in_line.size();
  for (int i = 0; i < num_cakes; i++) {
    cakes[i] = (in_line[i] == '-'?0:1);
  }  
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

void GetParams(const std::string &in_line, std::vector<int> &params, const char *delim) {
  char *ptr = strdup(in_line.c_str());
  char *token = strtok_s(ptr, delim, &ptr);
  while (token) {
	params.push_back(atoi(token));
	token = strtok_s(NULL, delim, &ptr);
  }
}

void GetString(const std::string &in_line, std::string &s) {
  s = in_line;
}

void GetArrayParams(const std::string &in_line, const int num_elements, int *param) {
  char *context = NULL;
  char *temp_in_line = new char [in_line.length() + 1];
  std::strcpy(temp_in_line, in_line.c_str());
  char *token = strtok_s(temp_in_line, " ", &context);
  param[0] = atoi(token);
  for (int i = 1; i < num_elements; i++) {
    token = strtok_s(NULL, " ", &context);
	param[i] = atoi(token);
  }  
}

void GetAlphabetFrequency(std::string &seq, int *alphabet_freq) {
  const int n_alphabets = 26;
  for (int i = 0; i < n_alphabets; i++) {
    alphabet_freq[i] = 0;
  }
  for (int i = 0; i < seq.size(); i++) {
    alphabet_freq[(int)seq[i] - (int)'A']++;
  }
}

void SolveA(int *alphabet_freq, std::ostream &out_file) {
  std::vector<int> digits(10);
  for (int i = 0; i < 10; i++) {
    digits[i] = 0;
  }
  // 0
  if (alphabet_freq[(int)'Z'-(int)'A'] != 0) {
	int tmp = alphabet_freq[(int)'Z'-(int)'A'];
    digits[0] += tmp;	
	alphabet_freq[(int)'Z'-(int)'A'] -= tmp;
	alphabet_freq[(int)'E'-(int)'A'] -= tmp;
	alphabet_freq[(int)'R'-(int)'A'] -= tmp;
	alphabet_freq[(int)'O'-(int)'A'] -= tmp;
  }
  // 2
  if (alphabet_freq[(int)'W'-(int)'A'] != 0) {
	int tmp = alphabet_freq[(int)'W'-(int)'A'];
    digits[2] += tmp;	
	alphabet_freq[(int)'T'-(int)'A'] -= tmp;
	alphabet_freq[(int)'W'-(int)'A'] -= tmp;
	alphabet_freq[(int)'O'-(int)'A'] -= tmp;	
  }
  // 6
  if (alphabet_freq[(int)'X'-(int)'A'] != 0) {
	int tmp = alphabet_freq[(int)'X'-(int)'A'];
    digits[6] += tmp;	
	alphabet_freq[(int)'S'-(int)'A'] -= tmp;
	alphabet_freq[(int)'I'-(int)'A'] -= tmp;
	alphabet_freq[(int)'X'-(int)'A'] -= tmp;	
  }
  // 8
  if (alphabet_freq[(int)'G'-(int)'A'] != 0) {
	int tmp = alphabet_freq[(int)'G'-(int)'A'];
    digits[8] += tmp;	
	alphabet_freq[(int)'E'-(int)'A'] -= tmp;
	alphabet_freq[(int)'I'-(int)'A'] -= tmp;
	alphabet_freq[(int)'G'-(int)'A'] -= tmp;	
	alphabet_freq[(int)'H'-(int)'A'] -= tmp;	
	alphabet_freq[(int)'T'-(int)'A'] -= tmp;
  }
  // 7
  if (alphabet_freq[(int)'S'-(int)'A'] != 0) {
	int tmp = alphabet_freq[(int)'S'-(int)'A'];
    digits[7] += tmp;	
	alphabet_freq[(int)'S'-(int)'A'] -= tmp;
	alphabet_freq[(int)'E'-(int)'A'] -= tmp;
	alphabet_freq[(int)'V'-(int)'A'] -= tmp;	
	alphabet_freq[(int)'E'-(int)'A'] -= tmp;	
	alphabet_freq[(int)'N'-(int)'A'] -= tmp;
  }
  // 5
  if (alphabet_freq[(int)'V'-(int)'A'] != 0) {
	int tmp = alphabet_freq[(int)'V'-(int)'A'];
    digits[5] += tmp;	
	alphabet_freq[(int)'F'-(int)'A'] -= tmp;
	alphabet_freq[(int)'I'-(int)'A'] -= tmp;
	alphabet_freq[(int)'V'-(int)'A'] -= tmp;	
	alphabet_freq[(int)'E'-(int)'A'] -= tmp;		
  }
  // 4
  if (alphabet_freq[(int)'F'-(int)'A'] != 0) {
	int tmp = alphabet_freq[(int)'F'-(int)'A'];
    digits[4] += tmp;	
	alphabet_freq[(int)'F'-(int)'A'] -= tmp;
	alphabet_freq[(int)'O'-(int)'A'] -= tmp;
	alphabet_freq[(int)'U'-(int)'A'] -= tmp;	
	alphabet_freq[(int)'R'-(int)'A'] -= tmp;		
  }
  // 3
  if (alphabet_freq[(int)'R'-(int)'A'] != 0) {
	int tmp = alphabet_freq[(int)'R'-(int)'A'];
    digits[3] += tmp;	
	alphabet_freq[(int)'T'-(int)'A'] -= tmp;
	alphabet_freq[(int)'H'-(int)'A'] -= tmp;
	alphabet_freq[(int)'R'-(int)'A'] -= tmp;	
	alphabet_freq[(int)'E'-(int)'A'] -= tmp;		
	alphabet_freq[(int)'E'-(int)'A'] -= tmp;		
  }
  // 1
  if (alphabet_freq[(int)'O'-(int)'A'] != 0) {
	int tmp = alphabet_freq[(int)'O'-(int)'A'];
    digits[1] += tmp;	
	alphabet_freq[(int)'O'-(int)'A'] -= tmp;
	alphabet_freq[(int)'N'-(int)'A'] -= tmp;
	alphabet_freq[(int)'E'-(int)'A'] -= tmp;		
  }
  // 9
  if (alphabet_freq[(int)'I'-(int)'A'] != 0) {
	int tmp = alphabet_freq[(int)'I'-(int)'A'];
    digits[9] += tmp;	
	alphabet_freq[(int)'N'-(int)'A'] -= tmp;
	alphabet_freq[(int)'I'-(int)'A'] -= tmp;
	alphabet_freq[(int)'N'-(int)'A'] -= tmp;		
	alphabet_freq[(int)'E'-(int)'A'] -= tmp;		
  }
  for (int i = 0; i < 10; i++) {
	if (digits[i] > 0) {
	  for (int j = 0; j < digits[i]; j++) {
		out_file << i;
	  }
	}
  }
  out_file << std::endl;
}

void GCJA() {
  std::ifstream in_file("A-large.in");  
  std::ofstream out_file("A-large.out");
  std::string in_line;  
  std::getline(in_file, in_line);
  std::vector<int> params;  
  GetParams(in_line, params, " ");
  const int n_test = params[0];
  for (int i = 0; i < n_test; i++) {
	const int n_alphabets = 26;
    int alphabet_freq[n_alphabets];
	std::getline(in_file, in_line);
	GetAlphabetFrequency(in_line, alphabet_freq);	
	out_file << "Case #" << i + 1 << ": ";
	SolveA(alphabet_freq, out_file);
  }  
}

int main() {
  GCJA();
  return 0;
}