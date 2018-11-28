#include <cstdio>
#include <sstream>
#include <vector>
#include <list>
#include <cmath>
#include <algorithm>
#include <numeric>
#include <iostream>
#include <functional>
#include <cstdlib>
#include <stack>
#include <queue>
#include <string>
#include <climits>

#pragma once
using namespace std;

#define LLONG long long
#define ULLONG unsigned long long
#define LDOUBLE long double
#define ULDOUBLE unsigned long double

LDOUBLE fair[40];

void init()
{
fair[0]=1;
fair[1]=4;
fair[2]=9;
fair[3]=121;
fair[4]=484;
fair[5]=10201;
fair[6]=12321;
fair[7]=14641;
fair[8]=40804;
fair[9]=44944;
fair[10]=1002001;
fair[11]=1234321;
fair[12]=4008004;
fair[13]=100020001;
fair[14]=102030201;
fair[15]=104060401;
fair[16]=121242121;
fair[17]=123454321;
fair[18]=125686521;
fair[19]=400080004;
fair[20]=404090404;
fair[21]=10000200001;
fair[22]=10221412201;
fair[23]=12102420121;
fair[24]=12345654321;
fair[25]=40000800004;
fair[26]=1000002000001;
fair[27]=1002003002001;
fair[28]=1004006004001;
fair[29]=1020304030201;
fair[30]=1022325232201;
fair[31]=1024348434201;
fair[32]=1210024200121;
fair[33]=1212225222121;
fair[34]=1214428244121;
fair[35]=1232346432321;
fair[36]=1234567654321;
fair[37]=4000008000004;
fair[38]=4004009004004;
fair[39]=100000020000001;
}

void main()
{
	freopen("input.txt","r",  stdin);
	freopen("output.txt", "w", stdout);

	int T = 0;	
	cin>>T;
	LDOUBLE A,B;	
	init();

	for(int t = 1; t <= T; t++)
	{
		int count=0;
		cin>>A>>B;
		for(int i = 0; fair[i]<=B;i++)
		{
			if(fair[i]<A)
			{
				continue;
			}

			count++;
		}
		cout<<"Case #"<<t<<": "<<count<<endl;
	}	
}