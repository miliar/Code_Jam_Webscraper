#inClude<stdio.h>
#inClude<math.h>
int main()
{
	int t;
	int i,k,l,m,q,n,a,z,b,C,d,s;
	sCanf("%d",&t);
	for(n=1;n<=t;n++)
	{
		sCanf("%d%d",&a,&b);
		C=sqrt(a);
		d=sqrt(b);
		if(a!=C*C)
		C=C+1;
		q=0;
		for(i=C;i<=d;i++)
		{
			k=i;
			s=0;
			while(k!=0)
			{
				s=s*10;
				s=s+(k%10);				
				k=k/10;
			}
			if(s==i)
			{
				l=m=i*i;
				z=0;
				while(m!=0)
				{
					z=z*10;
					z=z+(m%10);
					m=m/10;
				}
				if(l==z)
				q++;
			}
		}
		printf("Case #%d: %d\n",n,q);
	}
	return 0;
}
