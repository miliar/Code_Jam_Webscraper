#include<iostream>
#include<cstdio>
#include<map>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		cout<<"Case #"<<(i+1)<<": ";
		std::map<int, int> mp;
		int n;
		cin>>n;
		//int arr2[2510]={0}
		//int arr[200]={0};int l=0;
		for(int j=1;j<=(2*n-1);j++)
		{
			for(int k=1;k<=n;k++)
			{
				int ele;
				cin>>ele;
				mp[ele]++;
			}
		}
		std::map<int,int>::iterator it;
		for (it=mp.begin(); it!=mp.end(); ++it)
    		{
    			if(it->second%2!=0)
    				cout<<it->first<<" ";

    		}
    	cout<<"\n";

	}
}