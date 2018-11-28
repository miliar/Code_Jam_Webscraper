#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;
int main()
{
	int t;
	long long a,b,c,temp,ans;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		scanf("%lld",&a);
		scanf("%lld",&b);	
		scanf("%lld",&c);
		if(a<b)
		{
			temp=a;
			a=b;
			b=temp;
		}
		if(b<=c)
		{
			ans=a*b;
		}
		else
		{
			ans=a*c;
			int b2[32]={0},p,pos=0,g,end=-1;
			temp=c-1;
			p=0;
			/*while(temp)
			{
				if(temp&1)
				{
					b2[p]=1;
					pos=p;
					if(end==-1)
					end=p;
				}
				temp=temp/2;
				p++;
			}*/
			//printf("pos: %d end: %d\n",pos,end);
			for(long long j=c;j<b;j++)
			{
				ans++;
				for(long long r=1;r<a;r++)
				{
					if((j&r)<c)
					ans++;
				}
				/*int b1[32]={0};
				long long t2=j,t3=a-1;
				p=0;
				g=0;
				int len=0;
				while(t3)
				{
					len++;
					t3=t3/2;
				}
				while(t2)
				{
					if(t2&1)
					{
						b1[p]=1;
						if(p>=pos)
						g++;
					}
					p++;
					t2=t2/2;
				}
				printf("ans: %lld\n",ans);
				ans=ans+pow(2,len-g);
				printf("ans: %lld\n",ans);
				if(b1[pos]==1)
				{
					int count=0;
					for(int k=pos-1;k>=p;k--)
					{		
						if(b1[k]==1)
						count++;
					}
					ans=ans+pow(2,len-g-count);
				}
				printf("ans: %lld\n",ans);*/
			}
		}
		printf("Case #%d: %lld\n",i,ans);
	}
	return 0;
}
