#include <iostream>
#include <cassert>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
using namespace std;
#define rep(i,n) for(int i=1;i<=(n);++i)
#define rep2(i,a,b) for(int i=(a);i<=(b);++i)
int n;
char ind[20002];
char tstk[20002];
int pstk;
void task()
{
	pstk=0;
	scanf("%s",ind+1);
	n=strlen(ind+1);
	int tot=0;
	rep(i,n)
	{
		if(ind[i]==tstk[pstk])
		{
			--pstk;
			tot+=10;
		}
		else if(pstk+1<=n-i)
		{
			tstk[++pstk]=ind[i];
		}
		else
		{
			--pstk;
			tot+=5;
		}
	}
	printf("%d\n",tot);
}
int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int nt;scanf("%d",&nt);
	rep(i,nt)
	{
		printf("Case #%d: ",i);
		task();
	}
}
