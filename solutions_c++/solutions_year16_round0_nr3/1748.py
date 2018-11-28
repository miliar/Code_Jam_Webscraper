#include <iostream>
#include <string>
#include <cstdio>
#include <ctime>
#include <cstdlib>
#include <vector>
#include <map>
using namespace std;

#define N 16

map<string, vector<long long> > all;

long long isprime(long long num) {
  if(num <= 1) return 0;
  for(long long i = 2; i*i <= num; i++) {
    if(num%i == 0) return i;
  }
  return 0;
}

long long convert(string str, long long base) {
  long long result = 0;
  for(int i = 0; i < (int) str.size(); i++) {
    result *= base;
    result += str[i]-'0';
  }
  return result;
}

string generate() {
  string cur;
  for(int i = 0; i < N; i++)
    cur+= "1";
  
  for(int i = 1; i < N-1; i++) {
    cur[i] = '0'+(rand()%2);
  }
  return cur;
}

int main() {
  srand(time(NULL));

  do {
    string cur = generate();
    vector<long long> rems;
    bool good = true;
    for(long long base = 2; base <= 10; base++) {
      long long res = convert(cur, base);
      long long crem = isprime(res);
      rems.push_back(crem);
      if(crem == 0) good = false;
    }
    if(good && all.find(cur) == all.end()) {
      all[cur] = rems;
    }
  } while(all.size() < 50);
  cout << "Case #1:" << endl;
  for(typeof(all.begin()) it = all.begin(); it != all.end(); it++) {
    cout << (*it).first;
    for(int i = 0; i <9; i++) {
      cout << " " << (*it).second[i];
    }
    cout << endl;
  }
  return 0;
}
