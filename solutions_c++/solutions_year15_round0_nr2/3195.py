#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,l,h) for(int i=(l);i<=(h);++i)
#define FORD(i,h,l) for(int i=(h);i>=(l);--i)

typedef long long LL;

#define maxn 1010
//#define maxm 100
//#define mm 1000000007

int a[maxn];

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);

	int T;
	scanf("%d",&T);
	FOR(TT,1,T)
	{
		printf("Case #%d: ",TT);
		int n;
		scanf("%d",&n);
		int max_num=0;
		FOR(i,1,n)
		{
			scanf("%d",a+i);
			max_num=max(max_num,a[i]);
		}
		int ans=max_num;
		FOR(i,1,max_num)
		{
			int cnt=0;
			FOR(j,1,n)
				cnt+=(a[j]-1)/i;
			ans=min(ans,cnt+i);
		}
		printf("%d\n",ans);
	}
	
	//fclose(stdin);
	//fclose(stdout);
	return 0;
}
