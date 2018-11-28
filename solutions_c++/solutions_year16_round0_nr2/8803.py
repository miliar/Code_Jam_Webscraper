#include <iostream>
#include<stdio.h>
#include<cstring>
#include <fstream>

using namespace std;
int main() {
	// your code goes here
	int T,i,j;
	int count=1;
	int flip;
	char a[1000];
	
	ifstream fin ( "B-large.in" );
    ofstream fout ( "B-large.txt" );
	fin>>T;
	while(T>0)
	{
	   flip=0;
	   fin>>a;
	   for(i=0;i<strlen(a);i++)
	   {
	       if(a[i]=='-')
	       {
	          flip+=1;
	          j=i;
	          if(i==0)
	          {
	              while(a[j]=='-'){
	              a[j]='+';
	              j++;
	             }
                  i=j;	             
	              continue;
	          }
	          while(a[j]=='-'){
	              a[j]='+';
	              j++;
	          }
	          flip+=1;
	          i=j;
	       }
	   }
	   fout<<"Case #" << count<< ": "<<flip<<"\n";
	   count++;
	   T--;
	}
	return 0;
}
