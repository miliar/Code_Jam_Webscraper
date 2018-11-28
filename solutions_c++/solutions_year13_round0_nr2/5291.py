#include <iostream>
#include <fstream>
using namespace std;
bool check (int *arr1,int s,int p,int w1)
{
	int k;
	for(k=p+1;k<w1;k++)
		{if(arr1[k]>s)
			return false;
	    }	
	for(k=p-1;k>=0;k--)
		{if(arr1[k]>s)
			return false;
	    }
	return true;

}
int main ()
{ 
  ifstream fin ("input.txt");
  ofstream fout ("google1.txt");
  int num,l,w;
  bool bol=true;
  int j,k,h;
  int temp=0;
  int **arr;
  fin>>num;
  for(int i=0;i<num;i++)
  {   bol=true;
	  fin>>l>>w;
	  arr=new int*[l];
	  for(j=0;j<l;j++)
		  arr[j]=new int [w];
	  //enter data
	  for(j=0;j<l;j++)
		  for(k=0;k<w;k++)
			  fin>>arr[j][k];

	  for(j=0;j<w;j++)
	  { temp=0; 
	    for(h=0;h<l;h++)
		{if(arr[h][j]>temp)
		  temp=arr[h][j];
        }
		for(k=0;k<l;k++)
		{ 
			if(arr[k][j]!=temp)
		  {
	         if(!check(arr[k],arr[k][j],j,w))        	  
			 {
				 bol=false;		 
			     break; 
			 }
		  }
		}
		if(bol==false) break;
	  } 
 
	  if(bol==true) fout<<"Case #"<<i+1<<": YES"<<endl;
	  else fout<<"Case #"<<i+1<<": NO"<<endl;
	  
  for(int y=0;y<l;y++)
	{  delete []arr[y];
       arr[y]=NULL;
    }
  delete []arr;
  arr=NULL;
  }

return 0;
}