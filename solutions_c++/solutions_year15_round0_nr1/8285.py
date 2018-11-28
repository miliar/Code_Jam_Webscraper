#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <stdio.h>
using namespace std;
int main(){
  ifstream in("test.txt");
  ofstream out("testOut.txt");
  int cases,len,num;
  string c;
  in>>cases;
  for(int i=1;i<=cases;i++){
    in>>len;
    in>>c;
    int standing=c[0]-'0',total=0;
    for(int j=1;j<=len;j++){
      num= c[j] - '0';
      if(num==0){
        continue;
      }
      if(j>standing){
        total+=j-standing;
        standing=j;
      } 
      standing+=num;
    }
    //printf("Case #%d: %d\n",i,total);
    out << "Case #" << i << ": " << total << '\n';
  }
}