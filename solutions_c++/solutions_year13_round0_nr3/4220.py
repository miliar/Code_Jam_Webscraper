#include <stdio.h>

int n = 39;
__int64 num[39] = {1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 
1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 
400080004, 404090404, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004, 
1000002000001, 1002003002001, 1004006004001, 1020304030201, 1022325232201, 1024348434201, 
1210024200121, 1212225222121, 1214428244121, 1232346432321, 1234567654321, 4000008000004, 4004009004004};


int main()
{
	freopen("C-large-1.in", "r", stdin);
	freopen("C-large-1.out", "w", stdout);

	//=========code segment
	int T;
	__int64 A, B;
	int i, j;
	int start, end;
	int ans;

	scanf("%d", &T);
	for (i=0; i<T; i++)
	{
		int start, end;
		scanf("%I64d %I64d", &A, &B);
		
		start = 0;

		for (j=0; j<n && num[j]<A; j++) ;
		start = j;  // the first number (num[j])>=A   or j==n(all the number less than A)
		
		for (end=start; j<n && num[j]<=B; j++) ;
		end = j-1;    // the first number(num[j])>B
		
		ans = end - start + 1;
		printf("Case #%d: %d\n", i+1, ans);
	}

	//============================
	fclose(stdin);
	fclose(stdout);
	return 0;
}