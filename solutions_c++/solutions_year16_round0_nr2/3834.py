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

void flip(vector<bool>& v, int i) {
  for(int j = 0; j < i ; j++) {
    v[j] = !v[j]; 
  }
}

void process(vector<bool>& v) {
  bool first = v[0];
  int counter = 0; 
  for(int i = 1; i < v.size(); i++) {
    bool b = v[i]; 
    if (b != first) {
      counter++; 
      flip(v, i);
      i = 0; 
      first = v[i]; 
    } 
  }
  if(!v[0]) counter++; 
  cout << counter << endl;
}

int main() {
  int t, k = 1; 
  string pancakes; 
  cin >> t; 
  while(t--) {
    cout << "Case #" << k++ << ": ";
    cin >> pancakes; 
    vector<bool> v; 
    for(char c : pancakes) c=='+' ? v.push_back(1) : v.push_back(0);   
    process(v); 

  }
  return 0; 
} 
