#include<stdio.h>
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int j=0;j<t;j++)
	{
		float n,temp;
		vector<float> v1;
		vector<float> v2;
		cin>>n;
		for(int i=0;i<n;i++)
		{
			cin>>temp;
			v1.push_back(temp);
		}
		sort(v1.begin(),v1.end());
	    for(int i=0;i<n;i++)
		{
			cin>>temp;
			v2.push_back(temp);
		}
		sort(v2.begin(),v2.end());
		int cnt=0,cnt1=0;
		int i=0,k=0;
		while(i<n&&k<n)
		{
			if(v1[i]>v2[k])
			{
				cnt++;
				i++;
				k++;
			}
			else
			   i++;
		}
		i=0,k=0;
		while(i<n&&k<n)
		{
			if(v1[i]<v2[k])
			{
				cnt1++;
				i++;
				k++;
			}
			else
			   k++;
		}
		cout<<"Case #"<<j+1<<": ";
		cout<<cnt<<" "<<n-cnt1<<endl;
	}
	return 0;
}

