#include <cstdio>
#include <set>
#include <cmath>
#include <map>
using namespace std;

typedef long long LL;

const LL maxv = 3333338;
int vis[maxv];
LL Prime[maxv];
int Size;

int N,J;
int P[38];

void Init()//////////////////////////////////////
{
	Size = 0;
	for(LL i=2;i<maxv;i++)
	{
		if(vis[i])continue;

		Prime[Size++] = i;

		if(i>(LL)sqrt((long double)maxv)+1)continue;
		
		for(LL k=i*i;k<maxv;k += i)
			vis[k] = 1;
	}
}

bool IsPrime(LL ret)///////////////////////////////
{
	for(int i=0;i<Size;i++)
	{
		if(ret <= Prime[i])break;
		if(ret%Prime[i]==0)return false;
	}

	return true;
}

LL GetDivisor(LL ret)//////////////////////////////
{
	for(int i=0;i<Size;i++)
	{
		if(ret%Prime[i]==0)return Prime[i];
	}
}

LL Sum(LL base)////////////////////////////////////
{
	LL ans = 0,t = 1;
	for(int i=0;i<N;i++)
	{
		ans += P[i]*t;
		t *= base;
	}
	return ans;
}

void DFS(int cur)////////////////////////////////
{
	if(J==0)return;

	if(cur==N)
	{
		int ok = 1;
		for(int base = 2;base<=10;base++)
		{
			LL ret = Sum((LL)base);

			if(IsPrime(ret)){ok=0;break;}
		}

		if(ok)
		{
			J--;
			for(int i=N-1;i>=0;i--)printf("%d",P[i]);
			for(int base=2;base<=10;base++)
			{
				LL ret = Sum(base);
				printf(" %lld",GetDivisor(ret));
			}

		printf("\n");

		}

		return;
	}

	if(cur==0 || cur==N-1){P[cur]=1;DFS(cur+1);}
	else
		for(int i=0;i<2;i++)
		{
			P[cur] = i;
			DFS(cur+1);
		}

}

int main()///////////////////////////////////////
{
//	freopen("..\\B-small-attempt2.in","r",stdin);
	freopen("..\\C-small-attempt0.out","w",stdout);

//	freopen("..\\B-large.in","r",stdin);
//	freopen("..\\B-large.out","w",stdout);

	N = 16;
	J = 50;

	Init();

	printf("Case #1:\n");

	while(J)
	{
		DFS(0);
	}

	return 0;
}