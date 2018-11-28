//nathanajah's template
//28-11-2012
#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <math.h>
#include <string>
#include <string.h>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <set>
#include <deque>
#include <map>
#include <ctime>
#define ii pair<int,int>
#define vi vector<int>
#define vii vector<ii>
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define LL long long
#define ULL unsigned LL
#define INF 0x3FFFFFFF
#define INFLL 0x3FFFFFFFFFFFFFFF
#define SZ(a) (int)(a).size()
#define ALL(a) (a).begin(),(a).end()
#ifdef DEBUG
	#define debug(...) \
	fprintf(stderr,__VA_ARGS__)
#else
	#define debug(...) 
#endif
using namespace std;

inline string GetString()
{
	char GS[1000005];
	scanf("%s",GS);string ret=GS;
	return ret;
}

inline char getc()
{
	char c=' ';
	while (c==' ' || c=='\t' || c=='\r' || c=='\n')
		c=getchar();
	return c;
}
//ENDOFTEMPLATE

int t,n,x;
int arr[100005];
int i,j;
int main()
{
	scanf("%d",&t);
	int cs = 0;
	while (t--)  {
		scanf("%d %d",&n,&x);
		memset(arr,0,sizeof(arr));
		int ans = 0;
		for (i=0;i<n; ++i) {
			int tmp;
			scanf("%d",&tmp);
			arr[tmp]++;
		}
		for (i=700;i>=0;--i) {
			if (2*i <= x) {
				int kurang = arr[i]/2;
				arr[i] -= 2*kurang;
				ans += kurang;
			}
			for (j=i-1;j>=0;--j) {
				if (i+j <=x) {
					int kurang = min(arr[i],arr[j]);
					arr[i] -= kurang;
					arr[j] -= kurang;
					ans += kurang;
				}
			}
			ans += arr[i];
		}
		printf("Case #%d: %d\n",++cs,ans);
		
	}
}
