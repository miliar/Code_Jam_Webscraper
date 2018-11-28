#include <cstdio>

using namespace std;

bool isPal(int n)
{
	int nc = n;
	int digit , nr = 0;
	while(nc > 0)
	{
		digit = nc % 10;
		nr *= 10;
		nr += digit;
		nc /= 10;
//		printf("%d\n" , nr);
	}
	if(n == nr)
		return true;
	return false;
}

int main()
{
	int T , A , B , i , count , temp;
	bool fair[1001] = {0};
//	if(isPal(123))
//		printf("pass\n");
	for(i=0 ; i<35 ; i++)
	{
		if(!isPal(i))
			continue;
		temp = i*i;
		if(temp < 1001)
		{
			if(isPal(temp))
				fair[temp] = true;
		}
	}
	scanf("%d" , &T);
	for(int a =1 ; a<=T ; a++)
	{
		printf("Case #%d: " , a);
		scanf("%d %d" , &A , &B);
		count = 0;
		for(i=A ; i<=B ; i++)
		{
			if(fair[i])
			{
				count++;
//				printf("%d " , i);
			}
		}
		printf("%d\n" , count);
	}

	return 0;
}
