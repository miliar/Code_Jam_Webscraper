#include<bits/stdc++.h>
using namespace std;
int main()
{
	ios_base::sync_with_stdio(false);
	long long int t,i,d,j;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		cin>>d;
		long long int a[d];
		for(j=0;j<d;j++)
		{
			cin>>a[j];
		}
		long long int max_val=-1;
		for(j=0;j<d;j++)
		{
			if(a[j]>max_val)
				max_val=a[j];
		}
		long long int min_time=LLONG_MAX;
		for(long long int divisions=1;divisions<=max_val;divisions++)
		{
			long long int eat_time=0;
			long long int div_time=0;
			for(long long int k=0;k<d;k++)
			{
				if(divisions>=a[k])
					eat_time=max(eat_time,a[k]);
				else
				{
					if(a[k]%divisions==0)
					{
						div_time=div_time+((a[k]/divisions)-1);
					}
					else
					{
						div_time=div_time+(a[k]/divisions);
					}
				}
				eat_time=max(eat_time,divisions);
			}
			min_time=min(min_time,(eat_time+div_time));
			//cout<<"for division "<<divisions<<" min time = "<<min_time<<endl;
		}
		cout<<"Case #"<<i<<": "<<min_time<<"\n";
	}
	return 0;
}