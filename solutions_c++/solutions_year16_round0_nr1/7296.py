#include <iostream>
#include <fstream>
using namespace std;

bool canSleep(int n);
int findSleepNumber(int n);

int main(int argc, char* argv[])
{
  if (argc != 2) { return 0;}
  ofstream outFile("output.txt");
  ifstream inFile(argv[1]);
  if (!inFile.is_open()) return 0;
  std::string line;
  
  int num_of_tc, check_tc = 0;
  while (getline(inFile, line)) {
    int input;
    if (check_tc == 0) {
      num_of_tc = std::stoi(line);
      if (num_of_tc > 100 || num_of_tc < 1) {
        continue;
      } else {
        check_tc = num_of_tc;
        continue;
      }
    }
    check_tc = check_tc - 1;
    if (check_tc >= 0) {
      input = std::stoi(line);
      int result = findSleepNumber(input);
      if (result == 0) {
        outFile << "Case #" << num_of_tc - check_tc  << ": INSOMNIA" << endl;
      } else {
        outFile << "Case #" << num_of_tc - check_tc << ": "<< result << endl;
      }
    }
  }
  inFile.close();
  outFile.close();
  return 0;
}

int findSleepNumber(int in) {
  if (in == 0) {
    return 0;
  }
  int checkArr[10] = {};
  int i = 1;
  while (true) {
    int sleepNum = in * (i++);
    std::string s = std::to_string(sleepNum);
    for (std::string::iterator it  = s.begin(); it != s.end(); ++it) {
      checkArr[*it - '0'] = 1;
    }

    int checkNum = 0;
    for (int j = 0; j < 10; j++) {
      if (checkArr[j] == 1) checkNum += 1;
      if (checkNum == 10) return sleepNum;
    }
  }
}
