#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		int n;
		cin>>n;
		vector<double> y1,y2;
		double z;
		for(int j=0;j<n;j++)
		{
			cin>>z;
			y1.push_back(z);
		}
		for(int j=0;j<n;j++)
		{
			cin>>z;
			y2.push_back(z);
		}
		std::sort(y1.begin(),y1.end());
		std::sort(y2.begin(),y2.end());
		int k=0,l=0,ans1=0,ans2=0;
		while(k<n && l<n)
		{
			if(y1[k]<y2[l])
			{
				k++;
				l++;
				ans1++;
			}
			else{
				l++;
			}
		}
		k=0;l=0;
		while(k<n && l<n)
		{
			if(y2[k]<y1[l])
			{
				k++;
				l++;
				ans2++;
			}
			else{
				l++;
			}
		}
		cout<<"Case #"<<i<<": ";
		cout<<ans2<<" "<<(n-ans1)<<endl;
	}
}
