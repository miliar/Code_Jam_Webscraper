#include <iostream>
#include <string>

int find_max(std::string a) {
  std::string::iterator itr = a.begin();
  std::string::iterator found = a.begin();
  int counter = 0;
  int position = 0;
  while(itr != a.end()) {
    if(*itr >= *found) {
      found = itr;
      position = counter;
    }
    ++itr;
    ++counter;
  }
  return position;
}

std::string do_sort(std::string str) {
  if(str.size() == 0) {
    return "";
  }
  if(str.size() == 1) {
    return str;
  }

  int res = find_max(str); 
  std::string first = str.substr(res,1);
  std::string section1 = do_sort(str.substr(0,res));
  std::string section2 = str.substr(res+1, str.size());
  //std::string section2 = do_sort(str.substr(res+1, str.size()));
  return first + section1 + section2;
}

int main() {
  int cases = 0;
  int counter = 1;
  std::cin >> cases;

  while(cases--) {
    std::string str;
    std::cin >> str;
    std::cout << "Case #" << counter << ": ";
    std::cout << do_sort(str) << "\n";
    ++counter;
  }
  
  return 0;
}
