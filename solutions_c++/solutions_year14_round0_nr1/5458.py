#include<iostream>
using namespace std;
#include<conio.h>
#include <fstream>

int main()
{    
    ofstream output;
    ifstream input;
    input.open ("A-small-attempt1.in");
   
    
    int t,l[100],temp[100];
	input>>t;
	for(int a=0;a<t;a++)
	{ l[a]=0;
	  int r1,r2;
	  int c1[4][4];
	  int c2[4][4];
	  
	  input>>r1;
	  for(int i =0;i<4;i++)
	  {input>>c1[i][0]>>c1[i][1]>>c1[i][2]>>c1[i][3];
	  }

	  input>>r2;
	  for(int i =0;i<4;i++)
	  {input>>c2[i][0]>>c2[i][1]>>c2[i][2]>>c2[i][3];
	  }
	  for(int i=0;i<4;i++)
	  {
	  	for(int j=0;j<4;j++)
	  	 {
	  		if(c1[r1-1][i]==c2[r2-1][j])
	  		{
	  		  l[a]++;
	          temp[a] = c1[r1-1][i];
	        }
	  	 }
	  }

	}
	output.open ("output.txt");
	for(int a=0;a<t;a++)
	  {
	   output<<"Case #"<<a+1<<":";
	   if(l[a]==0)
	   output<<" Volunteer cheated!\n";
	   else if(l[a]==1)
	   output<<" "<<temp[a]<<endl;
	   else
	   output<<" Bad magician!\n";
      }
      output.close();
      return 0;
}
