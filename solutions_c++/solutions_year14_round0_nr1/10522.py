
#include<stdio.h>
#include<iostream>
#include<fstream>
using namespace std;

main()
{ ifstream in;
  ofstream  out;
  in.open("1.in",ios::in);
  out.open("2.out",ios::out);
  int t,i,r1,r2,j,k,a[4][4],b[4][4],c=0,d;
  in>>t;
  for(k=1;k<=t;k++)
  {c=0;
    in>>r1;
    for(i=0;i<4;i++)
    for(j=0;j<4;j++)   
    in>>a[i][j];
    in>>r2;
    for(i=0;i<4;i++)
    for(j=0;j<4;j++)   
    in>>b[i][j];
	for(i=0;i<4;i++)
	 {
	   for(j=0;j<4;j++)
	    {
	     if(a[r1-1][i]==b[r2-1][j])
	     {
	      c++;
	     d=a[r1-1][i];}
        }}
	 
	 if(c==0)
	 out<<"Case #"<<k<<": Volunteer cheated!\n";
	 else if(c==1)
	 out<<"Case #"<<k<<": "<<d<<"\n";
	 else if(c>1)
	 out<<"Case #"<<k<<": Bad magician!\n";
  }

	
}
