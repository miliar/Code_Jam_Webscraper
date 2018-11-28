#include<iostream>
#include<string>
#include<sstream>
#include<fstream>
#include<vector>
#include<algorithm>
#include<assert.h>

struct InputData {
  std::vector<bool> pancakes;
  unsigned switchesCnt = 0;
};

class InputSet {
  int linesPerCase;
  std::ifstream in_file;
  int str2int(std::string s) {
    int value;
    std::istringstream(s) >> value;
    return value;
  }
  std::vector<bool>str2vec(std::string s) {
    std::vector<bool> intVec;
    for(char& c : s)
      intVec.push_back(c == '+' ? true : false);
    return intVec;
  }
  void readFile() {
    int count=0;
    for(std::string line; getline(in_file, line); ++count)
    {
      if(!count) {
        testCases = str2int(line);
        inputVector.push_back(InputData());
      } else {
        if(line.empty())
          continue;
        inputVector.back().pancakes = str2vec(line);
        std::reverse(inputVector.back().pancakes.begin(), inputVector.back().pancakes.end());
        inputVector.push_back(InputData());
      }
    }
  }
  public:
  int testCases;
  std::vector<InputData>inputVector;
  InputSet(std::string input_filename, int linesPerCase_): linesPerCase(linesPerCase_){ 
    in_file.open(input_filename.c_str(), std::ifstream::in); 
    readFile();
  }
  ~InputSet(){ in_file.close(); }
};


int main(int argc, char *argv[]) {
  InputSet *inputSet = new InputSet(argv[1], 1);
  for(unsigned i =0; i < inputSet->testCases; i++)
  {
    InputData *inputData = &inputSet->inputVector[i];
    while(std::find(inputData->pancakes.begin(), inputData->pancakes.end(), 0) != inputData->pancakes.end())
    {
      bool flag=true;
      for(int it=0; it<inputData->pancakes.size(); it++)
      {
        flag = flag && inputData->pancakes[it];
          if(!flag)
            inputData->pancakes[it] = inputData->pancakes[it] ^ 1;
      }
      if(!flag) inputData->switchesCnt++; 
    }
    std::cout << "Case #" << i+1 << ": " << inputData->switchesCnt << std::endl;
  }
  return 0;
}
