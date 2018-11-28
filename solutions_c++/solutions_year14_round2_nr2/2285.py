#include<iostream>
#include<cstdio>

using namespace std;

int main()
{
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("output.out", "w", stdout);
	
	int t, counter = 1, a,b, k, val, res, i, j;
	
	scanf("%d", &t);
	
	while(t--)
	{
		cin>>a>>b>>k;
		
		res = 0;
		for(i=0; i<a; i++)
		{
			for(j=0; j<b; j++)
			{
				val = i&j;
				if(val<k)
					res++;
			}
		}
		printf("Case #%d: ", counter++);
		printf("%d\n", res);				
	}
	
	
	return 0;
}
