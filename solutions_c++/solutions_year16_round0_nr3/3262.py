#include<stdio.h>
#include<fstream>
#include<vector>
#include<algorithm>
#include<map>
#include<string>
#include<iostream>
#include<bitset>
#include<stdlib.h>
//#include <boost/dynamic_bitset.hpp>
using namespace std;
ofstream result;
int output,N;

long long int stringToNum(string a, int base){
 long long int ans = 0;
 long long int temp=1;
 int len = a.length();
 if(a[len-1]=='1'){ ans = 1;}  
 for (int i=len-2; i>=0; i--){
  temp *= base;
  if(a[i]=='1'){ ans += temp;}
 }
 return ans;
}

bool isPrime(long long int number){
    if(number < 2) return false;
    if(number == 2) return true;
    if(number % 2 == 0) return false;
    for(long long int i=3; (i*i)<=number; i+=2){
        if(number % i == 0 ) return false;
    }
    return true;
}

void check(bitset<16> num){
  string a = num.to_string();
  for(int i=2; i<=10; i++){
   long long int x = stringToNum(a,i);
   if(isPrime(x)){return;}
  }
  output++;
  //result<<"\n"<<a;
  result<<"\n"<<a.substr(16-N,N);
  for(int i=2; i<=10; i++){
   long long int x = stringToNum(a,i);
   long long int temp = 2;
   while(temp<x){
    if(x%temp==0){result<<" "<<temp; break;}
    temp++;
   }
  }
}

void findNonPrime(bitset<16> num, int N, int k){
  if(output>=N){ return;}
  if(k==0){
   check(num);
   return;
  }
  findNonPrime(num,N,k-1);
  findNonPrime(num.set(k),N,k-1);
  return;
}




int main(){
  int T,J,M=0;
  result.open("coinjam.txt");
  scanf("%d",&T);
  while(T--){
   cin>>N>>J;
   bitset<16> num;
   num.set(0); num.set(N-1);
   result<<"Case #"<<++M<<": ";
   output=0;
   findNonPrime(num,J,N-1);
  }
}
