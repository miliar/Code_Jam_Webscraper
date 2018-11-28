#include<iostream>
#include<string>
#include<sstream>
#include<fstream>
#include<vector>
#include<algorithm>
#include<assert.h>
#include<bitset>

struct InputData {
  unsigned long long in_num;
  std::bitset<10> seen;
  unsigned long long last_num;
};

class InputSet {
  int linesPerCase;
  std::ifstream in_file;
  int str2int(std::string s) {
    int value;
    std::istringstream(s) >> value;
    return value;
  }
  std::vector<int>str2vec(std::string s) {
    std::vector<int> intVec;
    std::string token, delimiter = " ";
    size_t pos=0;
    while((pos = s.find(delimiter)) != std::string::npos) {
      token = s.substr(0,pos);
      intVec.push_back(str2int(token));
      s.erase(0, pos + delimiter.length());
    }
    intVec.push_back(str2int(s));
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
        inputVector.back().in_num = str2int(line);
        inputVector.back().last_num = inputVector.back().in_num;
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
    for(int j=1; !inputData->seen.all(); j++)
    {
      inputData->last_num = inputData->in_num * j;
      if(j!=1 && inputData->last_num == inputData->in_num)
      {
        std::cout << "Case #" << i+1 << ": INSOMNIA" << std::endl;
        break;
      }
      unsigned long long div = inputData->last_num;
      while(div != 0)
      {
        unsigned int rem = div % 10;
        inputData->seen.set(rem);
        div/=10;
      }
    }
    if(inputData->seen.all())
      std::cout << "Case #" << i+1 << ": " << inputData->last_num << std::endl;
  }
  return 0;
}
