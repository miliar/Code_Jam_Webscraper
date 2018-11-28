#include<stdio.h>
#include<conio.h>
#include<iostream>
#include<cstdlib>
#include<iomanip>
#include<fstream>
using namespace std;
main()
{
      ifstream myfile("B-large.in");
      ofstream myfileo;
      myfileo.open("outla0.in");
      int T,i=0;
      double C=0,F=0,X=0,r=2,t=0,tot[1000],total=0;
      myfile>>T;
      if(T>=1&&T<=100)
      {
                      for(int tc=0;tc<T;tc++)
                      { 
                                         myfileo<<fixed;
                                         myfileo<<setprecision(7);       
                                         myfile>>C;
                                         myfile>>F;
                                         myfile>>X;
                                         t=0;i=0;total=0;r=2;
                                         if(C>=1&&C<=10000&&F>=1&&F<=100&&X>=1&&X<=100000)
                                         {
                                                                                    myfileo<<"Case #"<<tc+1<<": ";
                                         while(total+(X/r)>total+(C/r)+(X/(r+F)))
                                         {
                                                 t=C/r;
                                                 r=r+F;
                                                 total=total+t;  
                                         }
                                         pr:
                                                 
                                                 myfileo<<total+(X/r)<<endl;
                                         }
                                         }
      }
      myfileo.close();
      }
