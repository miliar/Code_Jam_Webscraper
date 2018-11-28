#include <iostream>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <fstream>
#include <map>
#include <cstring>
using namespace std;
int a[10];

int sum() {
  int sum = 0;
  for(int l = 0; l<10; l++) {
    sum = sum + a[l];
  }
  return sum;
}

int main() {
  ofstream output;
  output.open("output.txt");
  int t;
  cin >> t;
  long long int n;
  for(int i=1;i<=t;i++) {
    cin >> n;
    for(int j=0;j<10;j++) a[j] = 0;
    if(n==0) {
      output << "Case #" << i << ": INSOMNIA"<<endl;
    }
    else {
      long long int inc = 1,k,num = n;
      while(sum()!=10) {
	while(num!=0){
	  k = num%10;
	  num = num/10;	
	  a[k] = 1;
	}
	inc = inc + 1;
	num = n*inc;
      }
      output << "Case #" << i << ": "<<n*(inc-1)<<endl;
    }
  }
  return 0;
}
