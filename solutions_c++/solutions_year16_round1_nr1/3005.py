#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <algorithm>
#include <iterator>
#include <vector>
#include <cstdlib>

using namespace std;

int main() {
   string line;
   ifstream iFile("input.txt");
   if (!iFile.is_open()) {
      cout << "Input file not found." << endl;
      return 1;
   }
   getline(iFile, line);
   int numCases = strtol(line.c_str(),0,10);
   for (int i = 0; i < numCases; i++) {
      getline(iFile, line);
      string answer;
      for (int j = 0; j < line.length()-1; j++) {
         if (j == 0) {
            answer += line[j];
         } else if (line[j] < answer[0]) {
            //add to end
            answer += line[j];
         } else {
            //add to front
            string temp;
            temp += line[j];
            temp += answer;
            answer = temp;
         }
      }
      cout << "Case #" << i+1 << ": " << answer << endl;
   }
   iFile.close();
   return 0;
}
