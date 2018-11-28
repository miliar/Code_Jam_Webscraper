#include<cstdio>
#include<cstring>
using namespace std;

int arr[10];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	
	int cases;
	scanf("%d",&cases);
	int count=0;
	while(cases--)
	{
		long long int num;
		scanf("%lld",&num);
		if(num == 0) {printf("Case #%d: INSOMNIA\n",++count);continue;}
		
		long long int num2=num;
		int times=1;
		char s[30];
		memset(s, 0, sizeof(s));
		memset(arr, 0, sizeof(arr));
		while(1)
		{
			num2 = num*times;
			times++;
			sprintf(s,"%lld",num2);
			int n=strlen(s);
			for(int i=0;i<n;i++)
			{
				arr[s[i]-'0']=1;
			}
			int flag=1;
			for(int i=0;i<10;i++)
			{
				if(arr[i]) continue;
				else {flag = 0; break;}
			}

			if(flag)
			{
				printf("Case #%d: %lld\n",++count,num2);
				break;
			}
		}

	}
		
	return 0;

}
