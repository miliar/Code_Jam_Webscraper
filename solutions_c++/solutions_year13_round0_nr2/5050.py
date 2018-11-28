#include<algorithm>
#include<iostream>
#include<vector>
#include<stdio.h>
#include<fstream>
using namespace std;
int mow[100][100];
int origin[100][100];
int main()
{
	fstream fin("mow.txt");
	fstream fout("re.txt", ios::out);
	int T;
	fin>>T;
	for(int round=1;round<=T;round++)
	{
		int N,M;
		fin>>N>>M;
		for(int i=0;i<N;i++)
		{
			for(int j=0;j<M;j++)
			{
				fin>>mow[i][j];
			//	fout<<mow[i][j]<<" ";
			}
			  // fout<<endl;
		}
		        //fout<<endl<<endl;
		int maxnumber=0;
		int x,y;
	    for(int i=0;i<N;i++)
	    {
	    	for(int j=0;j<M;j++)
	    	{
	    		if(maxnumber<mow[i][j])
	    		{
	    			maxnumber=mow[i][j];
	    			x=i;
	    			y=j;
	    		}
	    	}
	    }
	    for(int i=0;i<N;i++)
	    {
	    	for(int j=0;j<M;j++)
	    	{
	    		if(i==x||j==y)
	    		{
	    			origin[i][j]=mow[i][j];
	    		}
	    		else
	    		{
	    			origin[i][j]=min(mow[x][j],mow[i][y]);
	    		}
	    	}
	    }
	    bool couldbe=true;
	    for(int i=0;i<N;i++)
	    {
	    	for(int j=0;j<M;j++)
	    	{
	    		//fout<<origin[i][j]<<" ";
	    		if(origin[i][j]!=mow[i][j])
	    		{
	    			couldbe=false;
	    		}
	    	}
	    	   // fout<<endl;
	    }
		
		if(couldbe)
		{
			fout<<"Case #"<<round<<": YES"<<endl;
		}
		else
		{
			fout<<"Case #"<<round<<": NO"<<endl;
		}
	}
}
