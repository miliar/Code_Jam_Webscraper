#include<bits/stdc++.h>
using namespace std;
int a[1005];
int main()
{
	int t,d,mx,m,tot;
	scanf("%d", &t);
	for(int i=1; i<=t; i++)
	{
		scanf("%d", &d);
		mx=-1;
		for(int j=0; j<d; j++)
		{
			scanf("%d", &a[j]);
			mx=max(mx, a[j]);
		}
		
		m=mx,tot=0;
		for(int j=1; j<=m; j++)
		{
			tot=j;
			for(int k=0; k<d; k++)
			{
				if(a[k]>j)
				{
					if(a[k]%j==0)
						tot+=((a[k]/j)-1);
					else
						tot+=a[k]/j;
				}
 
			}
			m=min(m, tot);	
		}
		printf("Case #%d: %d\n", i, m);
	}
	return 0;
}
