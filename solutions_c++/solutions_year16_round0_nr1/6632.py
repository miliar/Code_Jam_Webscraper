// Counting Sheep

#include <iostream>
#include <vector>

using std::vector;
using std::cin;
using std::cout;
using std::endl;

vector<int> getTests(){
  vector<int> v;
  int t, n;
  cin >> t; // number of tests
  for(int i = 0; i < t; i++){
    cin >> n;
    v.push_back(n);
  }
  return v;
}

bool testNums(bool nums[]){
  for(int i = 0; i < 10; i++){
    if(nums[i] == false){
      return false;
    }
  }
  return true;
}

vector<int> getDigits(int num){
  vector<int> digits;
  while(num != 0){
    digits.push_back(num % 10);
    num = num / 10;
  }
  return digits;
}

int getLastNumber(int number){
  if(number == 0){
    return 0;
  }

  bool nums[10] = {false,false,false,false,false,false,false,false,false,false};

  int n,counter = 1;
  vector<int> digits;
  while(!testNums(nums)){
    n = number*counter;
    digits = getDigits(n);
    for(int x : digits){
      nums[x] = true;
    }
    counter++;
  }
  return n;
}

void runTest(vector<int> tests){
  int ans;
  int size = tests.size();
  for(int i = 0; i < size; i++){
    ans = getLastNumber(tests[i]);
    if(ans == 0){
      cout<<"Case #" << i+1 << ": "<<"INSOMNIA"<<std::endl;
    }
    else{
      cout<<"Case #" << i+1 << ": "<<ans<<std::endl;
    }
  }
}

int main(int argc, char** argv){

  vector<int> tests = getTests();

  runTest(tests);

  return 0;
}
