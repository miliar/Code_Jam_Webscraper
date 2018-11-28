#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <cassert>
#include <queue>
#include <iostream>
using namespace std;

#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define lb(x) ((x)&(-(x)))
#define ms(x,y) memset(x,y,sizeof(x))
typedef vector<int> VI;
typedef long long ll;
typedef pair<int,int> PI;
const ll mod=1000000007;
const int inf=0x20202020;
const int N=505;
//head

int a[106];
int main()
{
	freopen("C.in","w",stdout);
	printf("Case #1:\n");
	for(int i=0;i<500;i++)
	{
		int tmp=i,cnt=0;
		for(;tmp;tmp/=2)
			a[++cnt]=tmp%2;
		printf("1");
		for(int j=1;j<=cnt;j++)
			printf("%d",a[j]);
		for(int j=cnt+1;j<=15;j++)
			printf("0");
		for(int j=cnt+1;j<=15;j++)
			printf("0");
		for(int j=cnt;j>=1;j--)
			printf("%d",a[j]);
		printf("1");
		printf(" 3 2 5 2 7 2 3 2 11\n");
	}
	return 0;
}

