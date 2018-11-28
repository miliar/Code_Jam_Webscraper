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

char a[maxn];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);

	int T;
	scanf("%d",&T);
	FOR(TT,1,T)
	{
		printf("Case #%d: ",TT);
		int n;
		scanf("%d%s",&n,a);
		int sum=0,ans=0;
		FOR(i,0,n)
		{
			if (sum<i)
			{
				ans+=i-sum;
				sum=i;
			}
			sum+=a[i]-'0';
		}
		printf("%d\n",ans);
	}

	//fclose(stdin);
	//fclose(stdout);
	return 0;
}
