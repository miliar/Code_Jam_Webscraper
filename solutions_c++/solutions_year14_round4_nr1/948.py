#include<bits/stdc++.h>
#define s(a) scanf("%d",&a)

using namespace std;
typedef long long int ll;
int inp[100005];
int main()
{
	int t,tt;
	s(t);
	for(tt=1;tt<=t;tt++)
	{
		int n,x,i;
		s(n);s(x);
		for(i=0;i<n;i++)
			s(inp[i]);
		sort(inp,inp+n);
		int res=0;
		int l=0,h=n-1;
		while(l<=h)
		{
			if(l==h)
			{
				res++;
				break;
			}
			if((inp[h]+inp[l])<=x)
			{
				res++;
				h--;
				l++;
			}
			else
			{
				h--;
				res++;
			}
		}
		printf("Case #%d: %d\n",tt,res);
	}
	return 0;
}
