#include<bits/stdc++.h>
using namespace std;

char S[1005];

int main()
{
	freopen("A-large.in","r",stdin);
	//freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	
	int T, k=0;
	scanf("%d",&T);
	while(T--)
	{
		k++;
		int N;
		scanf("%d",&N);N++;
		scanf("%s",S);
		int last = 0, ret = 0;
		
		for(int i=0; i<N; i++)
		{
			ret = max(ret, i-last);
			last += S[i] - '0';
		}
		printf("Case #%d: %d\n",k,ret);
	}
}
