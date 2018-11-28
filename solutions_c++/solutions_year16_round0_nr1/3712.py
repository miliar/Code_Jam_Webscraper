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

#define endl '\n'
using namespace std;

void check(vector<bool> &nums,long long num){
  string nstr = to_string(num);
  for(int i=0;i<nstr.length();i++){
    nums[nstr[i] - '0'] = true;
  }
}

bool isFin(vector<bool> &nums){
  for(int i=0;i<nums.size();i++)
    if(!nums[i])
      return false;
  return true;
}

int main(){

  std::ios_base::sync_with_stdio(false);
  int t;
  long long n;
  cin >> t;
  for(int tc=1;tc <= t;tc++){
    cin >> n;
    vector<bool> nums(10,false);

    if(n == 0){
      cout << "Case #" << tc << ": " << "INSOMNIA" << endl;
    }
    else{ 
      long long cur = n;
      check(nums,cur);
      while(!isFin(nums)){
        cur += n;
        check(nums,cur);
      }
      cout << "Case #" << tc << ": " << cur << endl;
    }
  }
  return 0;
}
