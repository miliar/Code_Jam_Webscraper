#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>

void initialize_map(std::map<char,int>& myMap) {
  std::string chars = "ZEROONETWOTHREEFOURFIVESIXSEVENEIGHTNINE";
  std::string::iterator itr = chars.begin();
  while(itr != chars.end()) {
    myMap.insert(std::make_pair(*itr,0));
    ++itr;
  }
}

void remove_num(std::map<char, int>& myMap, std::string s) {
  std::string::iterator itr = s.begin();
  while(itr != s.end()) {
    int curr = myMap[*itr];
    myMap[*itr] = curr - 1;
    ++itr;
  } 
}

void read_string(std::map<char,int>& myMap, std::string s) {
  std::string::iterator itr = s.begin();
  while(itr != s.end()) {
    int curr = myMap[*itr];
    myMap[*itr] = curr + 1;
    ++itr;
  }
}

bool less_than_zero_vals(std::map<char,int>& myMap) {
  std::map<char,int>::iterator itr = myMap.begin();
  while(itr != myMap.end()) {
    if(itr->second < 0) {
      return true;
    }
    ++itr;
  }
  return false;
}

long map_count(std::map<char,int>& myMap) {
  std::map<char,int>::iterator itr = myMap.begin();
  long totals = 0;
  while(itr != myMap.end()) {
    totals += itr->second;
    ++itr;
  }
  return totals;
}

std::string get_number(std::string s, int start) {
  std::map<char, int> myMap;
  initialize_map(myMap);
  read_string(myMap, s);
  std::string res = "";
 
  std::vector<char> nums_int = {'0','2','4','6','8','5','7','9','3','1'};
  std::vector<std::string> nums = {"ZERO","TWO", "FOUR", "SIX", "EIGHT", "FIVE", "SEVEN", "NINE", "THREE", "ONE"};
  std::vector<std::string>::iterator itr = nums.begin();
  while(itr != nums.end()) {
    remove_num(myMap, *itr);
    if(less_than_zero_vals(myMap)) {
      read_string(myMap, *itr); 
      ++itr;
    } else if(start > 0) {
      read_string(myMap, *itr);
      ++itr;
      --start;
    } else {
       res += nums_int[itr - nums.begin()];
    }
  }
   
  //if(map_count(myMap) != 0) {
  //  std::cout << map_count(myMap) << "\n";
  //}
  std::sort(res.begin(), res.end());
  return res;
}

int main() {
  int cases = 0;
  int counter = 1;
  std::cin >> cases;
  while(cases--) {
    std::string s;
    std::cin >> s;
    std::cout << "Case #" << counter << ": ";
    std::cout << get_number(s, 0) << "\n";
    ++counter;
  }
  return 0;
}
