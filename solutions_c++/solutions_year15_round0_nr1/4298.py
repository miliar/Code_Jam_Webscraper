#include <stdio.h>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <math.h>
#include <string>
#include <math.h>
using namespace std;
int main()
{

	int T;
	int t;
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		int N;
		cin >> N;
		char *a = new char [N+1];
		for(int i=0;i<=N;i++)
		{
			cin >> a[i];
		}

		int ans=0;
		if(N==0)
		{
			printf("Case #%d: %d\n",t,ans);
			continue;
		}
		int temp;
		temp = a[0]-'0';
		for(int i=1;i<=N;i++)
		{	
			if(i <= temp)
			{
				temp = temp + (a[i]-'0');
			}
			else
			{
				ans = ans + abs(temp-i);
				temp = temp + abs(temp-i) + (a[i]-'0');

			}

		}
		printf("Case #%d: %d\n",t,ans);

	}
	
	return 0;	

}
