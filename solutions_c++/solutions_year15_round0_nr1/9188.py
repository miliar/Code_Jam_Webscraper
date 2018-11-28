#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("file_large.txt", "w", stdout);
	int t,test;
	scanf("%d",&t);
	test = t;
	while(t--)
	{
		int smax=0, digit =0, sum_digit=0;
		int j=0, counter=0;
		char arr[1002];
		scanf("%d %s",&smax,arr);
		for(j=0;j<strlen(arr);j++)
		{
			digit = (arr[j]-'0');
			//printf("%d\n", digit);
			sum_digit = sum_digit + digit;
			if(sum_digit<(j+1)) 
			{
				counter = counter + ((j+1)-sum_digit);
				sum_digit = sum_digit + ((j+1)-sum_digit);
			}
			if(sum_digit >= smax) break;
		}
		printf("Case #%d: %d\n", (test-t),counter);
	}
	return 0;
}