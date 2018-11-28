#include <iostream>
#include <stdio.h>
#include <string>
#include <ctype.h>
#include <stdlib.h>
#include <math.h>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <utility>
#include <map>
#include <vector>
#include <list>
#include <string>
#include <set>
#include <stack>
#include <queue>
#include <deque>
#include <climits>
#include <limits.h>
 
#define MOD 1000000007 
 
typedef long long LL;
 
using namespace std;

// A utility function to get minimum of two numbers
int minVal(int x, int y) { return (x < y)? x: y; }
 
LL gcd(LL u, LL v)
{
	return (v != 0)?gcd(v, u%v):u;
}

int n;
bool isSafe(int arr[], int total)
{
	int i;
	total>>=1;
	for(i=0;i<n;++i)
	{
		if(arr[i] > total)return false;
	}
	return true;
}

int main()
{
	int t;
	cin>>t;	
	for(int tc=1;tc<=t;tc++)
	{
		cin>>n;
		int arr[26];
		int i,j;
		int total=0;
		for(i=0;i<n;++i)
		{
			cin>>arr[i];
			total+=arr[i];
		}

		printf("Case #%d: ", tc);
		while(total!=0)
		{
			for(i=0;i<n;++i)
			{
				arr[i]--;total--;
				if(isSafe(arr, total))
				{
					printf("%c ", (char)(i+65));
					break;
				}
				else
				{
					arr[i]++;total++;
				}
			}
			if(i!=n)continue;

			for(i=0;i<n;++i)
			{
				for(j=0;j<n;++j)
				{
					if(i==j)continue;

					arr[i]--;total--;
					arr[j]--;total--;
					if(isSafe(arr, total))
					{
						printf("%c%c ", (char)(i+65),(char)(j+65));
						break;
					}
					else
					{
						arr[i]++;total++;
						arr[j]++;total++;
					}
				}
				if(j!=n)break;
			}
			if(i!=n)continue;
		}
		printf("\n");
	}

	return 0;
}
