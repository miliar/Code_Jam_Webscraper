#include <iostream>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <climits>
#include <bitset>
#define N 1000000

int b[1000001];

using namespace std;

bitset<10> a;

int main()
{
	int i,j,p,q;
	
	for(i=1;i<=N;i++)
	{
		a.reset();
		for(j=1;j<N;j++)
		{
			p=i*j;
			q=p;
			while(1)
			{
				a[q%10]=1;
				q=q/10;
				if(q<=0)
					break;
			}
			if(a.all())
			{
				b[i]=p;
				break;
			}
		}
	}
	int t,n;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		cin>>n;
		cout<<"Case #"<<i<<": ";
		if(n)
		{
			cout<<b[n]<<endl;
		}
		else
		{
			cout<<"INSOMNIA"<<endl;
		}
	}

	return 0;
}
