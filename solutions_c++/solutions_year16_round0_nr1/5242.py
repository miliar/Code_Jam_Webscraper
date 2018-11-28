#include <bits/stdc++.h>
int main()
{
	long long int t,k=0;
	scanf("%lld",&t);
	int *a = new int[10];
	while(k!=t)
	{
		long long int n,n1,n2,i=1,temp,j;
		scanf("%lld",&n);
		for(j=0;j<10;j++)
			a[j] = 0;
		if(n!=0)
		{
		while(true)
		{
			n1 = n*(i++);
			n2=n1;
			while(n1!=0)
			{
				temp = n1%10;
				n1 = n1/10;
				a[temp]=1;
			}
			for(j=0;j<10;j++)
				if(a[j]==0)
					break;
			if(j==10)
				break;
		}
		printf("Case #%lld: %lld \n",(k+1),n2);
	    }
		else
	       printf("Case #%lld:INSOMNIA \n", (k+1));
		k++;
	}
	return 0;
}
