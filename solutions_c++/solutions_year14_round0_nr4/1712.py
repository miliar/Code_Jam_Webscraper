#include<cstdio>
#include<iostream>
#include <algorithm>

using namespace std;

int main()
{
	int t, T;
	cin>>T;

	for(t=1;t<=T;t++)
	{
		int n, i;
		cin>>n;

		double Ar1[n], Ar2[n];

		for(i=0;i<n;i++)
			cin>>Ar1[i];

		for(i=0;i<n;i++)
			cin>>Ar2[i];

		sort(Ar1, Ar1+n);
		sort(Ar2, Ar2+n);

		int p1=0, p2=0;
		int count1=0, count2=0;
		
		while(p1<n && p2<n)
		{
			if(Ar1[p1]>Ar2[p2])
			{
				count1++;
				p2++;
			}
			else
			{
				p1++;
				p2++;
			}
		}
		
		p1=0;
		p2=0;
		
		while(p1<n && p2<n)
		{
			if(Ar2[p2]>Ar1[p1])
			{
				count2++;
				p1++;
			}
			else
			{
				p2++;
				p1++;
			}
		}
		
//		cout<<t<<" : War : "<<count1<<" : "<<n-count2<<endl;
		cout<<"Case #"<<t<<": "<<n-count2<<" "<<count1<<endl;

	}
	
	
	return 0;
}
