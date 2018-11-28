#include <fstream>
#include <math.h>
#include <vector>
using namespace std;
int main()
{
  ifstream fin("B-large.in");
  ofstream fout("B-large.out");
  int n,x,y;
  bool b1,b2,b;
  fin>>n;
  for (int i=0;i<n;i++)
  {
    fin>>x>>y;
    int arr[x][y];
     for (int j=0;j<x;j++)
	for (int k=0;k<y;k++)
	{  
          fin>>arr[j][k];
	}
     b=true;
     for (int j=0;j<x;j++)
	for (int k=0;k<y;k++)
	{  
          b1=b2=true;
          for (int l=0;l<x;l++)
            if (arr[l][k]>arr[j][k])
	      b1=false;
          for (int l=0;l<y;l++)
            if (arr[j][l]>arr[j][k])
	      b2=false;
           if ((b1==false)&&(b2==false))
	     b=false;
	}
        if (b)
          fout<<"Case #"<<i+1<<": YES"<<endl; 
        else
	  fout<<"Case #"<<i+1<<": NO"<<endl; 
  }
  return 0;
}
