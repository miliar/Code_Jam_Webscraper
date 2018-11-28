#include <iostream>
#include <queue>
#include <vector>
#include <map>
#include <cmath>
#include <cstring>
#include <string>
#include <set>
#include <algorithm>
#include <stack>
#include <deque>
#define MAX 1000000000
#define eps 1e-10
using namespace std;

bool mark[10];

bool gao(long long x)
{
	while(x)
	{
		mark[x%10]=true;
		x/=10;
	}
	for(int i=0;i<10;i++)
	if(!mark[i])
	return false;
	return true;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	
	int re;
	cin>>re;
	
	for(int cases = 1;cases<=re;cases++)
	{
		long long x,tmp;
		cin>>x;
		tmp = x;
		if(x==0)
		{
			printf("Case #%d: INSOMNIA\n",cases);
			continue;
		}
		memset(mark,0,sizeof(mark));
		
		while(true)
		{
			if(gao(x))
			{
				printf("Case #%d: %lld\n",cases,x);
				break;
			}
			x+=tmp;
		}
		
		
	}
	
	
}
	