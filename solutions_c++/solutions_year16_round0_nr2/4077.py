#include <iostream>
#include <fstream>
#include <string>
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
      int numFlips = 0;
      for (int i = line.length()-1; i >= 0; i--) {
         if (line[i] == '-' && numFlips%2 == 0)
            numFlips++;
         if (line[i] == '+' && numFlips%2 == 1)
            numFlips++;
      }
      cout << "Case #" << i+1 << ": " << numFlips << endl;
   }
   iFile.close();
   return 0;
}