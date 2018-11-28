#include<bits/stdc++.h>
using namespace std;
int main(void)
{
	freopen("SO.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T,N;
	char S[1100];
	scanf("%d",&T);
	int c = 1;
	while(T--)
	{
		long long count = 0,people = 0;
		scanf("%d %s",&N,S);
		for(int i=0;i<=N;i++)
		{
			if(count < i)
			{
				people += i-count;
				count += i-count;
			}
			count += (S[i]-'0');
		}
		printf("Case #%d: %lld\n",c++,people);
	}
	return 0;
}
				
