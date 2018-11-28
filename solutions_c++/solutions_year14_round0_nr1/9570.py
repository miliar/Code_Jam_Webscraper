/* 
 * File:   main.cpp
 * Author: zviad
 *
 * Created on December 5, 2012, 12:08 AM
 */

#include <cstdlib>
#include <math.h>
#include <iostream>
#include <stdio.h>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <map>
using namespace std;

int a[4][4];
int b[4][4];
int t;
int  magic(){
 freopen("input.txt", "rt", stdin);
  freopen("output.txt", "wt", stdout);
  int t;
  int fc;
  int sc;
  int sum=0;
  int res=0;
  cin>>t;
  for(int i=0;i<t;i++){
      cin>>fc;
      for(int j=0;j<4;j++){
          for(int k=0;k<4;k++){
              cin>>a[j][k];
              
          }
         
      }
      cin>>sc;
      for(int j=0;j<4;j++){
          for(int k=0;k<4;k++){
              cin>>b[j][k];
               
          }
          
      }
      sum=0;
      for(int j=0;j<4;j++){
          for(int k=0;k<4;k++){
                 if(b[sc-1][j]==a[fc-1][k]){
                     sum++;res=a[fc-1][k];break;
                 }
          }
            }
      if(sum==0){
          cout<<"Case #"<<i+1<<": Volunteer cheated!\n";
      }else if(sum==1){
          cout<<"Case #"<<i+1<<": "<<res<<"\n";
      }else{
          cout<<"Case #"<<i+1<<": "<<"Bad magician!\n";
      }
           
  }
}
int main() {    
   int k=magic();
   return 0;
}
