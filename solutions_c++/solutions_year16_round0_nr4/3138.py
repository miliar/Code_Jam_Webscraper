#include<stdio.h>
#include<fstream>
#include<vector>
#include<algorithm>
#include<map>
#include<string>
#include<iostream>
using namespace std;
int main(){
  ofstream result;
  result.open("fractiles.txt");
  int T,K,C,S,M=0;
  scanf("%d",&T);
  while(T--){
   cin>>K>>C>>S;
   result<<"Case #"<<++M<<": ";
   for(int i=1; i<S;i++){result<<i<<" ";}
   result<<S<<"\n";
  }
}
