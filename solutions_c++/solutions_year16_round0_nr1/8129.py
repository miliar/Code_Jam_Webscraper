#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

void process(long long int cur,long long int array[10]) {
  int t;
  while(cur) {
    t = cur % 10;
    cur /= 10;
    array[t] = 1;
  }
}

int check(long long int array[10]) {
  int flag = 1;
  for(int i = 0;i<10;i++)
    if(array[i]!=1)
      flag = 0;
  return flag;
}

long long int prob(long long int N,long long int array[10]) {
  int flag = 0;
  long long int i = 1,cur;
  while(!flag) {
    cur = i * N;
    process(cur,array);
    flag = check(array);
    i++;
    if(flag)
      return cur;
    if(i>=9999999999)
      return -1;
  }
}

int main() {
  int T,iter;
  cin>>T;
  iter = 1;
  while(T--) {
    long long int N,array[10],result;
    for(int i = 0;i<10;i++)
      array[i]=0;
    cin>>N;
    if(N==0) {
      cout<<"Case #"<<iter<<": INSOMNIA"<<endl;
      iter++;
      continue;
    }
    else
      result = prob(N,array);
    cout<<"Case #"<<iter<<": "<<result;
    cout<<endl;
    iter++;
  }
}
