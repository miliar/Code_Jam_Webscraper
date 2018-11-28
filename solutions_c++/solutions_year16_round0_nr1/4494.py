#include<iostream>
#include<cstdio>
#include<cstring>

using namespace std;

int main()
{
	long long int test;
	bool used[10];
	while(scanf("%lld",&test) != EOF)
	{
		for(int i=0;i<test;++i)
		{
			memset(used,false,sizeof(used));
			long long int number,answer;
			scanf("%lld",&number);
			bool check;

			for(int j=1;j<300;++j)
			{
				long long int now = j * number;
				check = true;
				while(now > 0)
				{
					int temp = now%10;
					now = now / 10;
					used[temp] = true;
				}
				for(int k=0;k<10;++k)
				{
					if(used[k] == false)
					{
						check = false;
						break;
					}
				}
				if(check == true)
				{
					printf("Case #%d: %lld\n",i+1,j*number);
					break;
				}
			}
			if(check == false)
				printf("Case #%d: INSOMNIA\n",i+1);
		}
	}
	return 0;
}
