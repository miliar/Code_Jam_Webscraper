#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cmath>
#include <stack>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

#define sd(i) scanf("%d",&i)
#define sc(i) scanf("%c",&ch)
#define sll(i) scanf("%lld",&i)
#define sull(i) scanf("%llu",&i)
#define sstr(i) scanf("%s",i)
#define pd(i) printf("%d",i)
#define pc(i) printf("%c",i)
#define pll(i) printf("%lld",i)
#define pull(i) printf("%llu",i)
#define pstr(i) printf("%s",i)
#define newline printf("\n")
#define itoa(i,j) sprintf(i,"%d",j)
#define rep(i,j,n) for(i=j;i<n;i++)
#define ull unsigned long long
#define ll long long
#define pie acos(-1)


void readline(char *str)
{
	char ch;
	sc(ch);
	int i=0;
	while(ch != '\n') {str[i++]=ch;sc(ch);}
	str[i]='\0';
}

int mod(long long n)
{
	int res;
	res=n%1000000007;
	if(res<0) res+=1000000007;
	return res;
}


int main()
{
	int te;
	sd(te);
	int in;
	rep(in,1,te+1)
	{
		int r,t;
		sd(r);sd(t);
		int coun=0;
		int curr=0;
		double dt = (double)t;
		while(1)
		{
			dt-=(r+curr+1)*(r+curr+1)-(r+curr)*(r+curr);
			curr+=2;
			if(dt<0) break;
			coun++;
		}
		printf("Case #%d: %d\n",in,coun);
	}
}