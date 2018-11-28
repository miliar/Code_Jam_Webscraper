#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

using namespace std;
bool digitFound[10];

void setupArray() {
   for (int i = 0; i < 10; i++) {
      digitFound[i] = false;
   }
}

bool checkArray() {
   for (int i = 0; i < 10; i++) {
      if (digitFound[i] == false)
         return false;
   }
   return true;
}

int main() {
   setupArray();
   string line;
   ifstream iFile("input.txt");
   if (!iFile.is_open()) {
      cout << "Input file not found." << endl;
      return 1;
   }
   getline(iFile, line);
   istringstream buffer(line);
   int numCases;
   buffer >> numCases;
   for (int i = 0; i < numCases; i++) {
      setupArray();
      getline(iFile, line);
      buffer.str(line);
      int startingNum;
      int numAttempts = 1;
      buffer >> startingNum;
      for(; !checkArray(); numAttempts++) {
         int current = startingNum*numAttempts;
         while(current) {
            int lastDigit = current%10;
            digitFound[lastDigit] = true;
            current /= 10;
         }
         if (numAttempts >= 50000)
            break;
      }
      numAttempts--;
      if(!checkArray()) {
         cout << "Case #" << i+1 << ": INSOMNIA" << endl;
      } else {
         cout << "Case #" << i+1 << ": " << numAttempts*startingNum << endl;
      }
   }
   iFile.close();
   return 0;
}