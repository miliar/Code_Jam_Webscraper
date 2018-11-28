#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <list>
#include <vector>
#include <map>
using namespace std;

#define MS(A)	memset(A, 0, sizeof(A))
#define REP(i ,n) for(i = 0; i < (n); i++)
#define FOR(i, a, n) for(i = a; i < n; i++)

#define MAX 42
#define MOD 1000000007
#define INF (int(1e9))
#define PB push_back
#define M1 102
typedef long long int LL;
typedef vector <int> vi;

vi *v;

int solve(char a[],char b[])
{
	int i,j,k,x,y,p=0,ans=0;
	char c,d,e;
	for(i=0;a[i];)
	{
		c=a[i];		i++;
		x=1;
		while(a[i] && a[i]==c)	i++,x++;
		if(!b[p] || b[p]!=c)	return -1;
		y=1;	p++;
		while(b[p] && b[p]==c)	p++,y++;
		x=x-y;
		if(x<0)	x=-x;		ans+=x;		//printf("xx  %d\n",x);
	}
	if(a[i] || b[p])	return -1;
	return ans;
}

int main()
{
	int t,i,j,k,m,n;
	int x,y,ti;
	scanf("%d",&t);
	char a[105],b[105];
	REP(ti,t)
	{
		scanf("%d",&n);
		cin >> a;	cin >> b;
		k = solve(a,b);
		printf("Case #%d: ",ti+1);
		if(k== -1)	printf("Fegla Won\n");
		else		printf("%d\n",k);
	}
	return 0;
}
		
