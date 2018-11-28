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
void printnLoop(vector<T> vec) {
  for( T t : vec) {
    cout << t;
  }
  cout << " "; 
}template <typename T>
void printfLoop(vector<T> vec) {
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



bool primes[65536];


vector<int> generate(int n) {
  vector<int> v;
  memset(primes, true, sizeof(primes));
  for(int i = 2; i < n;) {
    v.push_back(i);
    for(int j = 2; (j*i) < n; ++j) {

      primes[i*j] = false;
    }
    int k = i+1;
    for(; k < n; k++) {
      if(primes[k]) {
        i=k;
        break;
      }

    }
    if(k >= n) break;
  }
  return v;
}

pair<int, int> isPrime(long long n, vector<int> v) {
  for(int i : v) {
    if(i > sqrt(n)) return make_pair(1,0); 
    if(n % i == 0) return make_pair(0,i);

  }
  return make_pair(1,0);
}


long long binToBase(vector<int> v, int n) {
  long long sum = 0; 
  for(int i = 0; i  < v.size(); i++) {
    sum += v[i] * pow(n, v.size()-1-i);
  }
  return sum; 
}

void increment(vector<int>& v) {
  int carry = 1; 
  for(int i = v.size()-2; i > 1; i--) {
    if(v[i] && carry) {
      v[i] = 0;
      carry = 1; 
    }
    else if(v[i] && !carry) {
      v[i] = 1; 
      carry = 0; 
    }
    else if(!v[i] && carry) {
      v[i] = 1; 
      carry = 0; 
    }
    else {
      break;
    }
  }
}


int main() {

  vector<int> v = generate(65536);
  int t, n, j; 
  cin >> t; 
  int i = 1; 
  while(t--) {
    cout << "Case #" << i++ << ": " << endl; 
    cin >> n >> j; 
    vector<int> num(n, 0); 
    num[0] = 1; 
    num[num.size()-1] = 1; 

    int counter = 0; 
    vector< vector< int > > ret;
    vector<int> factors;
    while(counter < j) {
      factors.resize(0); 
      bool found = true; 

      for(int i = 2; i <= 10; i++) {
	pair<int,int> p = isPrime(binToBase(num,i), v);
	factors.push_back(p.second); 
	if(p.first) {
	  found = false; 
	  break; 
	}
      }
      if(found) {
	ret.push_back(num);
	ret.push_back(factors); 
	counter++;
      }
      increment(num);
    }
    for(int i = 0; i < ret.size(); i++) {
      vector<int> num = ret[i]; 
      printnLoop(num); 
      num = ret[++i]; 
      printfLoop(num); 
    }
  }
  return 0; 
} 
