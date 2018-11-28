//
//  main.cpp
//  Testc++
//
//  Created by Shelven Zhou on 15/2/20.
//  Copyright (c) 2015年 Shelven Zhou. All rights reserved.
//

#include <stdio.h>
#include <string>
#include <fstream>
#include <iostream>

using namespace std;

int a[5][5]={{0,0,0,0,0},{0,1,2,3,4},{0,2,-1,4,-3},{0,3,-4,-1,2},{0,4,3,-2,-1}};

int cal(int i, int j)
{
	int re=1;
	if(i<0)
	{
		re=-re;
		i=-i;
	}
	if(j<0)
	{
		re=-re;
		j=-j;
	}
	
	return re*a[i][j];
}

int char2i(char c)
{
	if(c=='1')
		return 1;
	else
		return c-'i'+2;
}

int main (int argc, char *argv[])
{
	ifstream fin("C-small-attempt0.in");
	ofstream fout("C-small-attempt0.out");
	
	int T,count=0;
	fin>>T;
	
	while(count++<T)
	{
		bool flag=false;
		int l,x;
		string line;
		fin>>l>>x;
		fin>>line;
		
		if(l*x<3)
		{
			flag=false;
		}
		else if(l*x==3)
		{
			flag=(line=="ijk");
		}
		else
		{
			int n=1,iLen=0,kLen=0;
			bool iFlag=false,kFlag=false;
			
			for(int times=0;times<x;times++)
			{
				for(int len=0;len<l;len++)
				{
					int b=char2i(line[len]);
					n=cal(n,b);
					
					if(!iFlag)
					{
						iLen++;
						if(n==2)
							iFlag=true;
					}
				}
			}
			
			if(n==-1&&iFlag)
			{
				n=1;
				for(int times=0;times<x;times++)
				{
					for(int len=l-1;len>=0;len--)
					{
						int b=char2i(line[len]);
						n=cal(b,n);
						
						if(!kFlag)
						{
							kLen++;
							if(n==4)
							{
								kFlag=true;
								break;
							}
						}
					}
					if(kFlag)
						break;
				}
				
				flag=iFlag&&kFlag&&(iLen+kLen<l*x);
			}
			else
				flag=false;
		}
		
		fout<<"Case #"<<count<<(flag?": YES":": NO")<<endl;
	}
}