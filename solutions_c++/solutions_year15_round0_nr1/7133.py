#include <cstdio>
#include <cstring>
#include <algorithm>

char A[1000+7];

int main()
{
	//freopen("a.out","w",stdout);
	int T, Smax, tt=0;
 	scanf("%d", &T);
 	for (; T--; )
 	{
 		scanf("%d", &Smax);
 		scanf("%s", A);
 		int add=0;
 		int sum=0;
		for (int i=0; i<=Smax; i++)
			if (add+sum>=i)
			   sum+=A[i]-'0';
  			else add+=i-sum-add, sum+=A[i]-'0';
		printf("Case #%d: %d\n", ++tt, add);   
 	}
 	return 0;
}
