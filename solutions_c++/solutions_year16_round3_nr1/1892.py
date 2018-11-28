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

#define PB push_back
#define MP make_pair

#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,l,h) for(int i=(l);i<=(h);++i)
#define FORD(i,h,l) for(int i=(h);i>=(l);--i)

//#define coutpoint6 setiosflags(ios::fixed)<<setprecision(6)

#define maxn 50
//#define INF 100000000
//#define maxm 1000000
//#define MM 1000000007

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;

int a[maxn];

int main()
{
	//srand((int)time(NULL));
	
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	//ios_base::sync_with_stdio(false);
	
	int T;
	scanf("%d",&T);
	REP(TT,T)
	{
		printf("Case #%d: ",TT+1);
		int n;
		scanf("%d",&n);
		int sum=0;
		FOR(i,1,n)
		{
			scanf("%d",a+i);
			sum+=a[i];
		}
		while((sum--)>2)
		{
			int p=1;
			FOR(i,1,n)
				if (a[i]>a[p])
					p=i;
			printf("%c",'A'+p-1);
			a[p]--;
			
			FOR(i,1,n)
				if (a[i]>sum/2)
				{
					printf("%c",'A'+i-1);
					a[i]--;
					sum--;
					break;
				}
			printf(" ");
		}
		FOR(i,1,n)
			if (a[i])
				printf("%c",'A'+i-1);
		printf("\n");
	}

	//fclose(stdin);
	//fclose(stdout);
	return 0;
}
