#include <stdio.h>

int a[20100];
int tempa[20100];
void mergesort(int *a ,int n1 ,int n2);
int main(void)
{
	int t ,i;
	int n ,x ,j ,j2;
	int ans;
	
	scanf("%d" ,&t);
	for (i=1 ; i<=t ; i++)
	{
		ans=0;
		scanf("%d %d" ,&n ,&x);
		for (j=1 ; j<=n ; j++)
		{
			scanf("%d" ,&a[j]);
		}
		mergesort(a,1,n);
		for (j=n , j2=1 ; j>=j2 ;)
		{
			if (j==j2)
			{
				ans++;
				break;	
			}
			if (a[j]+a[j2]<=x)
			{
				j--;
				j2++;
				ans++;
			}
			else
			{
				j--;
				ans++;								
			}
		}
		printf("Case #%d: %d\n" ,i ,ans);
	}

	return 0;
}

void mergesort(int *a ,int n1 ,int n2)
{
	int a1 ,a2 ,n12;
	int i ,j;
	
	if (n1<n2)
	{	
		n12=(n1+n2)/2;
		mergesort(a,n1,n12);
		mergesort(a,n12+1,n2);
		for (i=n1 ; i<=n2 ; i++)
		{
			tempa[i]=a[i];	
		}
		a1=n1;
		a2=n12+1;
		for (i=n1 ; (a1<=n12 && a2<=n2) ;i++)
		{
			if (tempa[a1]<=tempa[a2])
			{
				a[i]=tempa[a1];
				a1++;
			}
			else
			{
				a[i]=tempa[a2];
				a2++;				
			}
		}
		if (a1>n12)
		{
			for (j=a2 ; j<=n2 ; j++ , i++)
			{
				a[i]=tempa[j];
			}
		}
		else
		{
			for (j=a1 ; j<=n12 ; j++ , i++)
			{
				a[i]=tempa[j];
			}			
		}
	}
}
