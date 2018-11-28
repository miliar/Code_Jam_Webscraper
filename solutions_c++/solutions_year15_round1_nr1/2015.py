#include<bits/stdc++.h>
using namespace std;
#define int long long
int main(void)
{
	int T,c = 1;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&T);
	while(T--)
	{
		printf("Case #%d: ",c++);
		int N;
		cin>>N;
		int A[N+1];
		for(int i=0;i<N;i++)
			scanf("%d",&A[i]);
		int a = 0,b = 0,max2 = 0;
		for(int i=1;i<N;i++)
		{
			if(A[i] < A[i-1])
				a += (A[i-1]-A[i]);
			max2 = max(max2,A[i-1]-A[i]);
		}
		for(int i=0;i<N-1;i++)
		{
			if(A[i] >= max2)
				b += max2;
			else
				b += A[i];
		}
		printf("%d %d\n",a,b);
	}
	return 0;
}
