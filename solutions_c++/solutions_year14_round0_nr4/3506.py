#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<string>
#include <iomanip>
#include<cmath>
using namespace std;

double a[1015];
double b[1015];

int main()
{
	long long int n,k,i,cnt,t,j;
	//double c,f,x,t1,t2,t,r,ans;
	cin>>t;
	for(k=1;k<=t;k++)
	{
		cin>>n;
		cnt=0;
		for(i=0;i<n;i++)
			cin>>a[i];
		for(i=0;i<n;i++)
			cin>>b[i];
		sort(a,a+n);
		sort(b,b+n);
		
		i=0;	j=0;
		while(1)
		{
			if(a[i]>b[j])
			{
				cnt++;
				i++;
				j++;
			}
			else
				i++;
			if((i == n)||(j == n))
				break;
		}
		cout<<"Case #"<<k<<": "<<(cnt);
		cnt=0;
		i=0;	j=0;
		while(1)
		{
			if(a[i]<b[j])
			{
				cnt++;
				i++;
				j++;
			}
			else
				j++;
			if((i == n)||(j == n))
				break;
		}
		cout<<"  "<<(n-cnt)<<endl;
	}

}