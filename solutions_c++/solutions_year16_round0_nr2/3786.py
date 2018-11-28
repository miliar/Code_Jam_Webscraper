#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <limits>
#include <utility>
#include <iomanip>
#include <cassert>
#include <map>

#define endl '\n'
using namespace std;

string pancake;

void rev_pancake(string &origin,int top){
  reverse(origin.begin(),origin.begin()+top+1);
  for(int i=0;i<=top;i++){
    origin[i] = (origin[i] == '+' ? '-' : '+');
  }
}

int greedy(){
  int ret = 0;

  while(true){
    int end = 0;
    while(end < pancake.length() && pancake[0] == pancake[end])
      end++;

    if(end == pancake.length()){
      if(pancake[0] == '-')
        return ret+1;
      else
        return ret;
    }
    else{
      rev_pancake(pancake,end-1);
      ret++;
    }
  }
  //do not come here
  assert(false);
}


int main(){

  std::ios_base::sync_with_stdio(false);
  int t;
  cin >> t;
  for(int tc=1;tc<=t;tc++){
    cin >> pancake;
    cout << "Case #" << tc << ": " << greedy() << endl;
  }
  return 0;
}
