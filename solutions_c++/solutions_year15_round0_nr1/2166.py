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
	ifstream fin("A-small-attempt1.in");
	ofstream fout("A-small-attempt1.out");
	
	int T,count=0;
	fin>>T;
	
	while(count++<T)
	{
		int re=0;
		
		int h;
		string a;
		
		fin>>h>>a;
		
		int clapped=0;
		for(int i=0;i<=h;i++)
		{
			if(clapped>=i)
				clapped+=(a[i]-'0');
			else
			{
				if(a[i]!='0')
				{
					re+=i-clapped;
					clapped+=re;
					clapped+=(a[i]-'0');
				}
			}
		}
		//		cout<<a<<endl;
		
		fout<<"Case #"<<count<<": "<<re<<endl;
	}
}