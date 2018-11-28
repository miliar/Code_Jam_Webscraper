// example program
#include <iostream>

#include <stdio.h>
#include <string>

using namespace std;

int main()
{
	freopen ("output.txt","w",stdout);
	freopen("input.txt","r",stdin);

  string s;
 int numberoftest,allattendes,numofinvited,stringcount;
   cin>>numberoftest;
 //  cout<<"sdjkfhjsdhfjk";
  for(int i=0;i<numberoftest;i++){
      numofinvited=0;
      allattendes=0;
      cin>>stringcount>>s;
      
      for(int j=0;j<stringcount+1;j++){
         if(s[j]=='0'){
             continue;
		 }
	     if(j>allattendes){
			 int newinvited=j-allattendes;
	         numofinvited+=newinvited;
             allattendes+=newinvited;
             
         }
         char currentchar=s[j];
         int number = (currentchar - '0')%48;
         allattendes +=number;
	
      }
      
      cout<<"case #"<<i+1<<": "<<numofinvited;
      if(i+1!=numberoftest)cout<<endl;
  } 
  return 0;
}
