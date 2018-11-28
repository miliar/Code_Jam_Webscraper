#include<iostream>
#include<vector>
#include<algorithm>
#include<cmath>
#include<cstdio>
#include<cstdlib>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		int a;
		cin>>a;
		int b;
		cin>>b;
		int q;
		cin>>q;
		long long int count = 0;
		for(int j=0;j<a;j++)
		{
			for(int k=0;k<b;k++)
			{
				int ans = j & k;
				if(ans<=q-1)
					count++;
			}
		}
		cout<<"Case #"<<i<<":"<<" "<<count<<endl;
	
	}
	cin>>t;
	return 0;
}
