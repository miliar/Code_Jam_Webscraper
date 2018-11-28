#include <cstdio>
#include <stdio.h>
#include <cstring>
using namespace std;
int a[10];
int main()
{
	freopen("A-large.in", "r", stdin);
    freopen("sample.out", "w", stdout);
    
	int n,num;
	scanf("%d",&n);
	for(int i=1;i<=n;i++)
	{
		scanf("%d",&num);
		if(num==0){printf("Case #%d: INSOMNIA\n",i);continue;}
		memset(a,0,sizeof(a));
		int cnt=10;
		for(int j=1;;j++)
		{
			int num1=num*j;
			while(num1)
			{
				int t=num1%10;
				if(!a[t]){a[t]=1;cnt--;}
				num1/=10;
			}
			if(!cnt){
				printf("Case #%d: %d\n",i,num*j);
				break;
			}
		}
	}
	return 0;
}