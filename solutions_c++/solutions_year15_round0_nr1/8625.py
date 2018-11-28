
#include<stdio.h>
#include<iostream>
#include<fstream>
using namespace std;

main()
{ ifstream in;
  ofstream  out;
  in.open("1.in",ios::in);
  out.open("2.out",ios::out);
  int T,i,it,sm,npk[1002];
  char nk[1002];
  in>>T;
  for(it=0;it<T;it++)
  {
  	in>>sm;
  	in>>nk;
  
  for(i=0;i<sm+1;i++)
  npk[i]=(int)( nk[i]-'0');
  int nps = 0, npi = 0;
  for(i=0;i<sm+1;i++)
  {
  	 if(nps>=i)
  	 {
  	 	nps+=npk[i];
	 }
	 else
	 {
	 	npi+=(i-nps);
	 	nps+=(npk[i]+i-nps);
	 }
  }
  out<<"Case #"<<it+1<<": "<<npi<<'\n';
  }
}
