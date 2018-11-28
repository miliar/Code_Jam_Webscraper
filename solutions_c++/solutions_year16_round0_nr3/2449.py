#include<iostream>
#include<vector>


using namespace std;
typedef unsigned long long ull;

void addOne(string& s) {
  
  int i = s.length() - 2;
  s[i] = s[i] + 1;

  while(s[i] > '1') {
    s[i] = '0';
    if(i-1 < 0) break;
    s[i-1] = s[i-1] + 1;
    --i;
  }
}

ull findDivisor(ull number) {
  for(ull i=2; i * i <  number; ++i) {
    if(number % i == 0) {
      return i;
    }
  }
  return 1;
}

void solve(ull N, ull J) {
  string number(N,'0');
  number[0] = '1';
  number[number.size()-1] = '1';
  int j = 0;
  while(j < J) {
    vector<ull> divisors;
    for(int base = 2; base <= 10; ++base) {
      ull interpreted = stoull(number, NULL, base);
      ull result = findDivisor(interpreted);
      if(result == 1) {
        break;
      } else {
        divisors.push_back(result); 
      }
    }
    if(divisors.size() == 9){
      ++j;
      cout<<number;
      for(auto di : divisors) {
        cout<<" "<<di;
      }
      cout<<endl;
    }
    addOne(number);
  }
}

int main() {
  int T;
  cin >> T;
  for(int t=0;t < T; ++t) {

    ull N, J; 
    cin >> N >> J;
    cout<<"Case #" << t + 1 << ":" <<endl;
    solve(N, J);
  }
}
