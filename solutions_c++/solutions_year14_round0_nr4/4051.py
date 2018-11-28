#include <iostream>
#include <fstream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <iomanip>

using namespace std;

long double x;
int a[5000],b[5000],n,qa,rez1,rez2,qb,i,j,d[5000],t,tt;

int main()
{
	//ios_base::sync_with_stdio(false);
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>t;
	for (tt=1; tt<=t; tt++)
	{
		cin>>n;
		for (i=0; i<n; i++)
		{
			cin>>x;
			a[i]=x*100000;
			//c[a[i]]++;
		}
		for (i=0; i<n; i++)
		{
			cin>>x;
			b[i]=x*100000;
		}
		sort(a,a+n);
		sort(b,b+n);
		rez2=0;
		for (i=0; i<n; i++)
			d[i]=0;
		for (i=0; i<n; i++)
		{
			for (j=0; j<n; j++)
				if (b[j]>a[i] && d[j]==0)
					break;
			if (j==n) rez2++;
			else
			{
				d[j]=1;
			}
		}
		for (i=0; i<n; i++)
			d[i]=0;

		rez1=0;
		for (i=0; i<n; i++)
		{
			for (j=0; j<n; j++)
					if (d[j]==0) break;
			if (a[i]>b[j])
			{
				rez1++;
				
				d[j]=1;	

			}
			else
			{
				for (j=n-1; j>=0; j--)
					if (d[j]==0) break;
				d[j]=1;	
			}
		}
		cout<<"Case #"<<tt<<": "<<rez1<<' '<<rez2<<endl;
	}
	return 0;
}


