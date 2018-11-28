#include <iostream>
#include <cstdio>
using namespace std;
int fair[]={1,4,9,121,484};
int main()
{
	int T,start,end,result;
	freopen("C-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&T);
	for(int cas = 1; cas <= T; ++cas)
	{
		scanf("%d%d",&start,&end);
		int i,j;
		result = 0;
		for(i = 0; i<5 && fair[i] < start; ++i);
		for(j = 4; j>=0 && fair[j] > end; --j);
		printf("Case #%d: %d\n",cas,j-i+1);

	}
}