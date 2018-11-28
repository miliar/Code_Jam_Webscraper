#include<bits/stdc++.h>
using namespace std;
int main()
{
	//ios_base::sync_with_stdio(false);
	long long int t,i;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		long long int smax,j;
		cin>>smax;
		int a[smax+1];
		long long int people_standing=0,extra_people=0;
		getchar();
		for(j=0;j<=smax;j++)
		{
			char c=getchar();
			//cout<<c<<" ";
			a[j]=c-'0';
			//cout<<a[j]<<" ";
		}
		people_standing=a[0];
		for(j=1;j<=smax;j++)
		{
			if(people_standing>=j)
			{
				people_standing+=a[j];
			}
			else
			{
				long long int diff=abs(people_standing-j);
				people_standing+=diff;
				extra_people+=diff;
				people_standing+=a[j];
			}
		}
		cout<<"Case #"<<i<<": "<<extra_people<<"\n";
	}
}