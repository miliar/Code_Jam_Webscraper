#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <string>
using namespace std;

int main()
{
	int T;
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		printf("Case #%d: ",t);
		int n,x;
		cin>>n>>x;
		int s[n];
		for (int i = 0; i < n; ++i)
		{
			cin>>s[i];
		}
		sort(s,s+n);
		
		int count=0;
		for (int i = 0,j=n-1; j>=i; )
		{
			if(s[i]+s[j]<=x)
			{
				i++;
			}
			j--;
			count++;
		}
		// if(n%2==1) count++;
		printf("%d\n",count );
	}
}