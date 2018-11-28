#include <cstdio>
#include <iostream>
#include <climits>
using namespace std;
void checknum(unsigned long long a, bool *chk)
{
	char num[65];
	sprintf(num,"%lld",a);
//	printf("%lld",a);
	int count =0;
	while(num[count] != '\0')
	{
		chk[(num[count]-'0')] = true;
		count++;
	}
	return;
}

int main(void)
{
	int T;
	cin >> T;
	for(int t=1; t <=T; t++)
	{
		bool chk[10]={false,};
		int n;
		unsigned long long i;
		scanf("%d",&n);
		unsigned long long num;
		if( n ==0 )
		{
			printf("Case #%d: INSOMNIA\n",t);
			continue;
		}

		for( i = 1; i< ULLONG_MAX; i++)
		{
				num = n*i;
				checknum(num,chk);
				int flag = 0;
				for(int j=0; j< 10; j++)
				{
					if( chk[j] )
						flag++;
				}
				if (flag == 10)
				{
					printf("Case #%d: %lld\n",t,num);
					break;
				}
		}
	}

}
