#include<algorithm>
#include<iostream>
#include<stdio.h>
#include<math.h>

using namespace std;

int main()
{
	int t,d,a[1010],temp,tot;
	int spm,m,ind=0,ans=0;
	scanf("%d",&t);
	while(t--)
	{
		ind++;
		scanf("%d",&d);
		for(int i=0;i<=1000;i++)	a[i]=0;
		for(int i=0;i<d;i++)
		{
			scanf("%d",&temp);
			a[temp]++;
		}
		spm=m=0;
		/* wont work for 9-->5 and 26-->2
		for(int i=1000;i>=1;i--)
		{
			if(a[i]>0)
			{
				ans=min(ans,i+spm);
				spm+=a[i];
				a[i/2]+=a[i];
				a[i-i/2]+=a[i];
			}
		}*/
		tot=0;
		ans=1000;
		for(int j=1;j<=1000;j++)
        {
            tot=0;
            for(int i=j+1;i<=1000;i++)
		    {
		        temp=i/j;
		        if(i%j==0)  temp--;
		        tot+=a[i]*temp;
		    }
		    tot+=j;
		    if(ans>tot) ans=tot;
		}
		printf("Case #%d: %d\n",ind,ans);
	}
	return 0;
}
