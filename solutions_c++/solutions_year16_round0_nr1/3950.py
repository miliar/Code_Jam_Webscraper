#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
using namespace std;
typedef long long LL;
int f[12];
int n;
int main()
{
	int T;
	cin>>T;
	for(int ii=1;ii<=T;++ii)
	{
		printf("Case #%d: ",ii);
		scanf("%d",&n);
		if(n==0)
		{
			printf("INSOMNIA\n");
			continue;
		}
		int sum=0;
		bool flag=false;
		for(int i=1;i<=100;++i)
		{
			int num=i*n;
			while(num)
			{
				if(f[num%10]!=ii)
				{
					sum++;
					f[num%10]=ii;
				}
				num/=10;
				if(sum==10)
				{
					flag=true;
					break;
				}
			}
			if(flag) {printf("%d\n",i*n);break;}
		}
	}
	return 0;
}