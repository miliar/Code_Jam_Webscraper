#include<iostream>
#include<fstream>

using namespace std;

int main()
{
    ifstream alpha("B-large.in");
    ofstream beta("output.txt");
    int i,j,k,l,m,s;
    int N;
    alpha>>N;
    int x[N];
    int y[N];
    int a[100][100];
    
    for(k=0;k<N;k++)
    {
                    alpha>>x[k]>>y[k];
                    for(i=0;i<x[k];i++)
                    for(j=0;j<y[k];j++)
                    alpha>>a[i][j];
                    
                    
                    for(i=0;i<x[k];i++)
                    {for(j=0;j<y[k];j++)
                    {
                                       s=0;
                                       for(l=0;l<x[k];l++)
                                       if(a[i][j]<a[l][j])
                                       {
                                                          s++;
                                                          break;
                                                          }
                                       for(m=0;m<y[k];m++)
                                       if(a[i][j]<a[i][m])
                                       {
                                                          s++;
                                                          break;
                                                          }
                                       if(s==2)
                                       break;
                                       }
                    if(s==2)
                    break;
                    }
                    switch(s)
                    {
                             case 0:
                                  beta<<"Case #"<<k+1<<": YES"<<endl;
                                  break;
                             case 1:
                                  beta<<"Case #"<<k+1<<": YES"<<endl;
                                  break;
                             case 2:
                                  beta<<"Case #"<<k+1<<": NO"<<endl;
                             }
                    }
                    
    return 0;
    }
