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



int arr[10]; 
long long counter; 
long long process(long long n, long long num) {

  long long ret = n; 
  n *= num; 
  while(n) {
    long long x = n % 10;

    n = n/10; 
    if(!arr[x]) {
      arr[x] = true; 
      counter++; 
    }
  }
  if(counter == 10) return ret*num; 
  else return process(ret, num+1); 
}

int main() {
  long long t, n; 
  cin >> t; 
  long long i = 1; 
  while(t--) {
    cout << "Case #" << i++ << ": ";
    counter = 0; 
    memset(arr, false, sizeof(arr)); 
    cin >> n;
    if (n == 0) cout << "INSOMNIA" << endl; 
    else cout << process(n, 1) << endl; 
    
  }
  return 0; 
} 
