#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main()
{
	int T;
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		int n;
		cin>>n;
		vector<float> v1,v2;
		float f;
		for(int i=0;i<n;i++)
		{
			cin>>f;
			v1.push_back(f);
		}
		for(int i=0;i<n;i++)
		{
			cin>>f;
			v2.push_back(f);
		}
		sort(v1.begin(),v1.end());
		sort(v2.begin(),v2.end());
		int c1=n-1,c2=n-1;
		int count = 0;
		while(c2>=0)
		{
			if(v1[c1]>v2[c2])
			{
				count++;
				c1--;
				c2--;
			}
			else
			{
				c2--;
			}
		}
		c1=c2=0;
		int z = 0;
		while(c2 != n)
		{
			if(v1[c1]<v2[c2])
			{
				c1++;
				c2++;
				z++;
			}
			else
			{
				c2++;
			}
		}
		z = n - z;
		printf("Case #%d: %d %d\n",t,count,z);
	}
}