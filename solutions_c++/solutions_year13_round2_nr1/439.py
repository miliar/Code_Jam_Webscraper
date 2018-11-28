#include<stdio.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<sstream>
using namespace std;
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define inf 0xfffffff
typedef long long lld;
#define pi acos(-1.0)
#define eps 1e-8
lld a[110];
int main()
{
//	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int cas;
	scanf("%d",&cas);
	for(int cc=1;cc<=cas;cc++)
	{
		printf("Case #%d: ",cc);
		lld A;
		int n;
		cin >> A >> n;
		for(int i=0;i<n;i++)
			cin >> a[i];
		sort(a,a+n);
		int ans=n;
		if(A == 1)
			printf("%d\n",n);
		else
		{
			for(int j=n;j>0;j--)
			{
				int add=n-j;
				lld now=A;
				for(int i=0;i<j;i++)
				{
					while(now <= a[i])
					{
						add++;
						now+=now-1;
					}
					now+=a[i];
				}
				ans=min(ans,add);
			}
			printf("%d\n",ans);
		}
	}
	return 0;
}
/*
4
2 2
2 1
2 4
2 1 1 6
10 4
25 20 9 100
1 4
1 1 1 1

 */
