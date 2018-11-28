#include <stdio.h>

char s[10100];
int main(void)
{
	int tt ,ii ,i ,j ,jj ,j2 ,j3 ,j4; 
	int n ,r ,p ,ss;
	int tr ,tp ,ts;
	int ans;
	int e ,m;
	int z;
	char tempc;
	
	scanf("%d" ,&tt);
	for (ii=1 ; ii<=tt ; ii++)
	{
		printf("Case #%d: " ,ii);
		scanf("%d %d %d %D" ,&n ,&r ,&p ,&ss);
		ans=1;
		while (r+p+ss>1)
		{
			if (r+p<ss||r+ss<p||p+ss<r)
			{
				ans=0;
				break;
			}
			ts=((p+ss)-r)/2;
			tp=p-ts;
			tr=r-tp;
			r=tr;
			p=tp;
			ss=ts;
		}
		if (ans==0)
		{
			printf("IMPOSSIBLE\n");
			continue;
		}
		if (r==1)
		{
			s[0]='R';
		}
		else if (p==1)
		{
			s[0]='P';			
		}
		else 
		{
			s[0]='S';						
		}
		for (i=1 ; i<=n ; i++)
		{
			jj=1<<(i-1);
			for (j=jj-1 ; j>=0 ; j--)
			{
				if (s[j]=='R')
				{
					s[j+j]='R';
					s[j+j+1]='S';
				}
				if (s[j]=='P')
				{
					s[j+j]='P';
					s[j+j+1]='R';
				}			
				if (s[j]=='S')
				{
					s[j+j]='P';
					s[j+j+1]='S';
				}	
			}
		}
		m=1<<n;
		e=1<<(n-1);
		for (i=2 ; i<=e ; i<<=1)
		{
			for (j=0 ; j<m ; j+=(i+i))
			{
				j2=j+i;
				z=0;
				for (j3=j , j4=j2 ; j3<j2 ; j3++ , j4++)
				{
					if (s[j4]<s[j3])
					{
						z=1;
						break;	
					}
					if (s[j3]<s[j4])
					{
						break;	
					}
				}
				if (z)
				{
					for (j3=j , j4=j2 ; j3<j2 ; j3++ , j4++)
					{
						tempc=s[j3];
						s[j3]=s[j4];
						s[j4]=tempc;
					}
				}
			}
		}
		
		
		jj=1<<n;
		for (j=0 ; j<jj ; j++)
		{
			printf("%c" ,s[j]);	
		}
		printf("\n");
	}
	
	return 0;
}
