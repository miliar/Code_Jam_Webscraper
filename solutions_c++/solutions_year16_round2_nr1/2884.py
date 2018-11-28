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
      string answer = "";
      //zero
      size_t found = line.find("Z");
      size_t found2 = line.find("E");
      size_t found3 = line.find("R");
      size_t found4 = line.find("O");
      size_t found5;
      while (found != string::npos) {
         line[found] = '!';
         line[found2] = '!';
         line[found3] = '!';
         line[found4] = '!';
         found = line.find("Z");
         found2 = line.find("E");
         found3 = line.find("R");
         found4 = line.find("O");
         answer += '0';
      }
      //two
      found = line.find("T");
      found2 = line.find("W");
      found3 = line.find("O");
      while (found2 != string::npos) {
         line[found] = '!';
         line[found2] = '!';
         line[found3] = '!';
         found = line.find("T");
         found2 = line.find("W");
         found3 = line.find("O");
         answer += '2';
      }
      //four
      found = line.find("F");
      found2 = line.find("O");
      found3 = line.find("U");
      found4 = line.find("R");
      while (found3 != string::npos) {
         line[found] = '!';
         line[found2] = '!';
         line[found3] = '!';
         line[found4] = '!';
         found = line.find("F");
         found2 = line.find("O");
         found3 = line.find("U");
         found4 = line.find("R");
         answer += '4';
      }
      //six
      found = line.find("S");
      found2 = line.find("I");
      found3 = line.find("X");
      while (found3 != string::npos) {
         line[found] = '!';
         line[found2] = '!';
         line[found3] = '!';
         found = line.find("S");
         found2 = line.find("I");
         found3 = line.find("X");
         answer += '6';
      }
      //seven
      found = line.find("S");
      found2 = line.find("E");
      found3 = line.find("V");
      found4 = line.find("E", found2+1);
      found5 = line.find("N");
      while (found != string::npos && found2 != string::npos && found3 != string::npos
               && found4 != string::npos && found5 != string::npos) {
         line[found] = '!';
         line[found2] = '!';
         line[found3] = '!';
         line[found4] = '!';
         line[found5] = '!';
         found = line.find("S");
         found2 = line.find("E");
         found3 = line.find("V");
         found4 = line.find("E", found2+1);
         found5 = line.find("N");
         answer += '7';
      }
      //eight
      found = line.find("E");
      found2 = line.find("I");
      found3 = line.find("G");
      found4 = line.find("H");
      found5 = line.find("T");
      while (found != string::npos && found2 != string::npos && found3 != string::npos
               && found4 != string::npos && found5 != string::npos) {
         line[found] = '!';
         line[found2] = '!';
         line[found3] = '!';
         line[found4] = '!';
         line[found5] = '!';
         found = line.find("E");
         found2 = line.find("I");
         found3 = line.find("G");
         found4 = line.find("H");
         found5 = line.find("T");
         answer += '8';
      }
      //three
      found = line.find("T");
      found2 = line.find("H");
      found3 = line.find("R");
      found4 = line.find("E");
      found5 = line.find("E", found4+1);
      while (found != string::npos && found2 != string::npos && found3 != string::npos
               && found4 != string::npos && found5 != string::npos) {
         line[found] = '!';
         line[found2] = '!';
         line[found3] = '!';
         line[found4] = '!';
         line[found5] = '!';
         found = line.find("T");
         found2 = line.find("H");
         found3 = line.find("R");
         found4 = line.find("E");
         found5 = line.find("E", found4+1);
         answer += '3';
      }
      //five
      found = line.find("F");
      found2 = line.find("I");
      found3 = line.find("V");
      found4 = line.find("E");
      while (found != string::npos && found2 != string::npos
               && found3 != string::npos && found4 != string::npos) {
         line[found] = '!';
         line[found2] = '!';
         line[found3] = '!';
         line[found4] = '!';
         found = line.find("F");
         found2 = line.find("I");
         found3 = line.find("V");
         found4 = line.find("E");
         answer += '5';
      }
      //nine
      found = line.find("N");
      found2 = line.find("I");
      found3 = line.find("N", found+1);
      found4 = line.find("E");
      while (found != string::npos && found2 != string::npos
               && found3 != string::npos && found4 != string::npos) {
         line[found] = '!';
         line[found2] = '!';
         line[found3] = '!';
         line[found4] = '!';
         found = line.find("N");
         found2 = line.find("I");
         found3 = line.find("N", found+1);
         found4 = line.find("E");
         answer += '9';
      }
      //one
      found = line.find("O");
      found2 = line.find("N");
      found3 = line.find("E");
      while (found != string::npos && found2 != string::npos && found3 != string::npos) {
         line[found] = '!';
         line[found2] = '!';
         line[found3] = '!';
         found = line.find("O");
         found2 = line.find("N");
         found3 = line.find("E");
         answer += '1';
      }
      string answerFormatted;
      for (int j = 0; j < answer.length(); j++) {
         if (answer[j] == '0')
            answerFormatted += answer[j];
      }
      for (int j = 0; j < answer.length(); j++) {
         if (answer[j] == '1')
            answerFormatted += answer[j];
      }
      for (int j = 0; j < answer.length(); j++) {
         if (answer[j] == '2')
            answerFormatted += answer[j];
      }
      for (int j = 0; j < answer.length(); j++) {
         if (answer[j] == '3')
            answerFormatted += answer[j];
      }
      for (int j = 0; j < answer.length(); j++) {
         if (answer[j] == '4')
            answerFormatted += answer[j];
      }
      for (int j = 0; j < answer.length(); j++) {
         if (answer[j] == '5')
            answerFormatted += answer[j];
      }
      for (int j = 0; j < answer.length(); j++) {
         if (answer[j] == '6')
            answerFormatted += answer[j];
      }
      for (int j = 0; j < answer.length(); j++) {
         if (answer[j] == '7')
            answerFormatted += answer[j];
      }
      for (int j = 0; j < answer.length(); j++) {
         if (answer[j] == '8')
            answerFormatted += answer[j];
      }
      for (int j = 0; j < answer.length(); j++) {
         if (answer[j] == '9')
            answerFormatted += answer[j];
      }
      cout << "Case #" << i+1 << ": " << answerFormatted << endl;
   }
   iFile.close();
   return 0;
}
