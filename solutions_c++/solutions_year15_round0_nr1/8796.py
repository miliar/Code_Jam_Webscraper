#include<stdio.h>
#include<conio.h>
#include<iostream>
#include<cstdlib>
#include<fstream>
using namespace std;
main()
{
      ifstream myfile("A-large.in");
      ofstream myfileo;
      myfileo.open("out6.in");
      int T=0,audcount=0,invite=0,temp=0;
      string input="\0";
      myfile>>T;
      if(T>=1&&T<=100)
      {
                      for(int TC=0;TC<T;TC++)
                      {
                              myfileo<<"Case #"<<TC+1<<": ";
                              int smax=0;
                              myfile>>smax;
                              if(smax>=0 && smax<=1000)
                              {
                                         myfile>>input;
                                         int audience[smax+1];
                                         for(int i=0;i<smax+1;i++)
                                         {
                                                 if(input[i]>=48 && input[i]<=57)
                                                 audience[i]=input[i]-48;
                                                 if(audience[i]>0)
                                                 {
                                                                  audcount+=audience[i];
                                                                  }
                                                                  if(audcount<=i+1)
                                                                  {
                                                                                temp=(i+1)-audcount;
                                                                                invite=invite + temp;
                                                                                audcount+=temp;
                                                                  }
                                         }
                              }
                      myfileo<<invite<<endl;
                      invite=0;
                      audcount=0;
                      }
      }
      myfileo.close();
}
