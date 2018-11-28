#include<iostream>
#include <list>
#include<map>
#include<set>
#include<stdio.h>
using namespace std;
int main()
{
	freopen("B-large416.in","r",stdin);  
	freopen("B-large416.out","w",stdout);
	int T;
	scanf("%d",&T);
	int k=1;
	while(T--)
	{
		int N;
		scanf("%d",&N);
		map<int ,int> res;
		int tem;
		for(int i=1;i<=2*N-1;i++)
			for(int j=1;j<=N;j++)
				{
					scanf("%d",&tem);
					if(res.find(tem)==res.end())
					res[tem]=1;
					else
					res[tem]++;
				}
		map<int ,int>::iterator itor=res.begin();
		printf("Case #%d: ",k++);
		while(itor!=res.end())
		{
			if(itor->second%2!=0)
			printf("%d ",*itor);
			itor++;
		}
		printf("\n");
	}
	
}
