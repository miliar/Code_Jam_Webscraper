#include <iostream>
using namespace std;
#include <fstream>
using std::ifstream;
using std::ofstream;

int main()
{
    ifstream indata;
    indata.open("B-small-attempt0.in");
    ofstream outdata;
    outdata.open("B-small-attempt0.txt");
	int t;
    indata>>t;
	for(int i=1; i<=t; i++)
	{
     string o = "YES";
     int n, m;
     indata>>n>>m;
     int lawn[n][m];
     int mr[n], Mr[n];
     for(int i=0; i<n; i++)
     {
      mr[i]=2;
      Mr[i]=1;
      for(int j=0; j<m; j++)
      {
       indata>>lawn[i][j];
       if(mr[i]>lawn[i][j])
        mr[i]=lawn[i][j];
       if(Mr[i]<lawn[i][j])
        Mr[i]=lawn[i][j];
      }
     }
     for(int i=0; i<n; i++)
     {        
      if(mr[i]!=Mr[i])
      {
       for(int j=0; j<m; j++)
       {
        if(mr[i]==lawn[i][j])
        {
         for(int k=0; k<n; k++)
         {
          if(mr[i]<lawn[k][j])
          {
           i=n; j=m; k=n;
           o="NO";
          }
         }
        }
       }
      }
     }
     outdata<<"Case #"<<i<<": "<<o<<"\n";
    }
    indata.close();
    outdata.close(); 
}
