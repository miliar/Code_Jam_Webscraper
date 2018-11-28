#include<stdio.h>
#include<stdlib.h>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <map>
#include <string>
#include <fstream>
using namespace std;

int main(){
  long T;
  cin >> T;
  for(long t=1;t<=T;++t){
      cout << "Case #"<<t<<": ";
      long long t,r;
      cin >> r;
      cin >> t;
      long long sum=0;
      long long it=-1;
      do{
        ++it;
        sum+=2*r+1+4*(it);
      }while(sum<=t);
      cout << it<<endl;
  }
  return 0;
}
