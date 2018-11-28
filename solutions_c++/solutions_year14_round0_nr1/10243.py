#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    int T,i=0;
    ifstream fin;
    ofstream fout;
    fout.open("result.txt");
    fin.open("input.txt");
    fin>>T;
    while(i<T)
    {
              int f1,f2,c=0,index,temp;
              int a[4],b[4];
              fin>>f1;
              int loop=1;
              while(loop<=4)
              {
                          if(loop==f1)
                          {
                                      for(int l2=0;l2<4;l2++)
                                      {
                                              fin>>a[l2];
                                              //fout<<a[l2]<<"\t";
                                      }
                          }
                          else
                          {
                                      for(int l2=0;l2<4;l2++)
                                      {
                                              fin>>temp;
                                      }
                          }
                          ++loop;
              }
              loop=1;
              fin>>f2;
              while(loop<=4)
              {
                          if(loop==f2)
                          {
                                      for(int l2=0;l2<4;l2++)
                                      {
                                              fin>>b[l2];
                                             // fout<<b[l2]<<"\t";
                                      }
                          }
                          else
                          {
                                      for(int l2=0;l2<4;l2++)
                                      {
                                              fin>>temp;
                                      }
                          }
                          ++loop;
              }
              for(int m=0;m<4;m++)
              {
                      for(int n=0;n<4;n++)
                      {
                              if(a[n]==b[m])
                              {
                                            ++c;
                                            index=n;
                              }
                      }
              }
              if(c==1)
              {
                      fout<<"Case #"<<i+1<<": "<<a[index]<<endl;
              }
              else if(c==0)
              {
                      fout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
              }
              else
              {
                  fout<<"Case #"<<i+1<<": Bad magician!"<<endl;
              }
              c=0;
              ++i;
    }
    fin.close();
    fout.close();
    return(0);
}
