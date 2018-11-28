
#include <iostream>
#include <sstream>
#include <vector>

typedef  __float128 float_type;

class TestCase{
public:
  double firm_cost;
  double firm_gain;
  double goal;
};
#define debugPrint(var) std::cerr<<#var<<'='<<var<<std::endl;

double calcTime(const TestCase &test){
  float_type spent_time = 0.0;
  float_type cps = 2.0;
  float_type cookies = 0.0;

  debugPrint(test.firm_cost);
  debugPrint(test.firm_gain);
  debugPrint(test.goal);
  while(true){
    float_type next_buy = test.firm_cost / cps;
    float_type remain = test.goal / cps;
    float_type next_cps = cps + test.firm_gain;
    float_type next_remain = test.goal / next_cps;
    if(remain < next_buy + next_remain){
      spent_time += remain;
      break;
    }
    else{
      spent_time += next_buy;
      cps = next_cps;
    }
  }

  return spent_time;
}


int main(){
  int num_of_cases;
  {
    std::string line;
    if(!std::getline(std::cin, line)) return 1;
    num_of_cases = atoi(line.c_str());
  }

  std::vector<TestCase> tests;
  for(int i=0;i<num_of_cases;i++){
    std::string line;
    if(!std::getline(std::cin, line)) return 1;
    std::stringstream ss(line);
    std::cerr << line << std::endl;

    TestCase test;
    ss >> test.firm_cost >> test.firm_gain >> test.goal;
    tests.push_back(std::move(test));
  }

//  printf("Case #%d: %lf\n", 0, calcTime(tests[0]));
//  printf("Case #%d: %lf\n", 1, calcTime(tests[1]));
  for(int i=0;i<num_of_cases;i++){
    printf("Case #%d: %.7lf\n", i+1, calcTime(tests[i]));
  }
}
