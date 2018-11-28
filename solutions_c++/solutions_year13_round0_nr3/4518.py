#include<iostream>
#include<stdio.h>
#include<string>
#include<vector>
#include<map>
#include<algorithm>
#include<list>
#include <stack>
#include <math.h>
#include <sstream> 
using namespace std;

bool isStrPalindrome(string str){   
   int len = str.length();
   if(len == 1) return true;
   map<string, int>p; 
   int mid = str.length()/2;
   p[str.substr(0,mid)] = 1;
   //cout<<str.substr(0,mid)<<", "<<str.substr(mid,mid)<<endl;
   //str.substr(0,mid)  
   if(len%2){
     p[str.substr(mid+1,mid)] = 1;        
   }else{
     p[str.substr(mid,mid)] = 1;    
   }
   return (p.size() == 1);      
   
}
int main()
{
    int T=0;
    cin>>T;
    for(int z=1;z<=T;z++)
    {
       long double start,end;
       cin>>start>>end;
       long double fairAndSquare = 0;
       long double sqRootOfEnd = floor (sqrt(end));
       long double sqRootOfStart = floor (sqrt(start));
       for(long double i = sqRootOfStart; i<=sqRootOfEnd; i++){
          //is i*i palindrome
          stringstream s1;
          long double sq = (i*i);
          s1 << sq;
          string str = s1.str();
          if(isStrPalindrome(str) && sq >= start){                                   
             stringstream s2;                                   
             s2 << i;
             str = s2.str();;
             if(isStrPalindrome(str)){
               fairAndSquare++;
               //cout<<"sq: "<<sq<<", i: "<<i<<endl;
             }                      
          }
       }
       cout<<"Case #"<<z<<": "<<fairAndSquare<<endl;
    }
    //int k;cin>>k;    
    return 0;
}
