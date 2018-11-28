
#include<stdio.h>
int main()
{
	freopen("A-small-practice.in","rt",stdin);
	freopen("b.out","wt",stdout);
	int N;
	scanf("%d",&N);
	
	for (int ii = 0; ii < N; ++ii) 
	{
		int n, c;
		scanf("%d",&c);
		scanf("%d",&n);
		int arr[2010];
		printf("Case #%d: ",ii+1);
		for (int i = 0; i < n; ++i) {
			scanf("%d",arr+i);
			for (int j = 0; j < i; ++j) {
				if( arr[i]+arr[j] == c )
					printf("%d %d\n",j+1,i+1);
			}
		}
	}
	return 0;
}
