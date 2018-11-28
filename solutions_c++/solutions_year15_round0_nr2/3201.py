/******************    Author : Hrishikesh Vaidya *********************/
//Codejam2.cpp
#include <stdio.h>
#include <vector>
#include <queue>
#include <string.h>
#include <stdlib.h>
#include <cstdio>
#include <map>
#include <string>
#include <iostream>
#include <algorithm>
#include <math.h>
#define ld long
#define ll long long
using namespace std;

int arr[1204];
int main()
{
	int tt,C=1;
	scanf("%d",&tt);
	while(tt--)
	{
		int i,d,j,temp,ans=100000;
		scanf("%d",&d);
		for(i=0;i<d;i++)
			scanf("%d",&arr[i]);
	
		for(i=1;i<=1000;i++)
		{	
			temp=0;
			for(j=0;j<d;j++)
			{
				if(arr[j]>i)
				{
					if(arr[j]%i==0)
						temp+=(arr[j]/i-1);
					else
						temp+=(arr[j]/i);
				}
			}
			ans=min(ans,i+temp);
		}
		printf("Case #%d: %d\n", C++,ans);
	}
	return 0;	
}

