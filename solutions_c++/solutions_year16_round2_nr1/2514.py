#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <cstdlib>
#include <climits>

using namespace std;


int T;

int main (int argc, char const *argv[])
{
  cin >> T;
  for (size_t i =  1; i <= T; i++) {
    string s;
    cin >> s;
    map<char,int> m;
    for(auto &&c:s) {
      m[c] += 1;
    }
    int zero = m['Z']; for (char c:"ZERO") m[c] -= zero;
    int two = m['W']; for (char c:"TWO") m[c] -= two;
    int four = m['U']; for (char c:"FOUR") m[c] -= four;
    int six = m['X']; for (char c:"SIX") m[c] -= six;
    int eight = m['G']; for (char c:"EIGHT") m[c] -= eight;
    int three = m['H']; for (char c:"THREE") m[c] -= three;
    int five = m['F']; for (char c:"FIVE") m[c] -= five;
    int seven = m['S']; for (char c:"SEVEN") m[c] -= seven;
    int one = m['O']; for (char c:"ONE") m[c] -= one;
    int nine = m['I']; for (char c:"NINE") m[c] -= nine;

    cout << "Case #" << i << ": " ;
    for (size_t i = 0; i < zero; i++)  cout << "0" ;
    for (size_t i = 0; i < one; i++)   cout << "1" ;
    for (size_t i = 0; i < two; i++)   cout << "2" ;
    for (size_t i = 0; i < three; i++) cout << "3" ;
    for (size_t i = 0; i < four; i++)  cout << "4" ;
    for (size_t i = 0; i < five; i++)  cout << "5" ;
    for (size_t i = 0; i < six; i++)   cout << "6" ;
    for (size_t i = 0; i < seven; i++) cout << "7" ;
    for (size_t i = 0; i < eight; i++) cout << "8" ;
    for (size_t i = 0; i < nine; i++)  cout << "9" ;
    cout << endl;
  }

  return 0;
}
