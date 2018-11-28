#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <cstring>
#define SIZE 1005

using namespace std;

char A[SIZE];

int main()
{
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		printf("Case #%d: ",t);
		scanf("%s",&A);
		int n=strlen(A);
		int K;
		scanf("%d",&K);
		int cnt=0;
		for(int i=0;i+K<=n;i++)
		{
			if(A[i]=='-')
			{
				cnt++;
				for(int j=i;j<i+K;j++)
				{
					if(A[j]=='+') A[j]='-';
					else A[j]='+';
				}
			}
		}
		for(int i=0;i<n;i++) if(A[i]=='-') cnt=-1;
		if(cnt>=0) printf("%d\n",cnt);
		else puts("IMPOSSIBLE");
	}
	return 0;
}
