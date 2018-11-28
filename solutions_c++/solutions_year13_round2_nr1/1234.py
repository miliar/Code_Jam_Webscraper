#include <stdio.h>
#include <algorithm>
using namespace std;

__int64 a[110];
int n;

bool cmp(__int64 x,__int64 y)
{
return x<y;
}


int main(int argc, char const *argv[])
{
	freopen("A-large.in","r",stdin);
	//freopen("A-large.txt","w",stdout);
	int t,cass=1;
	unsigned __int64 size;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%I64d %d",&size,&n);
		for (int i = 0; i < n; ++i)
			scanf("%I64d",&a[i]);
		sort(a,a+n,cmp);
		//for (int i = 0; i < n; ++i)
			//printf("%d\n",a[i] );
		int op=0,min=200;
		for (int i = 0; i < n; ++i)
		{
			if(size>a[i])
			{
				size+=a[i];
			}
			else
			{

				if(op+n-i<min)
					min=op+n-i;
				if(size==1)
					break;
				while(size<=a[i])
				{
					size=size+size-1;
					op++;
				}
				size+=a[i];
			}
		}
		if(op<min&&size!=1)
			min=op;
		printf("Case #%d: %d\n",cass++,min);
	}
	return 0;
}
