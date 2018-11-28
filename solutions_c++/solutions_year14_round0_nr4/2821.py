#include<iostream>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<map>
#include<vector>
#include<cstdio>
#include<climits>
#include<cmath>
#include<cstring>
using namespace std;

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	long long t,test,n,i,j,c1,c2;
	cin>>test;
	for(t=1;t<=test;t++)
	{
		cin>>n;
		double x[n],y[n];
		for(i=0;i<n;i++)
			cin>>x[i];
		for(i=0;i<n;i++)
		{
			cin>>y[i];
		}
		sort(x,x+n);
		sort(y,y+n);
		i=0;j=0;c1=0;
		while(i<n&&j<n)
		{
			if(x[i]>=y[j])
			{
				i++;j++;
				c1++;
			}
			else
			{
				i++;
			}
		}
		i=0;j=0;c2=0;
		while(i<n&&j<n)
		{
			if(x[i]<y[j])
			{
				i++;j++;
				
			}
			else
			{
				j++;
				c2++;
			}
		}
		cout<<"Case #"<<t<<": "<<c1<<" "<<c2<<endl;
	}
	return 0;
}

