#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
  int cases; cin >> cases;
  string s = "a";
  vector<int> my;
  for(int i = 1; i<cases+1; i++){
    my.clear();
    string s; cin >> s;
    while(s.length() > 0){
      if(s.find('Z') != string::npos){
        my.push_back(0);
        s.erase(s.begin() + s.find('Z'));
        s.erase(s.begin() + s.find('E'));
        s.erase(s.begin() + s.find('R'));
        s.erase(s.begin() + s.find('O'));
      }
      else if(s.find('W') != string::npos){
        my.push_back(2);
        s.erase(s.begin() + s.find('T'));
        s.erase(s.begin() + s.find('W'));
        s.erase(s.begin() + s.find('O'));
      }
      else if(s.find('U') != string::npos){
        my.push_back(4);
        s.erase(s.begin() + s.find('F'));
        s.erase(s.begin() + s.find('O'));
        s.erase(s.begin() + s.find('U'));
        s.erase(s.begin() + s.find('R'));
      }
      else if(s.find('X') != string::npos){
        my.push_back(6);
        s.erase(s.begin() + s.find('S'));
        s.erase(s.begin() + s.find('I'));
        s.erase(s.begin() + s.find('X'));
      }
      else if(s.find('G') != string::npos){
        my.push_back(8);
        s.erase(s.begin() + s.find('E'));
        s.erase(s.begin() + s.find('I'));
        s.erase(s.begin() + s.find('G'));
        s.erase(s.begin() + s.find('H'));
        s.erase(s.begin() + s.find('T'));
      }
      else{
        break;
      }
    }
    while(s.length() > 0){
      if(s.find('O') != string::npos){
        my.push_back(1);
        s.erase(s.begin() + s.find('O'));
        s.erase(s.begin() + s.find('N'));
        s.erase(s.begin() + s.find('E'));
      }
      else if(s.find('F') != string::npos){
        my.push_back(5);
        s.erase(s.begin() + s.find('F'));
        s.erase(s.begin() + s.find('I'));
        s.erase(s.begin() + s.find('V'));
        s.erase(s.begin() + s.find('E'));
      }
      else if(s.find('S') != string::npos){
        my.push_back(7);
        s.erase(s.begin() + s.find('S'));
        s.erase(s.begin() + s.find('E'));
        s.erase(s.begin() + s.find('V'));
        s.erase(s.begin() + s.find('E'));
        s.erase(s.begin() + s.find('N'));
      }
      else if(s.find('H') != string::npos){
        my.push_back(3);
        s.erase(s.begin() + s.find('T'));
        s.erase(s.begin() + s.find('H'));
        s.erase(s.begin() + s.find('R'));
        s.erase(s.begin() + s.find('E'));
        s.erase(s.begin() + s.find('E'));
      }
      else{
        break;
      }
    }
    while(s.length() > 0){
      if(s.find('N') != string::npos){
        my.push_back(9);
        s.erase(s.begin() + s.find('N'));
        s.erase(s.begin() + s.find('I'));
        s.erase(s.begin() + s.find('N'));
        s.erase(s.begin() + s.find('E'));
      }
      else{
        break;
      }
    }
    sort(my.begin(), my.end());
    cout << "Case #" << i << ": ";
    for(int q = 0; q< my.size(); q++){
      cout << my[q];
    }
    cout << endl;
  }
}
