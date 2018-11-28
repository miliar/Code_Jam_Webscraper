#include <cmath>
#include <cstdint>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <map>
#include <algorithm>


using namespace std;

bool all_seen(bool (&seen)[10]){
  for(bool b: seen){
    if(!b)
      return false;
  }
  return true;
}

void mark_seen(bool (&seen)[10], uint64_t N){
  stringstream ss;
  ss << N;
  string str = ss.str();
  for(char c: str){
    string s;
    s.push_back(c);
    seen[stoi(s)] = true;
  }
}

int main(){
  int T;
  cin >> T;
  for(int t=1; t<=T; ++t){
    uint64_t N;
    cin >> N;
    if(N==0){
      cout << "Case #" << t << ": INSOMNIA" << endl;
      continue;
    }
    uint64_t count = 1;
    bool seen[10] = {false,false,false,false,false,false,false,false,false,false};
    for(;!all_seen(seen); ++count){
      mark_seen(seen,count*N);
    }
    cout << "Case #" << t << ": " << (count-1)*N << endl;
  }
}
