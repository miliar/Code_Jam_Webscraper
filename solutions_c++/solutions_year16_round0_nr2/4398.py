#include<iostream>
using namespace std;



int main() {
	 long test;
   long test2;
   long out;
	char  input[101];
	cin>>test;
	test2=test;
   for(int i=1;i<=test;i++)
   {
     	cin>>input;
      out=0;
      for(int j=0;input[j]!='\0';j++)
      {
      	if(input[j]=='-' && input [j+1]=='\0')
          out++;
          else if(input[j]!=input[j+1] && input [j+1]!='\0')
          out++;
      }
      cout<<"Case #"<<i<<": "<<out<<endl;

   }
  
	return 0;
}