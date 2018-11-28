#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
double a[1010];
int mra[1010];
double b[1010];
int mrb[1010];
int main()
{
	int tt,n;
	scanf("%d",&tt);
	for(int t=1;t<=tt;t++){
		memset(mra,0,sizeof(mra));
		memset(mrb,0,sizeof(mrb));
		scanf("%d",&n);
		for(int i=0;i<n;i++)
			scanf("%lf",&a[i]);
		for(int i=0;i<n;i++)
			scanf("%lf",&b[i]);
		sort(a,a+n);sort(b,b+n);
		int cnt = 0;
		for(int i=n-1 ; i>=0 ; i--)
		{
			double al = a[i];
			bool bb = false;
			if(!mra[i])
			{
				for(int j=n-1; j >= 0 ;j--)
				{
					double bl = b[j];
					if(!mrb[j])
					{
						if((al-bl) > 0)
						{
							mra[i]=1;
							mrb[j]=1;
							bb= true;
							cnt++;
							break;
						}
					}
				}
				//if(bb)
					//break;
			}
		}
		int cntt = 0;
		for(int i=0;i<n;i++)
		{
			if(!mra[i])
			{
				double al=a[i];
				bool bb = false;
				for(int j=n-1;j >=0;j--)
				{
					if(!mrb[j])
					{
						double bl = b[j];
						if( (al-bl) < 0)
						{
							mra[i]=mrb[j]=1;
							bb=true;
							cntt++;
							break;
						}
					}
				}
				//if(bb)
					//break;
			}
		}
		int ans = (cnt + (n-cnt-cntt));
		memset(mra,0,sizeof(mra));
		memset(mrb,0,sizeof(mrb));
		cnt=0;
		for(int i=0;i<n;i++)
		{
			if(!mra[i])
			{
				double al = a[i];
				bool bb = false;
				for(int j=0;j<n;j++)
				{
					if(!mrb[j])
					{
						double bl = b[j];
						if( (al-bl) <  0)
						{
							mra[i]=mrb[j]=1;
							cnt++;
							bb = true;
							break;
						}
					}
				}
			}
		}
		printf("Case #%d: ",t);
		printf("%d %d\n",ans,(n-cnt));
	}
	return 0;
}

		
