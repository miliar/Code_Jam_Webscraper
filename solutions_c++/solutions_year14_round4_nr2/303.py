#include<cstdio>
#include<algorithm>
#include<cstring>
#include<vector>
using namespace std;

int N;
vector<int> A;

int main()
{
	freopen("p2.in","r",stdin);
	freopen("p2.out","w",stdout);
	int TT;
	scanf("%d",&TT);
	for (int tt=1;tt<=TT;tt++)
	{
		int ans(0);
		scanf("%d",&N);
		A=vector<int>(N);
		for (int i=0;i<N;i++) scanf("%d",&A[i]);
		while (!A.empty())
		{
			int x(0);
			for (int i=1;i<A.size();i++) if (A[i]<A[x]) x=i;
			ans+=min<int>(x,A.size()-x-1);
			A.erase(A.begin()+x);
		}
		printf("Case #%d: %d\n",tt,ans);
	}
	return 0;
}

