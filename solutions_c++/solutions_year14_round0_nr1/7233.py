#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <list>
#include <vector>
#include <map>
#include <set>
#include <utility>
using namespace std;

#define MS(A)	memset(A, 0, sizeof(A))
#define REP(i ,n) for( i = 0; i < (n); i++)
#define FOR(i, a, n) for( i = a; i < n; i++)

#define MAX 1562505
#define MOD 1000000007
#define INF (int(1e9))
#define PB push_back
typedef long long int LL;
typedef vector <int> vi;

vi *v;

int main()
{
	int t,n,m,i,j,k;
	scanf("%d",&t);
	int ti,a[4][4];
	set<int> ms;
	for(ti=0;ti<t;ti++)
	{
		ms.clear();
		scanf("%d",&k);		k--;		
		REP(i,4)	REP(j,4)	scanf("%d",&a[i][j]);
		REP(i,4)	ms.insert(a[k][i]);

		int ct=0;
		scanf("%d",&k);		k--;		
		REP(i,4)	REP(j,4)	scanf("%d",&a[i][j]);
		REP(i,4)
			if(ms.find(a[k][i]) != ms.end())	ct++, m=a[k][i];

		printf("Case #%d: ",ti+1);
		if(ct == 1)	printf("%d\n",m);
		else if(ct > 1)	printf("Bad magician!\n");
		else		printf("Volunteer cheated!\n");
	}
	return 0;
}
