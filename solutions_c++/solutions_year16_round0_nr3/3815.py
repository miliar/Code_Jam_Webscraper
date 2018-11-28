#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
#define INF 0x3f3f3f3f
typedef long long LL;
int A[20];
int n,m;
const int maxn=1e6+100;
const int Times = 10;
LL multi(LL a, LL b, LL m)
{
    LL ans = 0;
    a %= m;
    while(b)
    {
        if(b & 1)
        {
            ans = (ans + a) % m;
            b--;
        }
        b >>= 1;
        a = (a + a) % m;
    }
    return ans;
}

LL quick_mod(LL a, LL b, LL m)
{
    LL ans = 1;
    a %= m;
    while(b)
    {
        if(b & 1)
        {
            ans = multi(ans, a, m);
            b--;
        }
        b >>= 1;
        a = multi(a, a, m);
    }
    return ans;
}

bool Miller_Rabin(LL n)
{
    if(n == 2) return true;
    if(n < 2 || !(n & 1)) return false;
    LL m = n - 1;
    int k = 0;
    while((m & 1) == 0)
    {
        k++;
        m >>= 1;
    }
    for(int i=0; i<Times; i++)
    {
        LL a = rand() % (n - 1) + 1;
        LL x = quick_mod(a, m, n);
        LL y = 0;
        for(int j=0; j<k; j++)
        {
            y = multi(x, x, n);
            if(y == 1 && x != 1 && x != n - 1) return false;
            x = y;
        }
        if(y != 1) return false;
    }
    return true;
}
bool vis[maxn];
int pri[maxn];

void get()
{
	int tot=0;
	memset(vis,true,sizeof vis);
	for(int i=2;i<=1000000;i++)
	{
		if(vis[i]) pri[tot++]=i;
		for(int j=0;j<tot;j++)
		{
			if(i*pri[j]>1000000) break;
			vis[i*pri[j]]=false;
			if(i%pri[j]==0) break;
		}
	}
}

void dfs(int a)
{
	if(m<=0) return;
//	cout<<a<<endl;
	int i,j,k;
	if(a==1)
	{
		LL B[20];
		for(i=2;i<=10;i++)
		{
			LL sum=0;
			for(j=1;j<=n;j++)
			{
				sum=sum*i+A[j];
			}
//			cout<<sum<<endl;
			if(sum>=1000000)
			{
				if(Miller_Rabin(sum))
				{
					break;
				}
				else 
				{
					B[i]=sum;
				}
			}
			else
			{
				if(vis[sum]) break;
				else B[i]=sum;
			}
		}
//		cout<<i<<endl;
		if(i<=10) return ;
	//	cout<<m<<endl;
		for(i=1;i<=n;i++)
			printf("%d",A[i]);
		
		for(i=2;i<=10;i++)
		{
			for(j=2;;j++)
			{
				if(B[i]%j==0) 
				{
					printf(" %d",j);
					break;
				}
			}
		}
		puts("");
		m--;
		return ;
	}
	A[a]=0;
	dfs(a-1);
	A[a]=1;
	dfs(a-1);
}

		
		 
int main()
{
	//freopen("C-small-attempt2.in","r",stdin);
	//freopen("1.out","w",stdout);
	int t,case1=0;
	get();
	scanf("%d",&t);
	while(t--)
	{
		int i,j,k;
		memset(A,0,sizeof A);
		scanf("%d%d",&n,&m);
		A[n]=1;
		A[1]=1;
		printf("Case #%d:\n",++case1);
		dfs(n-1);
	}
	return 0;
}
	
