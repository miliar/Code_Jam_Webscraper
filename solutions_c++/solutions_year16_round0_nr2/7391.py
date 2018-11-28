#include <iostream>
#include <fstream>
using namespace std;

int getNumOfManeuver(std::string line);
std::string swapState(int until, std::string line);

int main(int argc, char* argv[])
{
  if (argc != 2) { return 0;}
  ofstream outFile("B_output.txt");
  ifstream inFile(argv[1]);
  if (!inFile.is_open()) return 0;
  std::string line;
  
  int num_of_tc, check_tc = 0;
  while (getline(inFile, line)) {
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
      for (std::string::iterator it  = line.begin(); it != line.end(); ++it) {
        if (*it != '+' && *it != '-') { return -1;}
    }
      int result = getNumOfManeuver(line);
      outFile << "Case #" << num_of_tc - check_tc  << ": "<< result  << endl;
    }
  }
  inFile.close();
  outFile.close();
  return 0;
}

int getNumOfManeuver(std::string line) {
  std::string line2 = line;
  int num = 0;
  int i = 0;
  for (std::string::iterator it = line2.end() - 1; it >= line2.begin(); --it) {
    if (*it == '+') {
      continue;
    } else {
      line2 = swapState(i, line2);
      num++;
    }
    i++;
  }
  return num;
}

std::string swapState(int until, std::string line) {
 int i = 0;
 for (std::string::iterator it  = line.begin(); it != line.end() - until; ++it) {
   if (*it == '+') { line.replace(i, 1, "-"); }
   else { line.replace(i, 1, "+"); }
   i++;
 }
 return line;
}
