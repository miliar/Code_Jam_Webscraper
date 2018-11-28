#include<iostream>
#include<cstdio>
#include<cstdlib>
using namespace std;
int main()
{
//	freopen("C-small-attempt0.in","r",stdin);
//	freopen("c.out","w",stdout);
	int t,a,b;
	scanf("%d",&t);
	int nos[5]={1,4,9,121,484};
	for(int tc=1;tc<=t;tc++)
	{
		scanf("%d%d",&a,&b);
		int cnt=0;
		for(int i=0;i<5;i++)
		{
			if(nos[i]>=a&&nos[i]<=b)
				cnt++;
		}
		printf("Case #%d: %d\n",tc,cnt);
	}
	return 0;
}