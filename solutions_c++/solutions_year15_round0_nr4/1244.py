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

int main (int argc, char *argv[])
{
	ifstream fin("D-small-attempt3.in");
	ofstream fout("D-small-attempt3.out");
	
	int T,count=0;
	fin>>T;
	
	while(count++<T)
	{
		bool f=false;
		
		int x,r,c;
		fin>>x>>r>>c;
		
		if(x==1)
			f=true;
		else if((r*c)%x==0)
		{
			if(x==2)
				f=true;
			else if(x==3)
				f=((r*c)!=3);
			else
			{
				int time=r*c;
				if(time==12||time==16)
					f=true;
			}
		}
		
		fout<<"Case #"<<count<<": "<<(f?"GABRIEL":"RICHARD")<<endl;
	}
}