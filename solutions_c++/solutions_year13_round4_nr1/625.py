#include<cstdio>
#include<cstring>
#include<algorithm>
#include<utility>
using namespace std;

const int maxm=1005;
const long long mo=1000002013;
int N, M;
pair<int,int> X[maxm], Y[maxm];

long long cost(int st, int en)
{
	long long len(en-st);
	return ((long long)len*N-(long long)len*(len-1)/2)%mo;
}

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int T, CNT(0);
	scanf("%d",&T);
	for (;T;T--)
	{
		scanf("%d%d",&N,&M);
		long long ori(0);
		for (int i=1;i<=M;i++)
		{
			int x, y, z;
			scanf("%d%d%d",&x,&y,&z);
			X[i]=make_pair(x,z);
			Y[i]=make_pair(y,z);
			ori+=cost(x,y)*z, ori%=mo;
		}
		sort(X+1,X+M+1);
		sort(Y+1,Y+M+1);
		long long ans(0);
		for (int i=1,j=1;i<=M;i++)
		{
			while (j<M && X[j+1].first<=Y[i].first) j++;
			int k(j);
			while (Y[i].second)
			{
				int people(min(X[k].second,Y[i].second));
				ans+=cost(X[k].first,Y[i].first)*people, ans%=mo;
				X[k].second-=people;
				Y[i].second-=people;
				k--;
			}
		}
		CNT++;
		printf("Case #%d: %I64d\n",CNT,((ori-ans)%mo+mo)%mo);
	}
	return 0;
}

