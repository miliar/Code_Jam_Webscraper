#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		int n, w=0, dw=0;
		float a[1001], b[1001], c[1001], d[1001];
		cin>>n;
		for(int j=0;j<n;j++)
		{
			cin>>a[j];
			c[j]=a[j];
		}
		for(int j=0;j<n;j++)
		{
			cin>>b[j];
			d[j]=b[j];
		}
		sort(a,a+n);
		sort(b,b+n);
		int j=0;
		while(j<n)
		{
			int flag=0;
			for(int k=0;k<n;k++)
			{
				if(b[k]>a[j])
				{
					a[j]=b[k]=0;
					j++;
					flag=1;
					break;
				}
			}
			if(flag==0)
			{
				for(int j=0;j<n;j++)
				{
					if(a[j]!=0)
						w++;
				}
				break;
			}
		}
		sort(c,c+n);
		sort(d,d+n);
		dw=n;
		j=0;
		int k=0;
		while(j<n&&k<n)
		{
			if(c[j]<d[k])
			{
				dw--;
				j++;
			}
			else if(c[j]>d[k])
			{
				j++;
				k++;
			}
		}
		cout<<"Case #"<<i<<": "<<dw<<" "<<w<<endl;
	}
	return 0;
}
