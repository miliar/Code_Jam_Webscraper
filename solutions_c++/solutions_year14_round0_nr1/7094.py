#include<stdio.h>
#include<conio.h>
#include<iostream>
#include<cstdlib>
#include<fstream>
using namespace std;
main()
{
      ifstream myfile("A-small-attempt5.in");
      ofstream myfileo;
      myfileo.open("out5.in");
      int T,r1,r2,ar1[4][4],ar2[4][4];
                          myfile>>T;
                          if(T>=1&&T<=100)
                          {
                          for(int tc=0;tc<T;tc++)
                          {
                                  myfileo<<"Case #"<<tc+1<<": ";
                                  int count=0,ind=0;
                                  myfile>>r1;
                                  for(int i=0;i<4;i++)
                                  {
                                          for(int j=0;j<4;j++)
                                          {
                                                  myfile>>ar1[i][j];
                                          }
                                  }
                                  myfile>>r2;
                                  for(int i=0;i<4;i++)
                                  {
                                          for(int j=0;j<4;j++)
                                          {
                                                  myfile>>ar2[i][j];
                                          }
                                  }
                                  for(int i=0;i<4;i++)
                                  {
                                          for(int j=0;j<4;j++)
                                          {
                                          if(ar1[r1-1][i]==ar2[r2-1][j])
                                          {
                                                                    count++;
                                                                    ind=i;
                                          }
                                          }
                                  }
                                  if(count==0)
                                  myfileo<<"Volunteer cheated!"<<endl;
                                  else if(count>1)
                                  myfileo<<"Bad magician!"<<endl;
                                  else if(count==1)
                                  {
                                       myfileo<<ar1[r1-1][ind]<<endl;
                                  }
                          }
                          }
      myfileo.close();
}
