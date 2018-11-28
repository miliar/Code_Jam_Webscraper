#include <cstdio>
#include <iostream>

using namespace std;

int main ()
{
	freopen("D-large.in","r",stdin);
	freopen("t4.out","w",stdout);	
	
	int i,j,n;
	int tt,t;
	double a[1111],b[1111];
	int c[1111];
	cin >> t;
	for (tt=1; tt<=t; tt++)
	{
		cin >> n;
		for (i=1; i<=n; i++) cin >> b[i];
		for (i=1; i<=n; i++) cin >> a[i];
		for (i=1; i<=n; i++) c[i]=0;
		
		
		for (i=1; i<=n; i++)
		for (j=i+1; j<=n; j++)
		{
			if (a[i]>a[j])
			{
				double t=a[i];
				a[i]=a[j];
				a[j]=t;
			}
			if (b[i]>b[j])
			{
				double t=b[i];
				b[i]=b[j];
				b[j]=t;
			}
		}
		int ans1=0;
		for (i=1; i<=n; i++)
		{
			int p=0;
			for (j=1; j<=n; j++)
			{
				if ((a[j]<b[i])&&(c[j]==0)) 
				{
					c[j]=1;
					p=1;
					ans1++;
					break;
				}
			}
			if (p==0)
			{
				while (c[j]==1)
				{
					j--;
				}
				c[j]=1;
			}
		}
		//
		/*for (i=1; i<=n; i++)
		{
			double t=a[i];
			a[i]=a[n-i+1];
			a[n-i+1]=t;
		}*/
		/*int ii;
			for (ii=1; ii<=n; ii++) cout << a[ii] << ' ';
			cout << endl;
			for (ii=1; ii<=n; ii++) cout << b[ii] << ' ';
			cout << endl;*/
		for (i=1; i<=n; i++) c[i]=0;
		int ans2=0;
		for (i=1; i<=n; i++)
		{
			int p=0;
			for (j=1; j<=n; j++)
			{
				if ((a[j]>b[i])&&(c[j]==0))
				{
					c[j]=1;
					p=1;
					break;
				}
			}

			if (p==0)
			{
				while (c[j]==1) j--;
				int k;
				for (k=1; k<=n; k++)
				{
					if (c[k]==0) 
					{
						c[k]=1;
						ans2++;
						break;
					}
				}
			} 
			//for (ii=1; ii<=n; ii++) cout << c[ii] << ' ';
			//cout << endl;
		}
		
		cout << "Case #" << tt << ": " << ans1 << ' ' << ans2 << endl;
		
	}
}
