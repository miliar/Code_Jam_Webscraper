#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>
#include <iostream>
#include <fstream>
using namespace std;

int calculateFriendsNeeded(string s);
int main() {
  string line;
  ifstream inputf ("input.txt");
  int line_no = 0;
  int T;
  int S_max;
  int case_no = 1;
  string s;
  if (inputf.is_open())
  {
        //test numbers
        getline (inputf,line);
        T = stoi(line);

      while(getline (inputf, line, ' ')){
        S_max = stoi(line);
        getline (inputf, line);
        s = line;
        cout << "Case #" << case_no << ": " << calculateFriendsNeeded(s)<< endl;
        ++case_no;
    }
  }
    inputf.close();

  return 1;
}

int calculateFriendsNeeded(string s){
  int needed_friends = 0;
  int i = 0;
  int currently_standing = 0;
  while(i < s.size()){
    while(currently_standing < i)
    {
      ++needed_friends;
      ++currently_standing;
    }
    char c = s[i];
    currently_standing += c - '0';
    ++i;
  }
  return needed_friends;
}
