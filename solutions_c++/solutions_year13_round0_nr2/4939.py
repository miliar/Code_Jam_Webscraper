#include<iostream>
#include<stdio.h>
#include<fstream>
using namespace std;
int main()
{
	int t;
	ifstream fil;
	fil.open("input.in");
	fil>>t;
	ofstream file;
	file.open("output.txt");
	int k;
	for(k=1;k<=t;k++)
	{
		int n,m;
		fil>>n;
		fil>>m;
		int i,j,l;
		int lawn[n][m],row,col;
		//int min=100;
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
			{
			  fil>>lawn[i][j];
			}
		}
		/*for(i=0;i<n;i++)
		{
			//row[i]=0;
			for(j=0;j<m;j++)
			{
			  cout<<lawn[i][j]<<" ";
			}
			cout<<"\n";
		}
		getchar();*/

		
		int flag=0;
		
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
			{
				row=0;
				col=0;
				for(l=0;l<m;l++)
				{
					if(lawn[i][l]>lawn[i][j])
					{
						row=1;
						break;
					}
				}
				for(l=0;l<n;l++)
				{
					if(lawn[l][j]>lawn[i][j])
					{
						col=1;
						break;
					}
				}	
				if(row==1 && col==1)
				{
				  flag=1;
				  break;
			    }
			} 
			if(flag==1)
			break;	
		}
		if(flag==1)
		file<<"Case #"<<k<<": NO\n";
		else if(flag==0)
		file<<"Case #"<<k<<": YES\n";
	}
	return 0;
}
