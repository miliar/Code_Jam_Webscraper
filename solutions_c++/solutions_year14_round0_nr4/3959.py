#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
	int t,n,y,z;
	float * a;
	float * b;
	cin >> t;
	for(int i=1;i<=t;i++)
	{
		y=0;
		z=0;
		cin >> n;
		a=new float[n];
		b=new float[n];
		for(int j=0;j<n;j++)
		{
			cin >> a[j];
		}
		for(int j=0;j<n;j++)
		{
			cin >> b[j];
		}
		sort(a,a+n);
		sort(b,b+n);
		for(int j=0,k=0;j<n;j++)
		{
			if(a[j]>b[k])
			{
				y++;
				k++;
			}
		}
		for(int j=0,k=0;j<n && k<n;k++)
		{
			if(a[j]<b[k])
			{
				j++;
			}
			z=n-j;
		}
		cout << "Case #" << i << ": " << y << " " << z << endl;
	}
	return 0;
}
