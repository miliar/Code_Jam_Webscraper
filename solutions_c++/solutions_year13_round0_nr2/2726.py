#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    ifstream fin;
    fin.open("input.txt");
    ofstream fout;
    fout.open("output.txt");
    int t,l=0;
    fin>>t;
    while(t--)
    {
              l++;
               
              int n,m,flag=0;
              fin>>n>>m;
              int arr[n][m],temp[n][m];
              for(int i=0;i<n;i++)
                      for(int j=0;j<m;j++)
                      {
                              fin>>arr[i][j];
                              temp[i][j]=arr[i][j];
                      }
              for(int i=0;i<n;i++)
              {
                      
                      int p=temp[i][0];
                      for(int j=1;j<m;j++)
                              p=max(p,temp[i][j]);
                      for(int j=0;j<m;j++)
                              temp[i][j]=p;
              }
              for(int j=0;j<m;j++)
              {
                      int f=0,p;
                      for(int i=0;i<n;i++)
                      {
                              if(arr[i][j]!=temp[i][j])
                              {
                                  f=1;
                                  p=arr[i][j];
                                  break;                      
                              }
                      }
                      if(f==1)
                      {
                              //cout<<l<<" "<<j<<" "<<m<<endl;
                              for(int i=0;i<n;i++)
                                      temp[i][j]=p;
                      }
              }
              for(int i=0;i<n;i++)
                      for(int j=0;j<m;j++)
                      {
                              if(arr[i][j]!=temp[i][j])
                              {
                                        flag=1;
                                        break;
                              }
                      }
              if(flag==1)
                         fout<<"Case #"<<l<<": NO\n";
              else
                         fout<<"Case #"<<l<<": YES\n";
                      
    }
    //system("pause");
    return 0;
}
                                    
              
                      
                      
                      
