#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		int n;
		double c;
		vector<double> v1,v2;
		cin>>n;
		for(int i=0;i<n;i++)
		{
			cin>>c;
			v1.push_back(c);
		}
		for(int i=0;i<n;i++)
		{
			cin>>c;
			v2.push_back(c);
		}
		sort(v1.begin(),v1.end());
		sort(v2.begin(),v2.end());
		int x=0,y=0;
		while(x<n)
		{
			if(v1[x] < v2[y])
				y--;
			x++;
			y++;
		}
		int x1=0, y1=0;
		while(y1<n)
		{
			if(v1[x1] >v2[y1])
				x1--;
			x1++;
			y1++;
		}
		printf("Case #%d: %d %d\n",i,y,n-x1);
	}
}