/*! if g++ -g a.cpp -o a.out; then ./a.out < a.test; fi
 */

#include <sstream>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <iostream>
#include <utility>
#include <set>
#include <cctype>
#include <queue>
#include <stack>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iterator>
#include <numeric>
#include <functional>



using namespace std;
typedef unsigned long long ull;
typedef long long ll;

void doit(int t){
  int n1, n2;
  int x[4][4];
  cin >> n1;
  n1--;
  for(int i = 0; i < 4; i++){
    for(int j = 0; j < 4; j++){
      cin >> x[i][j];
    }
  }
  set<int> ans;
  for(int i = 0; i < 4; i++){
    ans.insert(x[n1][i]);
  }
  cin >> n2;
  n2--;
  for(int i = 0; i < 4; i++){
    for(int j = 0; j < 4; j++){
      cin >> x[i][j];
    }
  }
  int ret, num;
  num = 0;
  for(int i = 0; i < 4; i++){
    set<int>::iterator it = ans.find(x[n2][i]);
    if(it != ans.end()){
      num++;
      ret = *it;
    }
  }
  cout << "Case #" << t << ": ";
  if(num==0){
    cout << "Volunteer cheated!" << endl;
  }
  else if(num > 1){
    cout << "Bad magician!" << endl;
  }
  else{
    cout << ret << endl;
  }
}

int main(int argc, char *argv[]){
  int t;
  cin >> t;
  for(int i = 0; i < t; i++){
    doit(i+1);
  }
  return 0;
}
