#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
	long long n,post;
	scanf("%lld",&n);
	for(int j=1;j<=n;j++)
	{
		long long a;
		bool arr[11]={0};
		scanf("%lld",&a);
		long long flag=0,i,count=0;post=0;
		for(i=1;!flag;i++)
		{
			post=post+a;
			if(a==0)
				break;
			long long hey,num=post;
			while(num!=0)
			{
				hey=num%10;
				num/=10;
				if(!arr[hey]){
					count++;arr[hey]=1;
				}
			}
			if(count==10){
				flag=1;
			}
		}
		if(flag)
			printf("Case #%d: %lld\n",j,post);
		else
			printf("Case #%d: INSOMNIA\n",j);
	}
	return 0;
}