#include<cstdio>
#include<algorithm>
using namespace std;

int t, a, b, ile,dobre[5];

int main()
{
	scanf("%d", &t);
	for(int j = 1; j <= t; j++)
	{
		ile = 0;
		
		scanf("%d %d", &a, &b);
		dobre[1] = 1;
		dobre[2] = 4;
		dobre[3] = 9;
		dobre[4] = 121;
		dobre[5] = 484;
		
		for(int i = 1; i <= 5; i++)
			if(a <= dobre[i] && b >= dobre[i])
				ile++;
		
			printf("Case #%d: %d\n", j, ile);
	}

	return 0;
}	