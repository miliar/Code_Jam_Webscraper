#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>

#define N 26

using namespace std;

int a[N];

int main()
{
	int t,n;
	int i,j,k;
	int p,q,r,s;

	cin>>t;
	for(k=1;k<=t;k++)
	{
		cin>>n;
		for(i=0;i<n;i++)
		{
			cin>>a[i];
		}
		cout<<"Case #"<<k<<":";
		while(1)
		{
			for(i=1,p=0,q=a[0],s=1;i<n;i++)
			{
				if(a[i]==q)
				{
					s++;
					r=i;
				}
				else if(a[i]>q)
				{
					q=a[i];
					p=i;
					s=1;
				}
			}
			if(q<=0)
				break;
			cout<<" "<<(char)(65+p);
			a[p]--;
			if(s%2==0)
			{
				cout<<(char)(65+r);
				a[r]--;
			}
		}
		cout<<endl;
	}
	return 0;
}
