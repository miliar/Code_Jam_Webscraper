#include<iostream>
#include<fstream>
#include<cstdio>
#define SIZE 10
#define l_int long int
using namespace std;
int temp[SIZE];
int garden_in[SIZE][SIZE];
int garden_temp[SIZE][SIZE];
int T,N,M;

bool checkRow(int i)
{
	for(int j=0;j<M;j++)
		if(garden_in[i][j]!=1)
			return false;

	return true;
}
bool checkCol(int j)
{
	for(int i=0;i<N;i++)
		if(garden_in[i][j]!=1)
			return false;

	return true;
}
int main()
{
	
	ifstream infile;
	ofstream outfile;
  	infile.open("B-small-attempt3.in");
  	outfile.open("b-output.out");
  	if (infile.is_open())
	{
	  	
	  		infile>>T;
	  		int k=1;
	  		while(T--)
	  		{
	  			infile>>N;
	  			infile>>M;
	  			for(int i=0;i<N;i++)
	  			{
	  				for(int j=0;j<M;j++)
	  				{
	  					infile>>garden_in[i][j];
	  					garden_temp[i][j]=2;
	  				}
	  			}

	  			/*  traversing */
	  			for(int j=0;j<M;j++)
	  			{
  					if(checkCol(j))
  					{
  						for(int i=0;i<N;i++)
  						{
  							garden_temp[i][j]=garden_in[i][j];
  						}
  					}
	  				
	  			}
	  			for(int i=0;i<N;i++)
	  			{
	  				if(checkRow(i))
	  				{
	  					for(int j=0;j<M;j++)
	  					{
	  						garden_temp[i][j]=garden_in[i][j];
	  					}
	  				}		
	  				
	  			}

	  			/*  matching */
	  			int flag=0;
	  			for(int i=0;i<N;i++)
	  			{
	  				for(int j=0;j<M;j++)
	  				{
	  					if( garden_in[i][j]!=garden_temp[i][j] )
	  					{
	  						flag=1;
	  						break;
	  					}
	  				}

	  				if(flag==1)
	  					break;
	  			}

	  			if(flag==0)
	  				outfile<<"Case #"<<k++<<": YES"<<endl;
	  			else
	  				outfile<<"Case #"<<k++<<": NO"<<endl;
	  			
	  		}
	}	
	infile.close();
	outfile.close();
  return 0;
}
