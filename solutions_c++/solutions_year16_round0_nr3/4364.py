#include<iostream>
#include<string>
#include<sstream>
#include<fstream>
#include<vector>
#include<algorithm>
#include<assert.h>
#include<math.h>
#define JAMCOINS 1
#define LENGTH 0

struct OutputData{
  unsigned long long jamCoin;
  std::vector<unsigned long long> nonTrivials;
};

struct InputData {
  unsigned long long maxVal, jamCoinsFound=0;
  std::vector<int> inData;
  std::vector<bool> lowestVal;
  std::vector<bool> highestVal;
  std::vector<OutputData> jamCoinCollection;
  void collectJamCoins()
  {
    do{
      if(validJamCoin()) jamCoinsFound++;
      if(jamCoinsFound == inData[JAMCOINS]) break;
    }while(to_inc());
  }
  bool to_inc()
  {
    unsigned long long val = accumulate(lowestVal.begin(), lowestVal.end(), 0, [](unsigned long long x, unsigned long long y) { return (x << 1) + y; });
    if (maxVal > val) {
      lowestVal.clear();
      val++;
      while(val) {
        lowestVal.push_back(val & 1);
        val >>= 1;
      } 
      std::reverse(lowestVal.begin(), lowestVal.end());
      lowestVal[0] = 1;
      lowestVal[inData[LENGTH]-1] = 1;
      return true;
    }
    return false;
  }
  bool validJamCoin()
  {
    jamCoinCollection.push_back(OutputData());
    for(int i=2; i<=10; i++)
    {
      unsigned long long sum=0;
      for(int it=0; it<lowestVal.size(); it++)
        sum+=lowestVal[it]*pow(i,it);
      if(i == 10) jamCoinCollection.back().jamCoin = sum;
      jamCoinCollection.back().nonTrivials.push_back(find_non_trivial(sum));
      if(!jamCoinCollection.back().nonTrivials.back()){
        jamCoinCollection.pop_back();
        return false;
      }
    } 
    return true;
  }
  unsigned find_non_trivial(unsigned long long number)
  {
    for(unsigned long long i=2; i<=sqrt(number); i++)
      if(number%i==0) return i; 
    return 0;
  }
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
        inputVector.back().inData = str2vec(line);
        for(int i=0; i<inputVector.back().inData[LENGTH]; i++)
        {
          inputVector.back().highestVal.push_back(1);
          if(!i || i==inputVector.back().inData[LENGTH]-1)
            inputVector.back().lowestVal.push_back(1);
          else
            inputVector.back().lowestVal.push_back(0);
        }
        inputVector.back().maxVal = 
          accumulate(inputVector.back().highestVal.begin(), 
              inputVector.back().highestVal.end(), 0, [](unsigned long long x, unsigned long long y) { return (x << 1) + y; });
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
  InputSet *inputSet = new InputSet(argv[1], 3);
  for(unsigned i =0; i < inputSet->testCases; i++)
  {
    InputData *inputData = &inputSet->inputVector[i];
    inputData->collectJamCoins();
    std::cout << "Case #" << i+1 << ":"<< std::endl;
    for(auto& a: inputData->jamCoinCollection){
      std::cout << a.jamCoin << " ";
      for(auto& b: a.nonTrivials){
        std::cout << b << " ";
      }
      std::cout << std::endl;
    }
  }
  return 0;
}
