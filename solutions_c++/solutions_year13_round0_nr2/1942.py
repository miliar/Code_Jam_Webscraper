#include <iostream>
using namespace std;

int main()
{
   int t;
  cin>>t;
  int c=1;
  while(t-->0)
  {
    int n,m;
    cin>>n>>m;
    int a[n][m];
    int tag=1;
    int found=0;
    for(int i=0;i<n;i++)
    for(int j=0;j<m;j++)
    {cin>>a[i][j];
    if(a[i][j]==1)found=1;}
      
      for(int k=0;k<n;k++)
     for(int l=0;l<m;l++)
    {
    int max;
        int maxr=a[k][l];
        int maxc=a[k][l];
     for(int k1=0;k1<m;k1++)
     {
     if(a[k][k1]>maxr)
       maxr=a[k][k1];
     }
     for(int l1=0;l1<n;l1++)
     {
     if(a[l1][1]>maxc)
       maxc=a[l1][l];
     }
        if(maxr<maxc)
          max=maxr;
        else
          max=maxc;
     
     if(a[k][l]!=max)
     { cout<<"Case #"<<c<<": NO"<<endl;
     goto label;
     }
    
    }
    
    
    
    
      
   
    cout<<"Case #"<<c<<": YES"<<endl;
    
    
    
   
    
  
  label:
 
  c++;
  }
   return 0;
}
   