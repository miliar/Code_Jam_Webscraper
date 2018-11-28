#include <iostream>
#include <vector>
#define N 100000000LL
using namespace std;

short int eratosthenes[N];
vector<int> primes;

void compute() {
  for(long long int i=2;i<N;i++) {
    if(eratosthenes[i]==0) {
      for(long long int j=i*i;j<N;j+=i) {
        eratosthenes[j] = i;
      }
    }
  }
  for(int i=2;i<N;i++) {
    if(eratosthenes[i]==0){
      primes.push_back(i);
    }
  }
}

int get_divisor(long long int n) {
  if(n<N) {
    return eratosthenes[n]; 
  }
  for(auto& e: primes) {
    if(n%e==0)
      return e;
  }
  return 0;
}

long long int base(long long int x, int b) {
  long long int ret = 0;
  long long int p =1;
  while(x) {
    ret += p*(x%2);
    p*=b;
    x/=2;
  }
  return ret;
}

int main () {
  cout<<"Case #1:"<<endl;
  int n=16;
  compute();
  long long int start = (1LL<<(n-1))+1;
  long long int stop = 1LL<<(n);

  int count = 0;
  for(long long int i=start;i<stop;i+=2) {
    bool flag = true;
    for(int b=2;b<=10;b++) {
      if(get_divisor(base(i,b))==0) { 
        flag=false;
        break;
      }
    }
    if(flag) {
      count++;
      cout<<base(i,10)<<" ";
      for(int b=2;b<=10;b++) {
        cout<<get_divisor(base(i,b))<<" ";
      }
      cout<<endl;
      if(count==50) {break;}
    }
  }
  return 0;
}
