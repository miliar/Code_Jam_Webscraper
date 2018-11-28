//By Toxyxer
#include <cstdio>

int ovation()
{
	char array[1001];
	int n, ovating=0, ret=0;
	
	scanf("%d", &n);
	scanf("%s", array);

	for(int i = 0; i <= n; i++)
	{
		if(ovating<i)
		{
			ret+=i-ovating;
			ovating=i;
		}
		ovating += array[i]-'0';
	}

	return ret;
}

int main()
{
	int T;
	scanf("%d", &T);
	
	for(int i = 1; i <= T; i++)
		printf("Case #%d: %d\n", i, ovation());
}