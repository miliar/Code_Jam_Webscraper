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
	int	flag = 0,answer,n,i=0,j,index = 0,x,y;
	int A,B,K,sum;
	freopen ("d:/Codejam/B-small-attempt0.in","r",stdin);
    freopen ("d:/Codejam/B-small-attempt0.out","w",stdout);
	scanf("%d",&n);
	int no_of_prior[102],no_dependency,index_of_dependent;
	while(n--)
	{
		scanf("%d %d %d",&A,&B,&K);
		sum = 0;
			for(i=0 ;i<A; i++)
				for(j=0 ;j<B; j++)
				{
					x = i & j;
					if(x<K)
						sum++;
				}

			printf("Case #%d: ",++index);
			printf("%d\n",sum);
	}
	return 0;
}
