#include<iostream>
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<double>a;vector<double>b;
vector<double>at;vector<double>bt;
int main()
{
	freopen("test.txt","w",stdout);
	int t;cin>>t;double temp;
	int ii,i,j,k;int n;
	for(ii=1;ii<=t;ii++)
	{
		cin>>n;int sum=0;
		a.clear();b.clear();at.clear();bt.clear();
		for(i=0;i<n;i++)
		{cin>>temp;a.push_back(temp);at.push_back(temp);}
		for(i=0;i<n;i++)
		{cin>>temp;b.push_back(temp);bt.push_back(temp);}
		cout<<"Case #"<<ii<<": ";
		//cout<<endl;
		sort(a.begin(),a.end());sort(b.begin(),b.end());
		//for(i=0;i<n;i++)cout<<a[i]<<" ";cout<<endl;
		//for(i=0;i<n;i++)cout<<b[i]<<" ";cout<<endl;
		while(!a.empty())
		{
			if(a[0]>b[0])
			{
				sum++;a.erase(a.begin());b.erase(b.begin());
			}
			else
			{
				a.erase(a.begin());b.pop_back();
			}
		}
		cout<<sum<<" ";sum=0;
		sort(at.begin(),at.end());sort(bt.begin(),bt.end());
		while(!at.empty())
		{
			for(i=0;i<at.size();i++)
			if(bt[i]>at[0])
			{
				sum++;bt.erase(bt.begin()+i);at.erase(at.begin());
				goto end;
			}
			if(i==at.size())
			{
				at.erase(at.begin());bt.erase(bt.begin());
			}
			end:;
		}
		sum=n-sum;
		cout<<sum<<endl;
	}
}
