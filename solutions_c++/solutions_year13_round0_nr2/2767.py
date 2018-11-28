#include<iostream>
#include<map>
#include<fstream>
#include<algorithm>
using namespace std;
int main()
{
	int a[100][100],i,j,t,k,n,m,flag,rowok,max,col,row,smax[100],stemp;

	map<int,int>mp;
	ifstream fin("C:/a.txt");
	ofstream fout("C:/o.txt");

	fin>>t;
	for(k=0;k<t;k++)
	{
		fin>>n>>m;
		for(i=0;i<n;i++)
		{
		  row=0;
			for(j=0;j<m;j++)
		 {
			 fin>>a[i][j];
			 if(row<a[i][j])
				 row=a[i][j];
		 }
			smax[i]=row;
		}

		flag=0;
		mp.clear();
		for(i=0;i<n;i++)
		{
			flag=1;
			rowok=1;
			stemp=smax[i];
			
			for(j=0;j<m;j++)
			{
				
				if(stemp!=a[i][j])
				{
					col=j;
					
					flag=0;
					rowok=1;
					if(mp.find(col)==mp.end())
					{
						mp[col]=1;
					  for(row=0;row<(n-1);row++)
						{
							if(a[row][col]!=a[row+1][col])
							{
								rowok=0;
								break;
							}
						}
					}
					flag=rowok;
					if(flag==0)
						break;

				}
				
			}
			if(flag==0)
			  break;
		}
		
		/*for(i=0;i<n;i++)
		{
			
			for(j=0;j<m;j++)
				fout<<a[i][j]<<" ";
			fout<<endl;
		}*/

		if(flag==0)
				fout<<"Case #"<<(k+1)<<": NO"<<endl;
			else
				fout<<"Case #"<<(k+1)<<": YES"<<endl;

	}
	return 0;
}