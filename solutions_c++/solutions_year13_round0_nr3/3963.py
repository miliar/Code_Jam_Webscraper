#include <stdio.h>

using namespace std;

int main()
{
	freopen("fair.in","r",stdin);
	freopen("fair.out","w",stdout);
	int t,a,b,counter = 0,r[6] = {1,4,9,121,484,10201};
	scanf("%d",&t);
	for(int q = 0;q < t;q++)
	{
		counter = 0;
		scanf("%d%d",&a,&b);
		for(int i = 0;i < 6;i++)
		if(r[i] >= a && r[i] <= b)counter++;
		printf("Case #%d: %d\n",q+1,counter);
	}
}
