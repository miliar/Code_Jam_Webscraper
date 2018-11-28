#include <fstream>
#include <iostream>
#include <vector>
#include<string>
#include <set>
#include <algorithm>
#include <sstream>

struct testcase{
  int n, l;
  int caseno;
  std::vector<std::string> data;
  std::vector<std::vector<long> > numbers;
  std::vector<std::string> weights;
  testcase() {   }
  void add_str(std::string& s){
    data.push_back(s);
    compute_number(s);
  }
  void compute_number(std::string&s) {
    std::vector<long> number;
    number.resize(100, 0);
    std::string w = "";
    int current_val = 0;
    int c = 0;
    char last = s[0];
    w.push_back(last);
    for (int i = 1; i < s.size(); i++) {
      if (s[i] == last) {
        number[current_val] ++;

      } else {
        current_val ++;
        w.push_back(s[i]);
      }
      last = s[i];
    }
    numbers.push_back(number);
    weights.push_back(w);
  }

  bool is_equal_num() {
    bool f = true;
    std::string t = weights[0];
    for (int i = 1; i < weights.size(); i++) {
      if (weights[i]!= t){
        f = false;
        return false;
      }
    }
    return true;
  }
  long long result() {
    long long val = 0;
    long long res = 0;
    for (int j = 0; j < 100; j++) {
      val = 0;
      for (int i = 0; i < n; i++){ 
        val += numbers[i][j];
      }
      long long v1 = val/n;
      long long v2 = v1 + 1;
      long long v3 = v1 - 1;
      if (v3 < 0)
        v3 = 0;
      long long s1 = 0, s2 = 0, s3 = 0;
      for (int i = 0; i < n; i++) {
        if (numbers[i][j] > v1) {
          s1 += numbers[i][j]-v1;
        } else {
          s1 += v1 - numbers[i][j];
        }
        if (numbers[i][j] > v2) {
          s2 += numbers[i][j] - v2;
        } else {
          s2 += v2 - numbers[i][j];
        }
        if (numbers[i][j] > v3) {
          s3 += numbers[i][j]-v3;
        } else {
          s3 += v3 - numbers[i][j];
        }
      }
    res += std::min(s1, std::min(s2,s3));
    
    }
    return res;
  }
  
};

int main(int argc, char** argv) {
  if (argc < 3) {
    std::cout << "Please, provide input file name as a first parameter, and output file name as a second parameter" << std::endl;
    return 0;
  }
  std::ifstream inputStream(argv[1]);
  if (inputStream.fail()) {
    std::cout << "Please, provide _valid_ file name as first parameter" << std::endl;
    return 0;
  }
  std::ofstream output_file(argv[2]);
  //
  int t;
  inputStream >> t;
  for (int i = 0; i < t; i++) {
    testcase tc;
    tc.caseno = i + 1;
    inputStream >>  tc.n;
    std::string line;
    for (int j = 0; j < tc.n; j ++) {
      inputStream >> line;
      tc.add_str(line);
      
    }
    if (!tc.is_equal_num()) {
      output_file << "Case #" << tc.caseno << ": Fegla Won"  << std::endl;
    }
    else {
      output_file << "Case #" << tc.caseno << ": "<<tc.result()  << std::endl;
    }
  }
 //do smth with input
  inputStream.close();
  
  
  // output smth
  //output_file << "Case #" << (i+1) << ": ";
  output_file.close();
  return 0;
}