#include <iostream>
#include<iomanip>
#include <cstdio>
#include <climits>
#include <algorithm>
#include <queue>
#include <cstring>
#include <cmath>
#include <vector>
#include <stack>
#include <set>
#include<list>
#include <map>
#include <deque>
#define SET(p) memset(p,-1,sizeof(p))
#define CLR(p) memset(p,0,sizeof(p))
#define LL long long int
#define ULL unsigned long long int
#define S(n) scanf("%d",&n)
#define Sl(n) scanf("%lld",&n)
#define Sf(n) scanf("%lf",&n)
#define Ss(n) scanf("%s",n)
using namespace std;
int kmod=1000000007;

void fun(int k)
{
	long long int r,t;
	Sl(r);
	Sl(t);
	long long int s=0;
	LL p=2*r+1;
	LL q=p;

	while(p<=t)
	{
		s++;
		p+=(q+4);
		q+=4;
	}
	printf("Case #%d: %lld\n",k,s);
}

int main()
{
	int t;
	S(t);
	for(int k=1;k<=t;k++)
	{
		fun(k);
		//cin>>s;
	}
	return 0;
}

