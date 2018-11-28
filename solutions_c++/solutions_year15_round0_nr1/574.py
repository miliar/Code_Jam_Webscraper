#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <ctime>

#include <algorithm>
#include <iostream>
#include <string>
#include <utility>

#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <map>

#define FOR(i,a,b) for(i=a;i<=b;i++)
#define NL printf("\n")
#define MIN(a,b) (a<b?a:b)
#define MAX(a,b) (a>b?a:b)
#define QUAD(x) (x)*(x)
#define MOD(a,b) ((a)%(b)+b)%(b)

#define N 1000

using namespace std;

char a[N+10];

int main()
{
	freopen("A-large.in","r",stdin); freopen("1.out","w",stdout);
	int T;
	int i,j,r;
	int n;
	int num,col,ans;

	scanf("%d",&T);
	FOR(r,1,T){
		scanf("%d %s",&n,a);
		col=a[0]-'0'; ans=0;
		FOR(i,1,n){
			if(col>=n) break;
			num=a[i]-'0';
			if(col<i) ans+=i-col,col=i;
			col+=num;
		}
		printf("Case #%d: %d\n",r,ans);
	}
	return 0;
}