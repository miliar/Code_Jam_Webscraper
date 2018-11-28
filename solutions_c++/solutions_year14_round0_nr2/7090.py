#include<stdio.h>
#include<conio.h>
#include<iostream>
#include<cstdlib>
#include<iomanip>
#include<fstream>
using namespace std;
main()
{
      ifstream fin("B-large.in");
      ofstream fout("fwfwfw22.out");
      int T,i=0;
      double C=0,F=0,X=0,r=2,t=0,tot[1000],total=0;
      fin>>T;
      if(T>=1&&T<=100)
      {
                      for(int tc=0;tc<T;tc++)
                      { 
                                         fout<<fixed;
                                         fout<<setprecision(7);       
                                         fin>>C;
                                         fin>>F;
                                         fin>>X;
                                         t=0;i=0;total=0;r=2;
                                         if(C>=1&&C<=10000&&F>=1&&F<=100&&X>=1&&X<=100000)
                                         {
                                         fout<<"Case #"<<tc+1<<": ";
                                         while(total+(X/r)>total+(C/r)+(X/(r+F)))
                                         {
                                                 t=C/r;
                                                 r=r+F;
                                                 total=total+t;  
                                         }
                                         pr:
                                                 
                                                 fout<<total+(X/r)<<endl;
                                         }
                                         }
      }
      fout.close();
      }
