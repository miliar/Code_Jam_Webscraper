#include<bits/stdc++.h>
using namespace std;
int main()
{
	short int t,cnt=0,cont,contt,p,q,n,i,m;
	float a[100],b[100],z;
	cin>>t;
	while(t--)
	{
		cnt++;
		cont=0;contt=0;
		cin>>n;
		for(i=0;i<n;i++)
		cin>>a[i];
		for(i=0;i<n;i++)
		cin>>b[i];
		sort(a,a+n);
		sort(b,b+n);
		/*for(i=0;i<n;i++)
			printf("%f ",a[i]);
		printf("\n");
		for(i=0;i<n;i++)
			printf("%f ",b[i]);*/
		//z=b[0];
		p=0;q=0;
		for(i=0;i<n;i++)
		{
			if(b[p]<a[i])
			{
				cont++;
				p++;
			}
		}
		p=n-1;
		q=0;
		m=n-1;
		for(i=n-1;i>=0;i--)
		{
			if(a[i]>b[m])
			contt++;
			else
			m--;
		}
		printf("Case #%hd: %hd %hd\n",cnt,cont,contt);
	}
	return 0;
}
