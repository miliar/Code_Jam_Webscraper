// A_Tic-Tac-Toe-Tomek.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "iostream"
#include "fstream"
using namespace std;

int main()
{
	ifstream fin("A-small-attempt0.in");
	ofstream fout("A-small.out");
	int t;
	fin>>t;
	for(int n=0;n<t;n++)
	{
		char arr[4][4];
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				fin>>arr[i][j];
			}
		}
		int count=0;
		bool end=false;
		//------------------------------------------------------------------------------------------
		for(int i=0;i<3 && !end;i++)
		{
			for(int j=0;j<3;j++)
			{
				if((arr[i][j]==arr[i][j+1] && arr[i][j]!='.')|| arr[i][j]=='T' || arr[i][j+1]=='T' )
				{
					count++;
				}
			}
			if(count==3)
			{
				if(arr[i][0]!='T')
					fout<<"Case #"<<n+1<<": "<<arr[i][0]<<" won"<<endl;
				else
					fout<<"Case #"<<n+1<<": "<<arr[i][1]<<" won"<<endl;

				end=true;
				count=0;
			}
			else
			{
				count=0;
			}
		}
		//------------------------------------------------------------------------------------------
		for(int j=0;j<3 && !end;j++)
		{
			for(int i=0;i<3;i++)
			{
				if((arr[i][j]==arr[i+1][j] && arr[i][j]!='.' )|| arr[i][j]=='T' || arr[i+1][j]=='T')
				{
					count++;
				}
			}
			if(count==3)
			{
				if(arr[0][j]!='T')
					fout<<"Case #"<<n+1<<": "<<arr[0][j]<<" won"<<endl;
				else 
					fout<<"Case #"<<n+1<<": "<<arr[1][j]<<" won"<<endl;

				end=true;
				count=0;
			}
			else
			{
				count=0;
			}
		}
		//------------------------------------------------------------------------------------------
		for(int i=0,j=0;i<3 && !end;i++,j++)
		{
			if((arr[i][j]==arr[i+1][j+1] && arr[i][j]!='.' )|| arr[i][j]=='T' || arr[i+1][j+1]=='T')
				{
					count++;
				}
		}
		if(count==3)
			{
				if(arr[0][0]!='T')
					fout<<"Case #"<<n+1<<": "<<arr[0][0]<<" won"<<endl;
				else 
					fout<<"Case #"<<n+1<<": "<<arr[1][1]<<" won"<<endl;
				end=true;
				count=0;
			}
			else
			{
				count=0;
			}
		//-------------------------------------------------------------------------------------------
		for(int i=3,j=0;j<3 && !end;i--,j++)
		{
			if((arr[i][j]==arr[i-1][j+1] && arr[i][j]!='.' )|| arr[i][j]=='T' || arr[i-1][j+1]=='T')
				{
					count++;
				}
		}
		if(count==3)
			{
				if(arr[3][0]!='T')
					fout<<"Case #"<<n+1<<": "<<arr[3][0]<<" won"<<endl;
				else 
					fout<<"Case #"<<n+1<<": "<<arr[2][1]<<" won"<<endl;

				end=true;
				count=0;
			}
			else
			{
				count=0;
			}
		//-------------------------------------------------------------------------------------------
		if(!end)
		{
			bool b=false;
			for(int i=0;i<4;i++)
			{
				for(int j=0;j<4;j++)
				{
					if(arr[i][j]=='.')
					{
						b=true;
					}
				}
			} 
			if(b)
				fout<<"Case #"<<n+1<<": "<<"Game has not completed"<<endl;
			else 
				fout<<"Case #"<<n+1<<": "<<"Draw"<<endl;

			b=false;
			end=true;
		}

		//-------------------------------------------------------------------------------------------
	}
	return 0;
}

