#include<iostream>
#include<stdio.h>
#include<cstring>
#include<stdlib.h>
#include <queue>
#include<string>
#include <sstream>
#include<list>
#include<map>
#include<cmath>
#include<algorithm>
#include <unordered_map>
using namespace std;
#define INF 1e9
#define DIVIDE 10000

int main()
{
	int	flag = 0,answer,n,i=0,j,index = 0;
	freopen ("d:/Codejam/A-small-attempt2.in","r",stdin);
    freopen ("d:/Codejam/A-small-attempt2.out","w",stdout);
	int ans1,ans2,a[20][20],b[20][20];
	scanf("%d",&n);
	while(n--)
	{
		flag  = 0;
		scanf("%d",&ans1);
		for(i=1 ; i<=4 ;i++)
			for(j=1 ; j<=4 ;j++)
			scanf("%d",&a[i][j]);
	
		scanf("%d",&ans2);
		for(i=1 ; i<=4 ;i++)
			for(j=1 ; j<=4 ;j++)
			scanf("%d",&b[i][j]);
	for(i=1 ; i<=4 ;i++)
		for(j=1 ; j<=4 ;j++)
			{
			if(a[ans1][i] == b[ans2][j])
				{
				flag++;
				if(flag == 1)
					answer = a[ans1][i];
				}
			}

		printf("Case #%d: ",++index);
		if(flag == 0)
			printf("Volunteer cheated!\n");
		else if(flag == 1)
			printf("%d\n",answer);
		else
			printf("Bad magician!\n");
	}
	return 0;
}
