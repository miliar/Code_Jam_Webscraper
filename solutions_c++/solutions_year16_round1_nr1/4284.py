#include <iostream>
#include<cstring>
#include<stdio.h>
using namespace std;

int main() {
int test;
string str;
cin>>test;
for(int t=1;t<=test;t++)
{
cin>>str;
int length=str.size();
string output ; 
output =str[0];

for(int i=1;i<length;i++)
{   
   if(str[i] >=output[0])
     output=str[i]+output;
     
      
    
   else
   output=output+str[i];
   
 
   
} 
cout<<"Case #"<<t<<": "<<output<<endl;
  
   


}




	return 0;
}