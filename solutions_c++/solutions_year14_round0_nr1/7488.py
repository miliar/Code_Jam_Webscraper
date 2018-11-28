#include<iostream>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <queue>
#include <map>
#include <vector>
#include <cstdio>
#include <string>
#include <stack>
using namespace std;
int a[5][5],b[5][5];
int main()
{
	int t;
	int num,n,i,j,m,result;
	freopen("d:\\test.txt","w",stdout);
	scanf("%d",&t);
	int count=1;
	while(t--)
	{
		scanf("%d",&n);
		n--;
		num=0;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				scanf("%d",&a[i][j]);
		scanf("%d",&m);
		m--;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				scanf("%d",&b[i][j]);
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				if(a[n][i]==b[m][j]){
					num++;
					result=a[n][i];
				}
				printf("Case #%d: ",count++);
				if(num==1)
					printf("%d\n",result);
				else if(num>1)
				{
					puts("Bad magician!");
				}
				else
				{
					puts("Volunteer cheated!");
				}
	}
	return 0;
}
