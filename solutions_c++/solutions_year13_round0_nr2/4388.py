#include <iostream>
#include <string>
#include <fstream>
using namespace std;
int in[102][102];
int x,y;
bool judge()
{
	int Vy,Hy;
	int i,j;
	bool yes=true;
	for(Vy=0;Vy<x;Vy++)
	{
		for(Hy=0;Hy<y;Hy++)
		{
			for(i=0;i<x;i++)
			{
				if(in[Vy][Hy]>in[i][Hy])
				{
					for(j=0;j<y;j++)
					{
						if(in[i][Hy] < in[i][j])
						{
							yes=false;
							break;
						}
						
					}
					if(yes==false)break;
				}
			}
			if(yes==false)break;
		}
		if(yes==false)break;
	}



	for(Vy=0;Vy<x;Vy++)
	{
		for(Hy=0;Hy<y;Hy++)
		{
			for(i=0;i<y;i++)
			{
				if(in[Vy][Hy]>in[Vy][i])
				{
					for(j=0;j<x;j++)
					{
						if(in[Vy][i] < in[j][i])
						{
							yes=false;
							break;
						}
						
					}
					if(yes==false)break;
				}
			}
			if(yes==false)break;
		}
		if(yes==false)break;
	}
	return yes;
}
int main()
{
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");
	int n;
	fin>>n;
	int count=1;
	
	char input;
	int i,j;
	bool isempty,X,O;
	while(n--)
	{
		isempty=false;
		fout<<"Case #"<<count<<": ";
		count++;
		fin>>x>>y;
		for(i=0;i<x;i++)
		{
			for(j=0;j<y;j++)
			{
				fin>>in[i][j];
			}
		}
		//input over
		X=judge();
		if(X)
		{
			fout<<"YES"<<endl;
		}
		else 
		{
			fout<<"NO"<<endl;
		}
		
	}
	return 0;
}