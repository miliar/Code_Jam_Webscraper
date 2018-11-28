#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int a[10][10],b[10][10];

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int i,j,k,fr,sr,cases,cnt,t,num;
	scanf("%d",&t);
	for(cases=1;cases<=t;cases++)
	{
		scanf("%d",&fr);
		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++)
			scanf("%d",&a[i][j]);
		
		scanf("%d",&sr);
		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++)
			scanf("%d",&b[i][j]);
		
		cnt=0;
		num=0;
		
		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			{
				if(a[fr][i]==b[sr][j])
				{
					cnt++;
					num = a[fr][i];
				}
			}
		}
		
		if(cnt==1)
			printf("Case #%d: %d\n",cases,num);
		else if (cnt>1)
			printf("Case #%d: Bad magician!\n",cases);
		else
		printf("Case #%d: Volunteer cheated!\n",cases);
	     	
	}
	
	return 0;
}