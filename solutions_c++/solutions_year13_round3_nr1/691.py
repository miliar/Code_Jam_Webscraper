#include <cstdio>
#include <cstring>
#include <algorithm>

const int MAXN = 1e6+10;

using namespace std;

char A[MAXN];
int N;

bool isvowel(char a)
{
	return a == 'a' or a == 'e' or a == 'i' or a =='o' or a =='u';
}

int main()
{
	int cas;
	scanf("%d",&cas);
	for(int num = 1 ; num <= cas ; num++)
	{
		scanf(" %s %d",A,&N);
		int len = strlen(A);
		int cnt = 0;
		long long can_start = 0;
		long long sol = 0;
		for(int c = 0 ; c < len ; c++)
		{
			if(isvowel(A[c]))
				cnt = 0;
			else
				cnt++;
			if(cnt >= N)
				can_start = c+2-N;
			sol += can_start;
			// printf("%d ", can_start);
		}
		// printf("\n");
		printf("Case #%d: %lld\n",num, sol);
	}
}