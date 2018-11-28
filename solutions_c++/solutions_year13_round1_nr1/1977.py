#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
using namespace std;
typedef long long LL;
int main()
{
	int T;
	LL r,c;
	scanf("%d",&T);
	for(int i=0;i<T;i++)
	{
		scanf("%I64d%I64d",&r,&c);
		LL A=2;
		LL B=2*r-1;
		LL C=-c;
		LL n=(-B+sqrt((double)B*B-4*A*C))/(2*A);
		if(2*n*n+(2*r-1)*n-c>0)
			n--;
		printf("Case #%d: %I64d\n",i+1,n);
	}
	return 0;
}
