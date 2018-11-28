#include <iostream>
#include <utility>
#include <vector>
#include <cmath>
using namespace std;

pair <int, int> add(int num){
  num++;
  if(num == 2){
    return make_pair(1,0);
  }
  return make_pair(0,num);
}

bool inc(vector<int> &base, int limit){
  int carry = 1;
  int pos = 1;
  while(carry == 1){
    pair <int, int> info = add(base[pos]);
    carry = info.first;
    base[pos] = info.second;
    pos++;
    if(pos == limit){
      return false;
    }
  }
  return true;
}

int main(){
  int cases, n, j;
  cin >> cases;
  cin >> n >> j;
  cout << "Case #" << cases << ":\n";
  vector<int> base(n,0);
  base[0] = 1;
  base[1] = -1;
  base[n-1] = 1;
  int anscount = 0;
  vector<long long> ans;
  while(inc(base,n)){
    if(anscount == j){
      break;
    }
    ans.resize(0);
    for(int b = 2; b<11; b++){
      long long lbase = 0;
      for(int i = 0; i<base.size(); i++){
        if(base[i] == 1){
          lbase += pow(b,i);
        }
      }
      //cout << b << ": " << lbase << endl;
      if(lbase%2==0){
        ans.push_back(2);
      }
      else if(lbase%3==0){
        ans.push_back(3);
      }
      else{
        long long t = 5;
        while(!((t*t)>lbase)){
          if(lbase%t==0){
            ans.push_back(t);
            break;
          }
          else if(lbase%(t+2)==0){
            ans.push_back(t+2);
            break;
          }
          t += 6;
        }
      }
      if(ans.size() == 9){
        cout << lbase;
        for(int s = 0; s<ans.size(); s++){
          cout << " " << ans[s];
        }
        cout << endl;
        anscount++;
      }
    }
  }
}
