//Joe Snider
//4/16
//
//codjam 2016 qual b (pancakes)
//  g++ -std=c++11

#include <algorithm>
#include <vector>
#include <iostream>
#include <string>
#include <iterator>

using namespace std;

void disp(const vector<char>& x) {
   copy(x.begin(), x.end(), ostream_iterator<char>(cout, " "));
   cout << "\n" << flush;
}

//flip the whole thing
void flip(vector<char>& stack) {
   int n = stack.size()-1;
   vector<char> q = stack;
   for(int i = 0; i < stack.size(); ++i) {
      stack[i] = (q[n-i]=='+')?'-':'+';
   }
}

int doit(vector<char>& stack) {
   int count = 0;
   while(stack.size() > 0) {
      while(stack.back() == '+') {
          stack.pop_back();
      }
      if(stack.size() == 0) {return count;}
      
      //disp(stack);
      
      int nl = 0;
      for(auto it = stack.begin(); it != stack.end() && *it == '-'; ++it, ++nl);
      int pl = 0;
      for(auto it = stack.begin(); it != stack.end() && *it == '+'; ++it, ++pl);
      
      if(nl == 0) {
         //flip up to pl, to set up for next time
         for(int i = 0; i < pl; ++i) {
            stack[i] = '-';
         }
      } else {
         flip(stack);
      }
      count += 1;
      
   }

   //shouldn't get here
   cerr << "oops1\n" << flush;
   return -1;
}

int main() {
   int T;
   char c;
   string s;
   cin >> T;
   int count = 1;
   while(cin >> s) {
      vector<char> stack;
      for(int i = 0; i < s.length(); ++i) {
         stack.push_back(s[i]);
      }
      cout << "Case #" << count << ": " << doit(stack) << "\n" << flush;
      ++count;
   }
   return 0;
}

