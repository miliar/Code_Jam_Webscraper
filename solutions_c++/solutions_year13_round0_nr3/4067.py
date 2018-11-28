#include<cstdio>
#include<algorithm>
using namespace std;

int s[30];
bool isOk(long long num)
{
	int point=0;
	while(num)
	{
		s[point++]=num%10;
		num/=10;
	}
	int left=0,right=point-1;
	while(left<right)
	{
		if(s[left]!=s[right])
			return false;
		left++;
		right--;
	}
	return true;
}

long long nums[10000000];

int main()
{	
	int cnt=0;
	long long tmp;
	for(int i=0;i<=10000000;i++)
	{
		if(isOk(i))
		{
			tmp=i;
			tmp*=tmp;
			if(isOk(tmp))
			{
				nums[cnt++]=tmp;
				//printf("%lld\n",tmp);
			}
		}
	}
	//printf("%d\n",cnt);
	int T,TT;
	scanf("%d",&T);
	TT=T;
	while(T--)
	{
		long long a,b;
		scanf("%lld%lld",&a,&b);
		int num=upper_bound(nums,nums+cnt,b)-lower_bound(nums,nums+cnt,a);
		printf("Case #%d: %d\n",TT-T,num);
	}
	return 0;
}