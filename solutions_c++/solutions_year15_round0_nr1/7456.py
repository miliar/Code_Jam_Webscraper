#include<stdio.h>
#define INT_MAX 2147483646
#define INT_MIN -2147483645
#define max(a,b) (((a)>(b))?(a):(b))
#define min(a,b) (((a)<(b))?(a):(b))
#define ll long long
int main()
{
	int t,n,m,i,j,k,x,y,z,a,b,total,flag,ans,case_no;
	char A[1011];
	int count[1011];
	scanf("%d",&t);
	case_no=0;
	while(t--)
	{
		++case_no;
		scanf("%d",&n);
		scanf("%s",A);
		for(i=0;i<=n;i++)
		{
			count[i]=A[i]-'0';
		}
		total=count[0];
		ans=0;
		for(i=1;i<=n;i++)
		{
			if(total<i)
			{
				++ans;
				++total;
			}
			total+=count[i];
		}
		printf("Case #%d: %d\n",case_no,ans);
	}
	return 0;
}
