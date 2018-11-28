#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <iostream>
#include <cstdlib>
#include <sstream>

using namespace std;

int a[5][5];
int b[5][5];
int main()
{
	freopen("in.txt","r",stdin);freopen("out.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int cas=1;cas<=T;cas++)
	{
		int n1,n2;
		scanf("%d",&n1);
		for(int i=1;i<=4;i++)
			for(int j=1;j<=4;j++)
				scanf("%d",&a[i][j]);
		scanf("%d",&n2);
		for(int i=1;i<=4;i++)
			for(int j=1;j<=4;j++)
				scanf("%d",&b[i][j]);
		vector <int> ans;
		for(int i=1;i<=4;i++)
			for(int j=1;j<=4;j++)
				if(a[n1][i]==b[n2][j])
					ans.push_back(a[n1][i]);
		printf("Case #%d: ",cas);
		if(ans.size()==0)
			puts("Volunteer cheated!");
		else if(ans.size()==1)
			printf("%d\n",ans[0]);
		else
			puts("Bad magician!");
	}
	return 0;
}
