#include<iostream>
#include<bits/stdc++.h>
#define ll long long int
using namespace std;

int main(){
 ll t;
 cin>>t;
 ll rank;
 rank=0;
 while(t--){
  rank++;
   string s, str;
   cin>>s;
   ll len = s.length();
   ll a[26];
   for(ll i=0;i<26;i++){
      a[i]=0; 
   }

   for(ll i=0;i<s.length();i++){
      a[s[i]-'A']++;
   }
   str = s[0];
   string temp;
   for(ll i=1;i<s.length();i++){
       ll k=0;
       
       if(s[i]<str[0])
       {
          str +=s[i]; 
       }else{
         temp=s[i];
         temp+=str;
         str=temp;
       }
   }
   cout<<"Case #"<<rank<<": "<<str<<endl;
 
 }
 return 0;
}
