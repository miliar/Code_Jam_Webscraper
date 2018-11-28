#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

void add_pile(vector<int> &piles, int i){
  piles.push_back(i);
  push_heap(piles.begin(),piles.end());
}

int take_pile(vector<int> &piles){
  pop_heap(piles.begin(),piles.end());
  int ret = piles.back();
  piles.pop_back();
  return ret;
}

int calc(vector<int> piles, int moves, int min){
  if(moves >= min){
    return min;
  }
  if(moves+piles[0]<min){
    min = moves+piles[0];
  }
  {
    auto p = piles;
    int top = take_pile(p);
    add_pile(p,top-top/2);
    add_pile(p,top/2);
    int ret = calc(p,moves+1,min);
    if(ret<min) min = ret;
  }
  {
    auto p = piles;
    int top = take_pile(p);
    add_pile(p,top-2*top/3);
    add_pile(p,top/3);
    add_pile(p,top/3);
    int ret = calc(p,moves+2,min);
    if(ret<min) min = ret;
  }
  return min;
}

int main(){
  int T;
  cin >> T;
  for(int t=1; t<=T; ++t){
    vector<int> input_piles;
    
    int D;
    cin >> D;
    for(int d=0; d<D; ++d){
      int tmp;
      cin >> tmp;
      input_piles.push_back(tmp);
    }
    make_heap(input_piles.begin(),input_piles.end());
    int min = input_piles[0];
    min = calc(input_piles, 0, min);
    cout << "Case #" << t << ": " << min << endl;
  }
}
