#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
using namespace std;


void main()
{
	int t;
	cin>>t;
	for(int ii=0; ii<t; ii++)
	{
		int n,x;
		vector<int> s;
		cin>>n>>x;
		for(int i=0; i<n; i++)
		{
			int ss;
			cin>>ss;
			s.push_back(ss);
		}

		sort(s.begin(), s.end());
		int cnt=0;
		for(int i=s.size()-1; i>=0; i--)
		{
			if(s[i]==-1)
				continue;
			cnt++;
			int bb=s[i];
			for(int j=i-1; j>=0; j--)
			{
				if(s[j]==-1)
					continue;
				if(s[i]+s[j]<=x)
				{
					s[j]=-1;
					break;
				}
			}
		}

		cout<<"Case #"<<ii+1<<": "<<cnt<<endl;
	}
}
