#include <iostream>
#include <string.h>
#include <string>
using namespace std;

int calculate(string str){

 int i,val=0;

 if(str.size()==1){
   if(!str.compare("+"))
     return 0;
   else 
     return 1;
 }

 if(!str.compare(0,2,"+-")){
   val = 2;
 } else if(!str.compare(0,2,"-+")){
   val = 1;
 } else if(!str.compare(0,2,"--")){
   val = 1;
 }

 if(str.size()==2)
   return val;

 for(i=1;i<str.size();++i){
   if((str[i]=='+') && (str[i+1]=='-'))
     val += 2;
 }

 return val;

}


int main(){

 int i,t,val;
 string str;
 
 cin>>t;
 for(i=1;i<=t;++i){
   cin>>str;

   val = calculate(str);

   cout<<"Case #"<<i<<": "<<val<<endl;

 }

 return 0;
}
