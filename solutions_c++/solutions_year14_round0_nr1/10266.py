#include<iostream>
#include <fstream>
#include <string>
#include<stdlib.h>
#include<conio.h>
using namespace std;
int a[4][4];


int main()
{
	int t,r1,r2,i,j,k,count=0,found;
	
	string line;
	int inp;
  ifstream myfile ("A-small-attempt1.in");
  ofstream ofile ("magic.out");
  
    
    
  
  
  if (myfile.is_open() || ofile.is_open())
  {
    
    myfile>>inp;
 
      t=inp;
    
    
  
	int c[4];
	for(k=1;k<=t;k++)
	{		myfile>>inp;
			r1=inp;
			
					for( i=0;i<4;i++)
			{
				for( j=0;j<4;j++)
				{
					myfile>>inp;
					a[i][j]=inp;
					
				}
			
			}
			
			for( i=0;i<4;i++)
			{
				c[i]=a[r1-1][i];
			}
			
			
			myfile>>inp;
			r2=inp;
			
			for( i=0;i<4;i++)
			{
				for( j=0;j<4;j++)
				{
					myfile>>inp;
					a[i][j]=inp;
				
				}
				
			}
			
			
			for(i=0;i<4;i++)
			{
				for(j=0;j<4;j++)
				{
					if(a[r2-1][j]==c[i])
					{count++;
						found=c[i];
						
					}
				}
				
			}
			if(count==1)
			{
				ofile <<"Case #"<<k<<": "<<found;
			}
			else if(count>1)
			{ofile <<"Case #"<<k<<": "<<"Bad magician!";
				
			}
			else
			{
				ofile <<"Case #"<<k<<": "<<"Volunteer cheated!";
				
			}
			
	ofile<<endl;		
			count=0;
}
myfile.close();
ofile.close();
  }

	return 0;
}
