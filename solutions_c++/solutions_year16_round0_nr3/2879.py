#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>
#include <cmath>

using namespace std;
bool isPrime(unsigned long long n){
  //unsigned int a = rand() % (n-4) + 2;
  for(int i=2; i*i<n; i++){
    if(n%i==0) return false;
  }
  return true;
}
unsigned long long divisor(unsigned long long n){
  for(int i=2; i*i<n; i++){
    if(n%i==0) return i;
  }
  return 0;
}

int main(){
  int kase;
  cin >> kase;
  int k = 0;
  while(k < kase){
    int n, jcnt;
    cin >> n >> jcnt;
    cout<<"Case #"<<(k+1)<<":"<<endl;
    int j = 0;
    vector<bool> bits(n, false);
    bits[0] = bits[n-1] = true;
    while(j < jcnt){
      bool fake = false;
      vector<unsigned long long> divs(11, 0);
      for(int p = 2; !fake && p <= 10; p++){
        unsigned long long num = 0;
        for(int i = 0; i < n; i++){
          num *= p;
          num += (bits[i]);
        }
        divs[p] = divisor(num);
        if(divs[p]==0) fake = true;
      }
      if(!fake){
        for(bool b:bits) cout<<(b?1:0);
        for(int p = 2; p <= 10; p++){
          cout<<' '<<divs[p];
        }
        cout<<endl;
        j++;
      }
      //inc bits
      int pos = n-2;
      while(bits[pos]){
        bits[pos] = false;
        pos--;
      }
      bits[pos] = true;
    }
    k++;
  }
  return 0;
}
