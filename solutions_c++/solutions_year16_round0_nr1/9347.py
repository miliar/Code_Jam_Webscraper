#include <bits/stdc++.h>
#define ll long long
#define sz(a) a.size()
#define pb push_back
#define mp make_pair
#define srt(v) sort(v.begin(),v.end())
#define srtC(v,comp) sort(v.begin(),v.end(),comp)
#define FORI(i,x,n) for(int i=x;i<n;++i)
#define FORD(i,n) for(int i=n-1;i>=0;--i)

using namespace std;



int main()
{
	int T,N,count = 1;
		freopen("A-small-attempt0.in", "r", stdin);
		freopen("fileName.out", "w", stdout);
		scanf("%d",&T);
		while(T--)
		{
			scanf("%d",&N);
			if(N==0)
				printf("Case #%d: INSOMNIA\n",count);
			else
			{
				int k = 0;
				string found = "0000000000";
				while(++k)
				{
					int num = N*k;

					while(num>0)
					{
						found[num%10] = '1';
						num = num / 10;
					}
					if(found == "1111111111")
					{
						printf("Case #%d: %d\n",count,N*k);
						break;
					}
				}
			}
			++count;
		}


	return 0;
}
