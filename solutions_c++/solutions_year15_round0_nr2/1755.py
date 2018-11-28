#include <iostream> 
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;
#define rep(i,n) for(int i=1;i<=(n);++i)
#define rep2(i,a,b) for(int i=(a);i<=(b);++i)
int n;
int ind[1001];
void task()
{
	scanf("%d",&n);
	rep(i,n)scanf("%d",&ind[i]);
	int minans=10000,tres;
	rep(ians,1000)
	{
		tres=0;
		rep(i,n)tres+=(ind[i]-1)/ians;
		minans=min(minans,tres+ians);
	}
	printf("%d\n",minans);
}
int main()
{
	//freopen("in","r",stdin);
	//freopen("out","w",stdout);
	int nt;scanf("%d",&nt);
	rep(i,nt)
	{
		printf("Case #%d: ",i);
		task();
	}
}
