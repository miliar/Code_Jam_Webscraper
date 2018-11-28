#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
	int tc,t,n,i,win1,win2,j,m;
	double a[1001],b[1001],c[1001],d[1001],min;
	cin>>tc;
	for (t=1;t<=tc;t++)
	{
		cin>>n;
		for (i=0;i<n;i++)
		cin>>a[i];
		sort(a,a+n);
		for (i=0;i<n;i++)
		cin>>b[i];
		sort(b,b+n);
		for (i=0;i<n;i++)
		{
			c[i]=a[i];
			d[i]=b[i];
		}
	//	for (i=0;i<n;i++) cout<<a[i]<<" ";cout<<endl;
	//	for (i=0;i<n;i++) cout<<b[i]<<" ";cout<<endl;
		win2=0;
		win1=0;
		for (i=0;i<n;i++)
		{
			min=c[i];
			j=i;
			while (j<n&&d[j]<min)
			{
				j++;
			}
			if (j==n)
			{
				//d[i]=-1;
				win2=n-i;
	//			for (i=0;i<n;i++) cout<<a[i]<<" ";cout<<endl;
	//	for (i=0;i<n;i++) cout<<d[i]<<" ";cout<<endl;
				break;
			}
			else d[j]=-1;
			sort(d,d+n);
		}
		j=0;
		m=n-1;
		for (i=0;i<n;i++)
		{
			if (a[i]>b[j])
			{
				b[j]=-1;
				j++;
				win1++;
			}
			else 
			{
				b[m]=-1;
				m--;
			}
		}
		cout<<"Case #"<<t<<": "<<win1<<" "<<win2<<endl;
	}
	return 0;
}
