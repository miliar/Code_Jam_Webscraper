#include<stdio.h>
#include<iostream>
#include<vector>
#include<iterator>
#include<algorithm>

using namespace std;

int main()
{
	int i,j,cnt,t,n,ctr,ctr1;
	double x;
	cin>>t;
	for(i=0;i<t;i++)
	{
		vector<double> v1;
		vector<double> v2;

		vector<double> v3;
		vector<double> v4;
		vector<double>::iterator it;
		vector<double>::iterator it1;
		
		cin>>n;
		for(j=0;j<n;j++)
		{
			cin>>x;
			v1.push_back(x);
			v3.push_back(x);
		}
		for(j=0;j<n;j++)
		{
			cin>>x;
			v2.push_back(x);
			v4.push_back(x);
		}
		sort(v1.begin(),v1.end());
		sort(v2.begin(),v2.end());
		ctr=n;
		cout<<"Case #"<<i+1<<": ";
		while(1)
		{
			if(ctr==0)
			break;
			cnt=0;
			for(it=v1.begin(),it1=v2.begin();it<v1.end();it++,it1++)
			{
				if(*it<*it1)
				{
					cnt=1;
					break;
				}
			}
			if(cnt==1)
			{
				v2.erase(v2.end()-1);
				v1.erase(v1.begin());
				ctr--;
			}
			else
			break;
		}
		cout<<ctr<<" ";
		
		sort(v3.begin(),v3.end());
		sort(v4.begin(),v4.end());
		ctr1=n;
		for(it=v3.end()-1;it>=v3.begin();it--)
		{
			it1=lower_bound(v4.begin(),v4.end(),*it);
			if(it1<v4.end())
			{
				v4.erase(it1);
				ctr1--;
			}
			else
			v4.erase(v4.begin());
		}
		cout<<ctr1<<"\n";
	}
	return 0;
}
