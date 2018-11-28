#include<iostream>
#include<fstream>
#include<string.h>

using namespace std;

ifstream fin;
ofstream fout;

int main()
{
  int i,j,T,c;
  char S[100];
  
  fin.open("input.in");
  fout.open("output-fin.txt");
  
  fin>>T;
  
  for(i=0;i<T;i++)
    {
      fin>>S;
      c=0;

      if(S[strlen(S)-1]=='-')
	{c++;}
      
      for(j=1;j<strlen(S);j++)
	{
	  if(S[j]!=S[j-1])
	    {c++;}
	}
      
      fout<<"Case #"<<i+1<<": "<<c<<"\n";
    }
  
  return 0;
}
