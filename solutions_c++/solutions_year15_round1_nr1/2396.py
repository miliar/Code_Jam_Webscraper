#include <cstdio>
#include <iostream>
using namespace std;
int main()
{
	int t,a[11111],i,n,T,sum1,sum2,maxdiff,maxi,diff;
	FILE * fr=fopen("A-large.in","r");
	FILE * fw=fopen("A.out","w");
	fscanf(fr,"%d",&t);
	T=t;
	while(t--)
	{
		cout<<endl;
		fscanf(fr,"%d",&n);
		for(i=0;i<n;i++)
		{
			fscanf(fr,"%d",&a[i]);
		}
		sum1=sum2=0;
		for(i=0;i<n-1;i++)
		{
			if(a[i]-a[i+1]>0)
				sum1+=a[i]-a[i+1];
		}
		maxdiff=a[0]-a[1];
		for(i=1;i<n-1;i++)
		{
			if(a[i]-a[i+1]>maxdiff)
				maxdiff=a[i]-a[i+1];
		}	
		if(maxdiff<0)
			maxdiff=0;
		for(i=0;i<n-1;i++)
		{
			diff=a[i]-a[i+1];
			if(diff>=maxdiff)
			{
				sum2+=maxdiff;
				cout<<sum2<<endl;
			}			
			else if(maxdiff!=0&&a[i]<=maxdiff)
			{
				sum2+=a[i];
				cout<<sum2<<endl;
			}
			else
			{
				sum2+=maxdiff;
				cout<<sum2<<endl;
			}
			//fprintf(fw, "%d\n",diff);
		}
		fprintf(fw, "Case #%d: %d %d\n",(T-t),sum1,sum2);
	}
	fclose(fr);
	fclose(fw);
}