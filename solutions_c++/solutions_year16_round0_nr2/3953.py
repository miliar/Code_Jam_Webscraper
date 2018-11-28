#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <regex>

std::string ReplaceAll(std::string str, const std::string& from, const std::string& to) {
    size_t start_pos = 0;
    while((start_pos = str.find(from, start_pos)) != std::string::npos) {
        str.replace(start_pos, from.length(), to);
        start_pos += to.length(); // Handles case where 'to' is a substring of 'from'
    }
    return str;
}

int main (void) {

   int n;
   scanf("%d\n", &n);
   std::string s;
   
   for (int i = 0; i < n; ++i) {
      std::cin >> s;
      int ans = 0;
      while (s.size() != (unsigned int) std::count(s.begin(), s.end(), '+')) {
         if (s[s.size()-1] != '-') {
            //std::cout << "btrimmed: " << s << std::endl;
            s.resize(s.find_last_of("-")+1);
            //std::cout << "atrimmed: " << s << std::endl;
         }
         if (s.find_last_of("+") < s.find_last_of("-")) {
            s = s.substr(0, s.find_last_of("+")+1);
            //std::cout << "Before: " << s << std::endl;

            s = ReplaceAll (s, std::string("-"), std::string("5"));
            s = ReplaceAll (s, std::string("+"), std::string("-"));
            s = ReplaceAll (s, std::string("5"), std::string("+"));
            //std::cout << "After: " << s << std::endl;
            ans++;
         } else {
            ans++;
            break;
         }
      }
      
      
      std::cout << "Case #" << i+1 << ": " << ans << std::endl;
   }
}
