#include <iostream>
#include <fstream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <iomanip>

using namespace std;

int a[20],b[20],n,i,x,cur,num,j,tt,t;

int main()
{
	//ios_base::sync_with_stdio(false);
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	cin>>t;
	for (tt=1; tt<=t; tt++)
	{
		for (i=1; i<=16; i++)
		{
			a[i]=0;
			b[i]=0;
		}          
		cin>>n;
		for (i=1; i<=4; i++)
		{
			for (j=1; j<=4; j++)
			{
				cin>>x;
				if (i==n)
					a[x]=1;
			}
		}
		cin>>n;
		for (i=1; i<=4; i++)
		{
			for (j=1; j<=4; j++)
			{
				cin>>x;
				if (i==n)
					b[x]=1;
			}
		}
		num=0;
		cur=-1;
		for (i=1; i<=16; i++)
		{
			if (a[i] && b[i])
			{
				num++;
				cur=i;
			}
		}
		if (num==0)
		{
			printf("Case #%d: Volunteer cheated!\n",tt);
		}
		else
		{
			if (num>1)
				printf("Case #%d: Bad magician!\n",tt);
			else
			{
				printf("Case #%d: %d\n",tt,cur);				
			}
		}

	}
}


