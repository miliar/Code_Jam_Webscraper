#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

int main(int argc, char *argv[]){
  int cases;
  cin >> cases;

  for(int c=1;c<=cases;++c){
    vector<int> stack;
    string line;
    cin >> line;
    for(auto c : line){
      if(c == '-')
        stack.emplace_back(0);
      else
        stack.emplace_back(1);
    }
    
    int moves = 0;
    while(accumulate(stack.begin(), stack.end(), 0) != stack.size()){
      //find first distinct
      auto pos = stack.begin()+1;
      while(pos != stack.end()){
        if(*pos != stack[0])
          break;
        ++pos;
      }

      //reverse the equal elements
      transform(stack.begin(), pos, stack.begin(), [](int n) { return 1-n; });
      reverse(stack.begin(), pos);

      ++moves;
    }
    cout << "Case #" << c << ": " << moves << endl;
  }
}
