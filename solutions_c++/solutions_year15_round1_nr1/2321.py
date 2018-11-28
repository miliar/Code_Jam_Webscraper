#include<iostream>
#include<algorithm>
#include<stdio.h>
using namespace std;
int main()
{
	remove("output.txt");
	freopen("A-large.in","r", stdin);
	freopen("output.txt","w", stdout);
	
	int t;
	int n;
	long s1, s2, r;
	
	cin>>t;
	
	for(int i = 1; i <= t; ++i)
	{
		s1 = 0;
		s2 = 0;
		r = 0;
		cin>>n;
		long a[n];
		
		for(int i = 0; i < n; ++i)
			cin>>a[i];
			
		for(int i = 1; i < n; ++i)
			{
				if(a[i] < a[i - 1])
					s1 += a[i - 1] - a[i];
			}
		
		for(int i = 1; i < n; ++i)
		{
			if(a[i - 1] - a[i] > r)
				r = a[i - 1] - a[i];
			
		}
	
		for(int i = 0; i < n - 1; ++i)
		{
			s2 += min(a[i], r);
		}

		cout<<"Case #"<<i<<": "<<s1<<" "<<s2<<"\n";
	}
	fclose(stdout);
	fclose(stdin);
}
