#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>

using namespace std;

const int N = 20001;
char s[N];
int a[N];

int code(char c)
{
	return c-'i'+1;
}

// 0 1
// 1 i
// 2 j
// 3 k
// 4 -1
// 5 -i
// 6 -j
// 7 -k

int g[8][8] = {{0,1,2,3,4,5,6,7},{1,4,3,6,5,0,7,2},{2,7,4,1,6,3,0,5},{3,2,5,4,7,6,1,0},
{4,5,6,7,0,1,2,3},{5,0,7,2,1,4,3,6},{6,3,0,5,2,7,4,1},{7,6,1,0,3,2,5,4}};

void solve()
{
	int l, x;
	scanf("%d%d", &l, &x);
	
	scanf("%s", s);

	int n = l*x;
	for(int i=l;i<n;i++)
	{
		s[i] = s[i%l];
	}

	for(int i=0;i<n;i++)
	{
		a[i] = code(s[i]);
	}

	int curr1 = 0;
	int i1=0;
	for(;i1<n;i1++)
	{
		curr1 = g[curr1][a[i1]];
		if(curr1 == 1)
			break;
	}
	
	int curr2 = 0;
	int i2=n-1;
	for(;i2>=0;i2--)
	{
		curr2 = g[a[i2]][curr2];
		if(curr2 == 3)
			break;
	}

	if(i1<n && i2>=0)
	{
		int mid = 0;
		for(int i=i1+1;i<i2;i++)
		{
			mid = g[mid][a[i]];
		}
		if(mid==2)
		{
			printf("YES\n");
		}
		else
		{
			printf("NO\n");
		}
	}
	else
	{
		printf("NO\n");
	}
}

int main()
{
	freopen("C-small.in", "r", stdin);
	freopen("C-small.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int tst=0;tst<t;tst++)
	{
		printf("Case #%d: ", tst+1);
		solve();
	}
	return 0;
}