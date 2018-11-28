#include <bits/stdc++.h>
#include <string>
#define ull unsigned long long int
using namespace std;

long int divisors[11];

bool isnotprime(ull val) {
  for(int i=2; i<=sqrt(val); i++) {
    if(val%i == 0) return true;
  }
  return false;
}

long finddiv(ull v) {
  if(v%2 == 0) return 2;
  else {
  for(int i=3; i<=sqrt(v); i+=2) {
    if(v%i == 0) {
      return i;
    }
  }
  }
}

long long int binary(int num)

{
    int rem;
    if (num <= 1) {
      return num;
    }

    rem = num % 2;
    return binary(num/2)*10 + rem;

}

 int main() {
  int t;
  cin>>t;
  int j, n;
  cin>>n>>j;
  int x=1;
  int jamcount=0;
  string jamstring;
  bool flag;
  cout<<"Case #"<<t<<":"<<endl;
  for(int num=32769; num <= 65535; num+=2) {
    if(jamcount < j) {
      long long int jam = binary(num);
      ostringstream convert;
      convert << jam;
      jamstring = convert.str();
      for(int i=2; i<=10; i++) {
       ull base_rep = stoull(jamstring, 0, i);
        if(isnotprime(base_rep)) {
          long d = finddiv(base_rep);
          divisors[i] = d; flag = false;
        }
        else {
          flag = true; break;
        }
      }
      if(flag == true) continue;
      cout<<jam<<" "<<divisors[2]<<" "<<divisors[3]<<" "<<divisors[4]<<" "<<divisors[5]<<" "<<divisors[6]<<" "<<divisors[7]<<" "<<divisors[8]<<" "<<divisors[9]<<" "<<divisors[10]<<endl;
      jamcount++;
    }
  }


   return 0;
 }
