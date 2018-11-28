#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <iostream>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
using namespace std;

typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;

#define PB push_back
#define MP make_pair
#define clr(a,b)	(memset(a,b,sizeof(a)))
#define rep(i,a)	for(int i=0; i<(int)a.size(); i++)

const int INF = 0x3f3f3f3f;
const double eps = 1E-8;

int a[4][4],b[4][4];
int a1,b1,T;

int main()
{
//	freopen("D:\\in.txt","r",stdin);
	freopen("D:\\A-small-attempt0.in","r",stdin);
	freopen("D:\\out.txt","w",stdout);
	int cas = 1;
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d",&a1);
		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++)
				scanf("%d",&a[i][j]);

		scanf("%d",&b1);
		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++)
				scanf("%d",&b[i][j]);

		int cnt = 0;
		int ans = 0;
		for(int j=0; j<4; j++)
		{
			int num = a[a1-1][j];

			int fg = 0;
			for(int k=0; k<4; k++)
				if(b[b1-1][k] == num)
					fg = 1;

			if(fg)
			{
				cnt++;
				ans = num;
			}
		}

		printf("Case #%d: ",cas++);
		if(cnt == 0)	puts("Volunteer cheated!");
		else if(cnt == 1)	printf("%d\n",ans);
		else	puts("Bad magician!");
	}


	return 0;
}
