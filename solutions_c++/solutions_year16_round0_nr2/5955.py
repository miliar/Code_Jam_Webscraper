#include<iostream>
#include<bits/stdc++.h>

#define ll long long int

using namespace std;

int main(){
 ll t;
 cin>>t;
  ll caseNumber =0;
  while(t--){
   caseNumber++;
   string s;
   cin>>s;
   ll len,result;
   len = s.length();
   result =0;
   char ch = s[0];
   char plus='+', minus='-',first=s[0],last=s[len-1];
   char symbol;
    symbol = ch;
   ll change = 0;
   for(ll i =1;i<len;i++){
     if(s[i]!=symbol){
      change++;
             if(symbol=='+'){
                symbol = '-';
             }else{
                symbol = '+';
             }
    }
   }
   if(change!=0){
    
     result = change+1;
    if(last=='+'){
     result--; 
   } 

   }else{
      if(ch =='-'){
       result = 1;
      }else{ 
       result =0;
      }
   }
  cout<<"Case #"<<caseNumber<<": "<<result<<endl;
   
  }
 return 0;
}
