#include <iostream>
#include <string>

using namespace std;

int opt_flips(string pc) {
  int ret = 0;
  bool flipped = false;
  char state;
  char begin = *pc.begin();
  for(auto iter = pc.begin(); iter != pc.end(); ++iter) {
    if(iter == pc.begin())
      state = *iter;
    if(iter != pc.begin() && *iter != state) {
      ++ret;
      flipped = true;
      (state == '-')? state = '+': state = '-';
    }
  }
  if((begin == '-' && *(pc.end()-1) == '-') || *(pc.end() - 1) == '-') ++ret;
  return ret;
}
      


int main() {
  int t;
  string n;
  cin>>t;
  for(int i = 0; i < t; ++i) {
    cin >> n;
    cout << "Case #"<< i+1<<": "<<opt_flips(n)<<endl;
  }
  return 0;
}
