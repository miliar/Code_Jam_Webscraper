#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;
#define MAXN 1100

int T;
int N;

int A[MAXN];
bool S[MAXN];


int main()
{
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    int i,j,k;
    scanf("%d",&T);
    for (int cases=1;cases<=T;cases++)
    {
		scanf("%d",&N);
		for (i=0;i<N;i++)
		{
			scanf("%d",&A[i]);
		}
    	memset(S,0,sizeof S);
    	int ans = 0;
    	for (i=0;i<N;i++)
    	{
    		int mina = (int)2e9;
    		for (j=0;j<N;j++)
    		{
    			if (!S[j] && A[j] < mina)
    			{ 
    				k = j;
    				mina = A[j];
    			}
    		}
    		int c0,c1;
    		c0 = c1 = 0;
    		for (j=0;j<k;j++)
				if (!S[j])
				{
					c0 ++;
				}
			for (j=k+1;j<N;j++)
				if (!S[j])
				{
					c1 ++;
				}
			ans += min(c0,c1);
			S[k] = 1;
    	}
    	printf("Case #%d: %d\n",cases,ans);
    }
    return 0;
}
