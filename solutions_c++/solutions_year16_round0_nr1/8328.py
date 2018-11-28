#include<bits/stdc++.h>
using namespace std;
int tc,n,f,arr[15],y;
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large-output.txt","w",stdout);
	scanf("%d",&tc);
	for(int a=1;a<=tc;a++)
	{
		memset(arr,0,sizeof(arr));
		scanf("%d",&n);
		if(n==0)
		{
			printf("Case #%d: INSOMNIA\n",a);
		}
		else if(n==1)
		{
			printf("Case #%d: 10\n",a);
		}
		else
		{
			int l=0;
			for(int b=1;b<=100;b++)
			{
				f=b*n;
				y=f;
				int d=10,e,g,h,i,bagi,mod;
				for(int c=1;c<=20;c++)
				{
					if(f/10==0 && f%10==0)
					{
						//printf("halo");
						break;
					}
					e=f%10;
					if(arr[e]==0)
					{
						arr[e]=1;
						l++;
						//printf("%d %d %d\n",b,c,e);
					}
					f=f/10;
					//printf("%d %d\n",c,f);
					//d=d*10;
				}
				if(l==10)
				{
					break;
				}
			}
			
			printf("Case #%d: %d\n",a,y);
		}
	}
}
