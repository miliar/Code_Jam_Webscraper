/********   All Required Header Files ********/
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>
#include <deque>
#include <bitset>
#include <iterator>
#include <list>
#include <stack>
#include <map>
#include <set>
#include <functional>
#include <numeric>
#include <utility>
#include <limits>
#include <time.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<ii > vii;

int ch[10][26];

bool pairCompare(const std::pair<int, int>& firstElem, const std::pair<int, int>& secondElem) {
  return firstElem.first > secondElem.first;
}

string sol(vii v) {
  string moves;
  sort(v.begin(), v.end(), pairCompare);
  while(v[0].first > 0) {
    if(moves != "") moves += " ";
    if(v.size() == 1) {
      printf("ERRROR\n");
    } else if(v.size() == 3 && v[0].first == 1 && v[1].first == 1 && v[2].first == 1) {
      v[0].first --;
      moves += 'A' + v[0].second;
    } else if(v[0].first > v[1].first) {
      v[0].first -= 2;
      moves += 'A' + v[0].second;
      moves += 'A' + v[0].second;
    } else if(v[0].first == v[1].first ) {
      v[0].first --;
      v[1].first --;
      moves += 'A' + v[0].second;
      moves += 'A' + v[1].second;
    }
    
    sort(v.begin(), v.end(), pairCompare);
    v.erase(remove_if(v.begin(), v.end(), [](pair<int, int> x){ return x.first == 0;} ), v.end());
  }
  //printf("hello %s\n", moves.c_str());
  return moves;

}


int main(){
  vii v,w;
  v = {make_pair(2,0), make_pair(2,1)};
  assert(sol(v) == "AB AB");
  v = {make_pair(3,0), make_pair(2,1), make_pair(2,2)};
  assert(sol(v) == "AA BC B CA");
  v = {make_pair(1,0), make_pair(1,1), make_pair(2,2)};
  assert(sol(v) == "CC AB");
  v = {make_pair(2,0), make_pair(3,1), make_pair(1,2)};
  assert(sol(v) == "BB AA BC");


  //assert(move(vi({3,3,1})) == vi({2,2,1}));
  //assert(move(vi(3,2,2)) == vi(2,2,1);
	 //assert(move(vi(3,2,1)) == vi(2,2,0);
  

  int T;
  cin >> T;
  for (int i=1;i<=T;i++) {
    int N;
    cin >> N;
    vii v;
    for(int j=0;j<N;j++) {
      int w;
      cin >> w;
      v.push_back(make_pair(w, j));
    }
    printf("Case #%d: %s\n", i, sol(v).c_str());
  }
}






