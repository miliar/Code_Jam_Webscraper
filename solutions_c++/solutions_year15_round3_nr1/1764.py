#include<bits/stdc++.h>
using namespace std;

int main()
{
	freopen("inp.txt","r",stdin);
	freopen("codejam_A.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for(int tst = 1; tst <= t;tst++)
	{
		int r,c,w;
		scanf("%d%d%d",&r,&c,&w);
		printf("Case #%d: %d\n",tst,(c-1)/w+w);
	}
	
}
