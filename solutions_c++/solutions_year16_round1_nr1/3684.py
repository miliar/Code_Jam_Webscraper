#include<bits/stdc++.h>
using namespace std;

int main(){


string s1,s2;
long long int t,x,i;


 cin>>t;x=1;
 while(x<=t){
 cin>>s1;s2=s1.substr(0,1);
 for(i=1;i<s1.length();i++){
    if(s1[i]>=s2[0])s2=s1[i]+s2;
    else s2=s2+s1[i];
    //cout<<s2<<endl;
 }
 cout<<"Case #"<<x<<": "<<s2.substr(0,s2.length())<<endl;
  x++;

 }


}

