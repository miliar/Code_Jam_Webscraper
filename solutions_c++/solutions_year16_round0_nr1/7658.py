#include <iostream>
#include <string>

const int LIMIT = 200;

using namespace std;

bool markOffNumbers(int num, bool* numbersSeen){
  string s = to_string(num);
  for (char c : s){
    numbersSeen[c - '0'] = true;
  }

  for (int i = 0; i < 10; i++){
    if (!numbersSeen[i]){
      return false;
    }
  }
  return true;
}

int main(int argc, char** argv){

  int numTestCases = -1;
  long testCase = -1;

  bool numbersSeen[10];

  cin >> numTestCases;
  for (int t = 1; t <= numTestCases; t++){

    cout << "Case #" << t << ": ";

    cin >> testCase;

    if (testCase == 0){
      cout << "INSOMNIA" << endl;
    } else {

      for (int i = 0; i < 10; i++){
        numbersSeen[i] = false;
      }

      long currNumber = testCase;

      while (!markOffNumbers(currNumber, numbersSeen)){
        currNumber += testCase;
      }

      cout << currNumber << endl;

    }

  }
  return 0;
}
