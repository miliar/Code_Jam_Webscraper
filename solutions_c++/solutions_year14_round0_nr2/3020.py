#include <cstdio>
#include <iostream>
using namespace std;

int t, n;
double c, f, x, prev, cur;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("b.out","w",stdout);
	scanf("%d",&t);
	for(int k=1; k<=t; k++)
	{
		n=0;
		cin>>c>>f>>x;
		prev=x;
		cur=x/2.0;
		while(cur<prev)
		{
			n++;
			prev=cur;
			cur=0.0;
			for(int i=0; i<n; i++)
			{
				cur+=(c/((f*i)+2.0));
			}
			cur+=(x/((f*n)+2.0));
		}
		printf("Case #%d: %f\n",k,prev);
	}

}
