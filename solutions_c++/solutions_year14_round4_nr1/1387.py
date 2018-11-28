#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <math.h>
using namespace std;

int main()
{
	int T;
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		int n,c;
		cin>>n>>c;
		int ans=0,a;
		vector<int> v;
		for(int i=0;i<n;i++)
		{
			cin>>a;
			v.push_back(a);
		}
		sort(v.begin(),v.end());
		int s = 0;
		for(int i=0,count=0;count<n;i++)
		{
			int d = v[n-i-1] + v[i-s];
			if(d > c)
			{
				s++;
				count++;
				ans++;
			}
			else
			{
				count+=2;
				ans++;
			}
		}
		cout<<"Case #"<<t<<": "<<ans<<endl;
	}
}