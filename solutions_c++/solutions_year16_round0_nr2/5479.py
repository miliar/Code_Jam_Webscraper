#include<bits/stdc++.h>

using namespace std;
int count_boundaries(char a[],int n)
{
	int b=0;
	for(int i=1;i<n;i++)
	{
		if(a[i]!=a[i-1])
			b++;
	}
	return b;
}
int main()
{
	int t,cs=0;
	int n,i;
	char a[200];
	scanf("%d",&t);
	while(t--)
	{	
		cs++;
		printf("Case #%d: ",cs);
		scanf("%s",a);
		n = strlen(a);
		if(a[n-1]=='-')
			printf("%d\n",count_boundaries(a,n)+1);
		else
			printf("%d\n",count_boundaries(a,n));


	}

	return 0;
}