#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <set>
using namespace std;

set<long long int> s;

//finding digits of a number and inserting the digits in a set
void abc(long long int n){
  long long int digit;
  while (n!=0){
    digit=n%10;
    n=n/10;
    s.insert(digit);
  }
}

//finding multiples of a number and checking the size of the set
long long int check_multiples(long long int num){
  int i=1;
  while (s.size()!=10){
    abc(num*i);
    i++;
  }
  return num*(i-1);
}


int main() {
    int T;
    long long int num;
    cin>>T;
    int i=1;
    while(i<=T){
      cin>>num;
      if(num==0)
        cout<<"Case #"<<i<<": INSOMNIA"<<endl;
      else
        cout<<"Case #"<<i<<": "<<check_multiples(num)<<endl;
      i++;
      s.clear();
    }
    return 0;
}
