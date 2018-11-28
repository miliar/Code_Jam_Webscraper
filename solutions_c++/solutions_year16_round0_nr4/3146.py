#include <iostream> 
#include <string> 
#include <vector> 
#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <queue> 
#include <string>
#include <string.h> 
using namespace std; 

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
#define INF 1000000000;
 
template <typename T>
void printLoop(vector<T> vec) {
  for( T t : vec) {
    cout << t << " "; 
  }
  cout << endl;
}

template <typename T>
void printdubLoop(vector<vector<T>> vec) {
  for( vector<T> v : vec) {
    printLoop(v); 
  }
}

template<class T>
bool findDuplicate(const vector<T>& v) {
  for(int i = 0; i < v.size(); i++) {
    for(int j = i + 1; j < v.size(); j++) {
      if(v[i] == v[j]) {
	return true;
      }
    }
  }
  return false;
}

template<class T>
void swap(T& a, T& b) {
  T temp = a;
  a = b;
  b = temp;
}

class timer {
public:
  timer() : start(clock()) {}
  double elapsed() { return ( clock() - start ) / CLOCKS_PER_SEC; }
  void reset() { start = clock(); }
private:
  double start;
};

void process(int k, int c, int s) {
  if (k == 1) cout << 1 << endl;
  else if (c == 1) {
    if (k > s) cout << "IMPOSSIBLE" << endl; 
    else {
      for(int i = 1; i < k+1; i++) cout << i << " ";
      cout << endl;
    }
  }
  else if (s <= k-2)  cout << "IMPOSSIBLE" << endl; 
  else {
    for(int i = 2; i < k+1; i++) cout << i << " ";
    cout << endl;
  }
}

  


int main() {
  int t, k, c, s; 
  cin >> t; 
  int i = 1; 
  while(t--) {
    cout << "Case #" << i++ << ": "; 
    cin >> k >> c >> s; 
    process(k, c, s); 
  }
  return 0; 
} 
