#include <cstdio>
#include <cstring>

using namespace std;

int main()
{
	int T , n , len , lastZindex , sum[100] = {0} , totalSum;
	char str[101];
	bool flag;
	scanf("%d" , &T);
	for(int a = 1 ; a<=T ; a++)
	{
		printf("Case #%d: " , a);
		scanf("%s %d" , str , &n);
		len = strlen(str);
		
		for(int i=0 ; i<len ; i++)
		{
			if(str[i] == 'a' || str[i] == 'e' || str[i] == 'i' || str[i] == 'o' || str[i] == 'u')
			{
				str[i] = '0';
			}
			else
			{
				str[i] = '1';
			}
		}
		totalSum = 0;
		for(int i=0 ; i<len ; i++)
		{
			lastZindex = i-1;
			flag = false;
			for(int j=i ; j<len ; j++)
			{
				if(str[j] == '1')
				{
					if( (j - lastZindex) >= n ) 
					{
						flag = true;
					}
				}
				else
				{
					lastZindex = j;
				}
				if(flag)
					totalSum++;
			}
		}
		printf("%d\n" , totalSum);
	}
	return 0;
}
