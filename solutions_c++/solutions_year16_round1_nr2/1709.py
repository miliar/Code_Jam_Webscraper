#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>

#define N 2501

using namespace std;

unsigned int a[N];
vector <int> b;

int main()
{
	int t,n,l;
	int i,j,k;
	int x;
	
	cin>>t;
	for(k=1;k<=t;k++)
	{
		cin>>n;
		l=(2*n-1)*n;
		memset(a,0,sizeof(a));
		for(i=0;i<l;i++)
		{
			cin>>x;
			a[x]++;
		}
		b.clear();
		for(i=1;i<N;i++)
		{
			if(a[i])
			{
				if(a[i]%2!=0)
				{
					b.push_back(i);
				}
			}
		}
		sort(b.begin(),b.end());
		cout<<"Case #"<<k<<": ";
		cout<<b[0];
		for(i=1;i<n;i++)
		{
			cout<<" "<<b[i];
		}
		cout<<endl;
	}

	return 0;
}
