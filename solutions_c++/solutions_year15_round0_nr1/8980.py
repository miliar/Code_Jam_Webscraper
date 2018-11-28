#include <iostream>
#include <cstdio>

using namespace std;
/*
5
4 11111
1 09
5 110011
0 1
5 600001

*/
int main()
{
freopen("A-large.in","r",stdin);
freopen("A-large.out","w",stdout);

	int N,T;scanf("%d",&T);
	for(int t=0;t<T;++t)
	{
		scanf("%d",&N);
		int sit, stand , f=0;
		string s;
		cin>>s;
		stand = (s[0]-'0');
		for(int i=1;i<=N;++i)
		{
			if(s[i]=='0') continue;
			sit = s[i]-'0';
			if(stand>=i) stand+=sit;
			else
			{
				f+=(i-stand);
				stand+=(i-stand+(sit));
			}
		}
		printf("Case #%d: %d\n",t+1,f);
	}

	return 0;
}