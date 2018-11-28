#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<string>
#include<vector>
using namespace std;
int main()
{
	long long int t,n,iter=0;
	FILE *f;
	f=fopen("test.txt","w");
	cin>>t;
	for (int i=0;i<t;i++)
	{
		vector<long long int>ob;
		iter=0;
		cin>>n;
		int d=n;
		if(n==0)
		{
			
			fprintf(f,"Case #%d: %s\n",i+1,"INSOMNIA");
			continue;
		}
		while(d)
		{
			int v=d%10;
			if (!( std::find(ob.begin(), ob.end(), v) != ob.end() ))
			{
				
				ob.push_back(v);
			 }
			d=d/10;
		}
		iter=1;
		while(ob.size()<10)
		{
			int d=++iter*n;
			while(d)
			{
				int v=d%10;
				if (!( std::find(ob.begin(), ob.end(), v) != ob.end() ))
				{
			
					ob.push_back(v);
				}
				d=d/10;
			}
			

		}
		
		fprintf(f,"Case #%d: %lld\n",i+1,iter*n);
	}
}
