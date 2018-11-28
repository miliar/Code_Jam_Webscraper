#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ifstream fin;
    ofstream fout;
    fin.open("B-large.in");
    fout.open("outputl.txt");
    int t;
    int M,N;
    fin>>t;
    int arr[100][100];
    int case_no=1;
    while(t--)
    {
       fin>>N>>M;
       int max_row[100]={0};
       int max_col[100]={0};
       for(int i=0;i<N;i++)
       {
          for(int j=0;j<M;j++)
          {
              fin>>arr[i][j];
                if(max_col[j]<arr[i][j])max_col[j]=arr[i][j];
                if(max_row[i]<arr[i][j])max_row[i]=arr[i][j];
          }        
       }              
        bool flag=true;
         for(int i=0;i<N;i++)
       {
          for(int j=0;j<M;j++)
          {
              
                if((min(max_col[j],max_row[i]))!=arr[i][j])
                {
                 flag=false;
                 break;
                }
                
          }        
          if(!flag)break;
       }     
       fout<<"Case #"<<case_no++<<": ";
      if(flag)fout<<"YES"<<endl;
      else fout<<"NO"<<endl;
    }    

     fin.close();
     fout.close();
        
}
