#include <algorithm>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <cmath>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i!=(b);++i) 
#define REP(i,n) FOR(i,0,n) 
#define dbg(x)   (cout << #x << ":" << (x) << "\t") 
#define dbge(x) (cout << #x << ":" << (x) << "\n") 
#define all(c) c.begin(), c.end() 
#define cpresent(container, element) (find(all(container),element) != container.end())

bool palindrome(int num){
  string s = "";
  int numcpy = num;
  vector <int> num_items;

  while(numcpy > 0){
    int lastnum = numcpy % 10;
    numcpy  = numcpy/10;
    num_items.push_back(lastnum);
  }

  int len = num_items.size();
  bool palin = true;
  for(int i=0;i<len/2;i++) {
    if(num_items[i] != num_items[len-i-1])
    {
      palin = false;
      break;
    }
  }

  return palin;
}

int main() {
  int count, min, max, minsqrt, maxsqrt, counter = 0, number, fsq_count;
  cin >> count;

  while(counter < count)
  {
    fsq_count = 0;
    cin >> min >> max;
    minsqrt = floor(sqrt(min));
    maxsqrt = ceil(sqrt(max));
    for(int i=minsqrt; i <= maxsqrt; i++){
      number = i*i;
      if( number >= min && number <= max && palindrome(number) && palindrome(i))
      {
        fsq_count++;
      }
        
    }

    cout << "Case #" << (counter + 1) << ": " << fsq_count << endl;
  	counter++;
  }

  return 0;
}
