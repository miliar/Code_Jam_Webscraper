#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
int T,p,q,v[200];
int main()
{
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	cin>>T;
	for (int Case=1;T;T--,Case++) {
		printf("Case #%d: ",Case);
		scanf("%d",&p);
		for (int i=1;i<=16;i++) v[i]=0;
		for (int i=1;i<=4;i++)
			for (int j=1;j<=4;j++) {
				int x;
				scanf("%d",&x);
				if (i==p) v[x]|=1;
			}
		scanf("%d",&q);
		for (int i=1;i<=4;i++)
			for (int j=1;j<=4;j++) {
				int x;
				scanf("%d",&x);
				if (i==q) v[x]|=2;
			}
		int ans=0;
		for (int i=1;i<=16;i++)
			if (3==v[i]) {
				if (!ans) ans=i;
				else ans=-1;
			}
		if (!ans) printf("Volunteer cheated!\n");
		else if (-1==ans) printf("Bad magician!\n");
		else printf("%d\n",ans);
	}
	return 0;
}
