# include <cstdio>
# define gc() getchar()

inline int scan()
{
	int n = 0;
	char c = gc();
	while(c < '0' || c > '9')
	c = gc();
	while(c >= '0' && c <= '9')
	{
		n = n * 10 + c - '0';
		c = gc();
	}
	return n;
}


int main()
{
	int T = scan();
	int S;
	int c = 0;
	long long int sum, friends;
	while(T--)
	{
		c++;
		S = scan();
		char arr[S+1];
		scanf("%s",arr);
		sum = 0;
		friends = 0;
		if(S == 0)
		printf("Case #%d: 0\n",c);
		else
		{
			int i = 0;
			sum = arr[0] - '0';
			for(i = 1 ; i <= S ; i++)
			{
				if(sum < i)
				{
					friends += i - sum;
					sum += i - sum + arr[i] - '0';
				}
				else
				sum += arr[i] - '0';
			}
			printf("Case #%d: %d\n",c,friends);
		}
	}
	return 0;
}