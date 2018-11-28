#include<stdio.h>
#include<algorithm>

using namespace std;


int main()
{
	int t,l=0;
	scanf("%d",&t);
	while(t--)
	{
		l++;
		int n,i,j;
		double a[15],b[15];
		scanf("%d",&n);
		for(i=0;i<n;i++)
		scanf("%lf",&a[i]);
		for(i=0;i<n;i++)
		scanf("%lf",&b[i]);
		sort(a,a+n);
		sort(b,b+n);
		j=0;
		int cnt=0;
		for(i=0;i<n;i++)
		{
			if(a[i]>b[j])
			{
			cnt++;
			j++;
		    }
		}
	//	printf("%d\n",cnt);
		j=n-1;
		int ptr=n;
    for(i=n-1;i>=0;i--)
    {
       if(a[i]<b[j])
	   {
	   	j--;
	   	ptr--;
	   }	
    }
    
  // ptr=n-i;
//	printf("%d  %d\n",cnt,n-i);
    printf("Case #%d: %d %d\n",l,cnt,ptr);	
	}
	return 0;
}
