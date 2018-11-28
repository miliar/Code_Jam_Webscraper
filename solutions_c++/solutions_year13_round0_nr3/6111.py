#include <iostream>
#include <algorithm>
#include <cstdio>
using namespace std;
int t,a,b,FS[5]={1,4,9,121,484};
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("cikti.txt","w",stdout);
	int i,j,s;
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		scanf("%d %d",&a,&b);
		s=0;
		for(j=0;j<5;j++)
			if(a<=FS[j] && FS[j]<=b)
				s++;
		printf("Case #%d: %d\n",i,s);		
	}
	getchar(); getchar();
	return 0;
}
