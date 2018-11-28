
#include <stdio.h>


int main ()
{
	int i =0;
	int t = 0;
	unsigned long ar[100][3];
	for(i=0;i<2;i++)
  {
		ar[i][0]=0; ar[i][1]=0;ar[i][2]=0;
  }
	scanf("%d",&t);
	for(i=0;i <t; i++)
	{
		scanf("%lu %lu %lu",&ar[i][0],&ar[i][1],&ar[i][2]);
	 //cin>> ar[i][0]>>ar[i][1]>>ar[i][2];
	}
	 unsigned long ans = 0, c=0;
	 unsigned long j=0,d=0, a=0,b=0,k=0;

	for (i=0; i< t; i++)
	{
		a=ar[i][0]; b=ar[i][1]; k=ar[i][2];
		for(j=0;j<a;j++)
		{
			for(d=0;d<b;d++)
			{
				c = j & d;
				if( c < k )
				{
					ans++;
				}
				c=0;
			}
		}
		  //int z=i+1;
		printf("Case #%d: %lu\n",i+1,ans);

		//cout <<"Case #"<<z<<": "<<ans<<"\n";
		ans = 0;
	}

	return 0;
}