#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<math.h>
using namespace std;
long long poww[10];
long long ans[100010];
int end;
void precal()
{
	long long middle;
	ans[end++]=0;
	ans[end++]=1;
	ans[end++]=2;
	ans[end++]=3;
	for(long long len=2;len<=6;len++)
	{
		if(len%2==1)
		{
			middle=(len+1)/2;
			//200010002
			ans[end++]=poww[middle-1]+poww[len-1]*2+2;
			//10000200001
			ans[end++]=poww[middle-1]*2+1+poww[len-1];
			for(int i=2;i<middle;i++)
			{
				ans[end++]=poww[len-1]+1+poww[i-1]+poww[len-i]+poww[i-1]+poww[middle-1]*2;
			}
			//10001000200010001
			ans[end++]=poww[len-1]+1+poww[middle-1];
			//10000100001
			for(int i=2;i<middle;i++)
			{
				ans[end++]=poww[len-1]+1+poww[i-1]+poww[len-i]+poww[middle-1];
			}
			//101010101
			for(int i=2;i<middle;i++)
			{
				for(int j=i+1;j<middle;j++)
				{
					ans[end++]=poww[len-1]+1+poww[i-1]+poww[len-i]+poww[middle-1]+poww[j-1]+poww[len-j];
				}
			}
			//1010101010101
			for(int i=2;i<middle;i++)
			{
				for(int j=i+1;j<middle;j++)
				{
					for(int k=j+1;k<middle;k++)
						ans[end++]=poww[len-1]+1+poww[i-1]+poww[len-i]+poww[middle-1]+poww[j-1]+poww[len-j]+poww[k-1]+poww[len-k];
				}
			}
			//1  1   1  1  1  1 1 1 1
		}
		ans[end++]=poww[len-1]*2+2;
		//2000002
		ans[end++]=poww[len-1]+1;
		//1000001
		middle=len/2;
		for(int i=2;i<middle;i++)
		{
			ans[end++]=poww[len-1]+1+poww[i-1]+poww[len-i];
		}
		//1010000101
		for(int i=2;i<middle;i++)
			{
				for(int j=i+1;j<middle;j++)
				{
					ans[end++]=poww[len-1]+1+poww[i-1]+poww[len-i]+poww[j-1]+poww[len-j];
				}
			}
		//101010000010101
		for(int i=2;i<middle;i++)
			{
				for(int j=i+1;j<middle;j++)
				{
					for(int k=j+1;k<middle;k++)
						ans[end++]=poww[len-1]+1+poww[i-1]+poww[len-i]+poww[j-1]+poww[len-j]+poww[k-1]+poww[len-k];
				}
			}
		//1  1   1  1  1  1 1 1 1
	}
	return;
}
main()
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	long long a,b,aaa,bbb;
	int aa,bb;
	poww[0]=1;
	for(int i=1;i<=8;i++) poww[i]=poww[i-1]*10;
	precal();
	sort(ans,ans+end);
	//cout << end << endl;
	//for(int i=0;i<20;i++) cout << ans[i] << " ";
	int t;
	scanf("%d\n",&t);
	for(int ll=0;ll<t;ll++)
	{
		printf("Case #%d: ",ll+1);
		scanf("%lld %lld",&a,&b);
		//A=sqrt(a);B=sqrt(b);
		aaa=(long long)sqrt((double)a);
		bbb=(long long)sqrt((double)b);
		if(aaa*aaa==a) aaa--;
		//cout << "-----" << aaa << " " << bbb << endl;
		//printf("%lld\n",f(b)-f(a));
		bb=upper_bound(ans,ans+end,bbb)-ans-1;
		aa=upper_bound(ans,ans+end,aaa)-ans-1;
		printf("%d\n",bb-aa);
	}
}
