#include <iostream>
#include <iostream>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <vector>
#include <set>
#include <algorithm>
#include <iomanip>
#include <map>

using namespace std;

#define mp make_pair
#define pb push_back

typedef long long ll;


int main(){

  int t;
  string pancakes;
  cin >> t;

  for (int i = 1; i <= t; ++i)
  {
    cin >> pancakes;
    ll ct = 0;
    for (int j = 1; j < pancakes.length(); j++){
      if(pancakes[j] != pancakes[j-1]) ct++;
    }

    if(pancakes[pancakes.length() - 1] == '-'){
      ct++;
    }


    cout << "Case #" << i << ": " << ct << "\n";
  }

  return 0;
}
