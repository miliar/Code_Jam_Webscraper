#include<iostream>
#include<cstring>
#include<cstdio>
#include<vector>
#include<fstream>
using namespace std;
main()
{
      ifstream in;
      ofstream out;
      in.open("input.txt");
      out.open("output.txt");
      int t,n,m,flag;
      in>>t;
      for(int i=0;i<t;i++)
      {
              flag=0;
              in>>n>>m;
              int mat[n][m],col[m],row[n];
              for(int j=0;j<n;j++)
              {
                      row[j]=0;
                      for(int k=0;k<m;k++)
                      {
                              in>>mat[j][k];
                              if(mat[j][k]>row[j])
                              row[j]=mat[j][k];
                              if(j==0)
                              col[k]=mat[j][k];
                              else if(mat[j][k]>col[k])
                              col[k]=mat[j][k];
                      }
              }
              for(int j=0;j<n;j++)
              {
                      for(int k=0;k<m;k++)
                      {
                              if(mat[j][k]==row[j] || mat[j][k]== col[k])
                              {}
                              else
                              {flag=1;break;}
                      }
                      if(flag==1)
                      break;
              }
              if(flag==0)
              out<<"Case #"<<i+1<<": YES\n";
              else
              out<<"Case #"<<i+1<<": NO\n";
              
      }



system("pause");
          
      }
