#include <iostream>
#include <cassert>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <set>
using namespace std;
#define rep(i,n) for(int i=1;i<=(n);++i)
#define rep2(i,a,b) for(int i=(a);i<=(b);++i)
int ng,nl;
char sb[52];
char sg[102][52];
set<string> myg;
void task()
{
	myg.clear();
	scanf("%d%d",&ng,&nl);
	rep(i,ng)
	{
		scanf("%s",sg[i]+1);
		myg.insert(sg[i]+1);
	}
	scanf("%s",sb+1);
	if(myg.find(sb+1)!=myg.end())
	{
		printf("IMPOSSIBLE\n");
		return;
	}
	rep(i,nl)printf("?0");
	printf(" ");
	if(nl==1)printf("0");
	rep(i,nl-1)printf("1");
	printf("\n");
	
}
int main()
{
	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);
	int nt;scanf("%d",&nt);
	rep(i,nt)
	{
		printf("Case #%d: ",i);
		task();
	}
}
