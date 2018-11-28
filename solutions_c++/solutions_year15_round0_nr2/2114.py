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
#include <algorithm>

#define MAX 1000

using namespace std;

int main (int argc, char *argv[])
{
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");
	
	int T,count=0;
	fin>>T;
	
	while(count++<T)
	{
		int d;
		int a[MAX];
		
		memset(a,0,MAX);
		
		int max=-1;
		fin>>d;
		for(int i=0;i<d;i++)
		{
			fin>>a[i];
			if(a[i]>max)
				max=a[i];
		}
		
		int min=max;
		for(int t=1;t<=max;t++)
		{
			int count=0,cost=0;
			for(int i=0;i<d;i++)
			{
				if(a[i]>t)
				{
					
					count+=(a[i]-1)/t;
				}
			}
			
			cost=count+t;
			if(cost<min)
				min=cost;
		}		
		
		fout<<"Case #"<<count<<": "<<min<<endl;
	}
}