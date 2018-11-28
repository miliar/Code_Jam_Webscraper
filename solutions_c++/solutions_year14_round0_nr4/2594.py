#include<iostream>
#include<string>
#include<cstdio>
#include<limits>
#include<vector>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
using namespace std;

//#define SMALL
#define LARGE

int main()
{

	#ifdef SMALL
		freopen("D-small-attempt0.in","rt",stdin);
		freopen("D-small.out","wt",stdout);
	#endif

	#ifdef LARGE
		freopen("D-large.in","rt",stdin);
		freopen("D-large.out","wt",stdout);
	#endif

	int i,t;
	cin>>t;
	
	for(i=1;i<=t;i++)
	{
		int ans1=0,ans2=0,n,j,k;
		double temp;
		vector<double> a1,a2,temp1,temp2;
		
		cin>>n;
				
		for(j=0;j<n;j++)
		{
			cin>>temp;
			a1.push_back(temp);
		}
		
		for(j=0;j<n;j++)
		{
			cin>>temp;
			a2.push_back(temp);
		}
		
		temp1=a1;
		temp2=a2;
		
		sort(temp1.begin(),temp1.end());
		sort(temp2.begin(),temp2.end());
		
		for(j=0;j<n;j++)
		{
			for(k=0;k<temp2.size();k++)
			{
				if(temp1[j]>temp2[k])
				{
					ans1++;
					temp2.erase(temp2.begin()+k);
					break;
				}
			}
		}
		
		temp1=a1;
		temp2=a2;
		
		sort(temp1.begin(),temp1.end(),greater<double>());
		sort(temp2.begin(),temp2.end(),greater<double>());
		
		k=0;
		for(j=0;j<n;j++)
		{
			if(temp1[j]>temp2[k])
				ans2++;
				
			else
				k++;
		}
		
		cout<<"Case #"<<i<<": "<<ans1<<" "<<ans2<<endl;		
	}
	
	return 0;
}
