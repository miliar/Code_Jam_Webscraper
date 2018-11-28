#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <vector>
#include <stack>
#include <queue>
#include <cstdlib>
#include <map>
#include <algorithm>
using namespace std;
int main()
{
	int T;
	scanf("%d",&T);
	for(int i=0;i<T;i++)
	{
		int a;
		scanf("%d",&a);
		int arr[4];
		a--;		
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				int inp;
				scanf("%d",&inp);
				if(j==a)
					arr[k]=inp;
			}
		}
		int b;
		scanf("%d",&b);
		b--;
		int matches=0,matched=-1;
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				int inp;
				scanf("%d",&inp);
				if(j==b)
				{
					for(int l=0;l<4;l++)
					{
						if(arr[l]==inp)
						{
							matches++;
							matched=inp;
						}
					}
				}
			}
		}
		printf("Case #%d: ",i+1);
		if(matches==1)
			printf("%d\n",matched);
		else if(matches > 1)
			printf("Bad magician!\n");
		else
			printf("Volunteer cheated!\n");
	}
}
