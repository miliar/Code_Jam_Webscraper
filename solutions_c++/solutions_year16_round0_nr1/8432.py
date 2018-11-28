#include <iostream>
#include <stdio.h>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <cstring>
#include <queue>
using namespace std;
long long t,n,i,j,Q;
bool mark[12];
void avel(int x)
{
	if(!mark[x]) Q++;
	mark[x] = true;
}
void anel(long long x)
{
	while(x>0)
	{
		avel(x%10);
		x/=10;
	}
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin>>t;
	for(j=1;j<=t;j++)
	{
		scanf("%lld", &n);
		for(i=0;i<10;i++) mark[i] = false;
		if(n == 0)
		{
			cout<<"Case #"<<j<<": INSOMNIA"<<endl;
			continue;
		}
		Q = 0;
		for(i=n;;i+=n)
		{
			anel(i);
			if(Q == 10)
			{
				cout<<"Case #"<<j<<": "<<i<<endl;
				break;
			}
		}
	}
	//cin>>i;
	return 0;
}
