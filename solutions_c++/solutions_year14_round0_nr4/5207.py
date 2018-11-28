#include <stdio.h>
#include <iostream>
#include <stdlib.h>

#include <algorithm> 
#include <functional>  
#include<vector>

using namespace std;

void print(vector<double>  v){
   for(int i=0; i< v.size(); i++){
    cout << v[i]  << " "; 
   }
  cout << endl;
}



int main(){

int Ncases, Nwoods, score;

cin >> Ncases;

for(int i=0; i<Ncases; i++){
   cin >> Nwoods;
  
  score = 0;

  vector<double> her(Nwoods);
  vector<double> his(Nwoods);

  for(int j=0; j<Nwoods; j++){
     
     cin>> her[j];
    
  }
   sort(her.begin(), her.end(), std::greater<double>() );
  for(int j=0; j<Nwoods; j++){
  
    cin>> his[j];
   
   
  }
  
   sort(his.begin(), his.end());

//print(her);
//print(his);

   int top=Nwoods-1;
   int low=0; 
   score=0;

  //cheat case
    for(int j=Nwoods-1; j>=0; j--){
     if(her[j]>his[low]){
       score++; 
       low++;
     }
     else{
       top--;
     }
   }
 
  cout << "Case #" << (i+1) << ": " << score;

 // normal case
  
 top=Nwoods-1;
  low=0; 
   score=0;
 
 for(int j=0; j<Nwoods; j++){
     if(her[j]>his[top]){
       score++; 
       low++;
     }
     else{
         
       top--;
     }
 }
   cout << " " << score << endl;
}
}
