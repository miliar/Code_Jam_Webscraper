//
//  main.cpp
//  TestC++
//
//  Created by Shelven Zhou on 15/4/14.
//  Copyright (c) 2015年 Shelven Zhou. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <math.h>
#include <map>

#define MAX 1000
using namespace std;

int reverse(int a)
{
	int re=0;
	while(a)
	{
		int digit=a%10;
		re=re*10+digit;
		a/=10;
	}
	return re;
}

int main(int argc, const char * argv[])
{
	ifstream fin("A-small-attempt2.in");
	ofstream fout("A-small-attempt2.out");
	
	int t,count=0;
	fin>>t;
	while(count++<t)
	{
		int n, step=1;
		fin>>n;
		
		if(n<=19)
			step=n;
		else
		{
			int *a=new int[n+1];
			for(int i=0;i<=n;i++)
				a[i]=9999999;
			for(int i=1;i<=19;i++)
				a[i]=i;
			
			for(int i=20;i<=n;i++)
			{
				if((a[i-1]+1)<a[i])
					a[i]=a[i-1]+1;
				int rev=reverse(i);
				int rrev=reverse(rev);
				if(i==rrev)
					if(rev<i)
						if((a[rev]+1)<a[i])
							a[i]=a[rev]+1;
			}
			
			step=a[n];
		}
		//		cout<<step<<endl;
		fout<<"Case #"<<count<<": "<<step<<endl;
	}
}
