#include<iostream>
#include<cstdio>
#include<queue>
#include<algorithm>

using namespace std;

int get1(deque<double> v1, deque<double> v2)
{
	int r = 0;
	for(int i=0;i<v1.size();i++)
	{
		int j;
		for(j=0;j<v2.size();j++)
			if( v2[j] > v1[i] )
				break;
		if( j <v2.size() )
			v2.erase(v2.begin()+j);
		else
		{
			r++;
			v2.pop_front();
		}

	}
	return r;
}

int get2(deque<double> v1, deque<double> v2)
{
	int r = 0;
	for(int i=0;i<v2.size();i++)
	{
		int j;
		for(j=0;j<v1.size();j++)
			if( v1[j] > v2[i] )
				break;
		if( j <v1.size() )
		{
			v1.erase(v1.begin()+j);
			r++;
		}
		else
		{
			return r;
		}

	}
	return r;
}

int main()
{
	freopen("in.txt","rt",stdin);
	freopen("Dout.txt","wt",stdout);

	int TC;
	cin>>TC;
	double x = 0;
	int n;
	for(int tc=0;tc<TC;++tc)
	{
		cin>>n;
		deque<double> v1,v2;
		for(int i=0;i<n;i++)
		{
			cin>>x;
			v1.push_back(x);
		}

		for(int i=0;i<n;i++)
		{
			cin>>x;
			v2.push_back(x);
		}

		sort(v1.begin(),v1.end());
		sort(v2.begin(),v2.end());
		printf("Case #%d: %d %d\n",tc+1,get2(v1,v2),get1(v1,v2));

	}
	return 0;
}