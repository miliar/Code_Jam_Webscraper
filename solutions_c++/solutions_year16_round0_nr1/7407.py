#include <cstdio>
#include <cstdlib>
int total, flag[10];
long long int temp, coef;

bool filled()
{
	for(int i=0; i < 10;i++)
		if(!flag[i])
			return false;
		return true;
}
int main()
{
	scanf("%d", &total);
	int num[total];
	for(int i = 0; i < total; i++)
		scanf("%d", &num[i]);
	for(int i = 0; i < total; i++)
	{
		if(num[i] == 0)
			printf("Case #%d: INSOMNIA\n",i+1);
		else
		{
			for(int j = 0; j < 10; j++)
				flag[j] = 0;
			coef = 0;
			while(!filled())
			{
				coef+=num[i];
				temp = coef;
				while(temp != 0)
				{
					flag[temp%10] = 1;
					temp /= 10;
				}
			}
			printf("Case #%d: %lld\n",i+1,coef);
		}
		
	}
}
