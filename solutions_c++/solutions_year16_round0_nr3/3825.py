//God & me
#include <bits/stdc++.h>
#define int long long
using namespace std;
const int maxn=1e6;
int n=16,k=50,cer[17];
int check(int a,int b){
  int x=0,z=1;
  while(a){
    if(a & 1)
      x += z;
    z *= b;
    a>>=1;
  }
  for(int p=2;p * p <= x;p++)
    if(x % p == 0){
      return p;
    }
  return 0;
}
main(){
  //ios::sync_with_stdio(0),cin.tie(0);
  for(int mask=(1 << (n-1) ) + 1;k;mask+=2){
    bool bad=0;
    for(int base=2;base<=10;base++)
      if(! (cer[base] = check(mask,base)) ){
	bad=1;
	break;
      }
    if(!bad){
      k--;
      for(int i=n-1;~i;i--)
	cout<<(mask >> i & 1);
      cout<<' ';
      for(int base=2;base<=10;base++)
	cout<<cer[base]<<' ';
      cout<<endl;
    }
  }
  return 0;
}
