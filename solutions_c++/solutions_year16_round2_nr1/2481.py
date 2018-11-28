//Joe Snider
//4/16
//
//codejam r1b, q1
#include <algorithm>
#include <vector>
#include <deque>
#include <iostream>
#include <string>
#include <list>
#include <iterator>
#include <math.h>

using namespace std;

string doit(string word) {
   vector<char> answer;
   //cases (cut and paste:)
   int pos;
   //zero
   while( word.find('Z') != string::npos) {
      answer.push_back('0');
      word.erase(word.find('Z'), 1);
      word.erase(word.find('E'), 1);
      word.erase(word.find('R'), 1);
      word.erase(word.find('O'), 1);
   }
   //two
   while( (pos = word.find('W')) != string::npos) {
      answer.push_back('2');
      word.erase(word.find('T'), 1);
      word.erase(word.find('W'), 1);
      word.erase(word.find('O'), 1);
   }
   //four
   while( (pos = word.find('U')) != string::npos) {
      answer.push_back('4');
      word.erase(word.find('F'), 1);
      word.erase(word.find('O'), 1);
      word.erase(word.find('U'), 1);
      word.erase(word.find('R'), 1);
   }
   //six
   while( (pos = word.find('X')) != string::npos) {
      answer.push_back('6');
      word.erase(word.find('S'), 1);
      word.erase(word.find('I'), 1);
      word.erase(word.find('X'), 1);
   }
   //eight
   while( (pos = word.find('G')) != string::npos) {
      answer.push_back('8');
      word.erase(word.find('E'), 1);
      word.erase(word.find('I'), 1);
      word.erase(word.find('G'), 1);
      word.erase(word.find('H'), 1);
      word.erase(word.find('T'), 1);
   }
   //one -- order matters
   while( (pos = word.find('O')) != string::npos) {
      answer.push_back('1');
      word.erase(word.find('O'), 1);
      word.erase(word.find('N'), 1);
      word.erase(word.find('E'), 1);
   }
   //three
   while( (pos = word.find('H')) != string::npos) {
      answer.push_back('3');
      word.erase(word.find('T'), 1);
      word.erase(word.find('H'), 1);
      word.erase(word.find('R'), 1);
      word.erase(word.find('E'), 1);
      word.erase(word.find('E'), 1);
   }
   //five
   while( (pos = word.find('F')) != string::npos) {
      answer.push_back('5');
      word.erase(word.find('F'), 1);
      word.erase(word.find('I'), 1);
      word.erase(word.find('V'), 1);
      word.erase(word.find('E'), 1);
   }
   //seven
   while( (pos = word.find('V')) != string::npos) {
      answer.push_back('7');
      word.erase(word.find('S'), 1);
      word.erase(word.find('E'), 1);
      word.erase(word.find('V'), 1);
      word.erase(word.find('E'), 1);
      word.erase(word.find('N'), 1);
   }
   //nine
   while( (pos = word.find('N')) != string::npos) {
      answer.push_back('9');
      word.erase(word.find('N'), 1);
      word.erase(word.find('I'), 1);
      word.erase(word.find('N'), 1);
      word.erase(word.find('E'), 1);
   }
   sort(answer.begin(), answer.end());
   string ret;
   ret.assign(answer.begin(), answer.end());
   return ret;
}

int main() {
   int N;
   string word;
   cin >> N;
   for(int i = 1; i <= N; ++i) {
      cin >> word;
      cout << "Case #" << i << ": " << doit(word) << "\n" << flush;
   }
}