#include <stdio.h>
#include <string>
#include <algorithm>
using namespace std;
bool isPal(int x)
{
	char str[256];
	sprintf(str,"%d",x);
	string a=str;
	string b=str;
	reverse(b.begin(),b.end());
	return a==b;
}
int main()
{
	int T;	scanf("%d",&T);
	for (int kase=1;kase<=T;++kase)
	{
		int a,b,ret=0;
		scanf("%d %d",&a,&b);	
		for (int q=1;q*q<=b;++q)
			if (a<=q*q && q*q<=b && isPal(q) && isPal(q*q))
				ret++;
		printf("Case #%d: %d\n",kase,ret);
	}
	return 0;
}
