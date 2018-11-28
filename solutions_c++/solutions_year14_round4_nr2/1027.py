#include<cstdio>
#include<iostream>
#include<vector>
#include<algorithm>
#include<queue>
#include<stack>

using namespace std;

#define sd(x) scanf("%d",&x);
#define slld(x) scanf("%lld",&x);
#define LL long long
#define LD long double
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define Fill(a, b) memset(a, b, sizeof(a))
#define INF 2000000009

typedef pair<int,int> PII;
typedef vector<int> VI;

#define MAXN 1010

int ar[MAXN],br[MAXN],cr[MAXN],tree[MAXN];

int bin(int l,int r,int val)
{
    if(l==r)return l;
    else
    {
        int mid=(l+r)/2;
        if(ar[mid]==val)return mid;
        else if(ar[mid]>val)return bin(l,mid-1,val);
        else return bin(mid+1,r,val);
    }
}

void update(int idx ,int val)
{
	while (idx <= MAXN-1)
    {
		tree[idx] += val;
		idx += (idx & -idx);
	}
}
int read(int idx)
{
	int sum = 0;
	while (idx > 0)
    {
		sum += tree[idx];
		idx -= (idx & -idx);
	}
	return sum;
}

void precompute()
{
    for(int i=0;i<MAXN;i++)
    {
        ar[i]=0;
        br[i]=0;
        cr[i]=0;
        tree[i]=0;
    }
}

void solve()
{
    precompute();
    int n,l=1,r,idx,ans=0;
    sd(n);
    r=n;
    for(int i=1;i<=n;i++)
    {
        sd(ar[i]);
        br[i]=ar[i];
    }
    sort(ar,ar+n+1);
    for(int i=1;i<=n;i++)
    {
        br[i]=bin(1,n,br[i]);
        cr[br[i]]=i;
        update(i,1);
    }
    for(int i=1;i<=n;i++)
    {
       //printf("%d %d\n",br[i],cr[i]);
    }//printf("aman %d\n",ans);
    for(int i=1;i<=n;i++)
    {
        idx=read(cr[i]);
        //printf("idx %d\n",idx);
        if(r-idx<idx-l)
        {
            update(cr[i],-1);
            ans=ans+r-idx;
            r--;
        }
        else
        {
            update(1,1);
            update(cr[i],-1);
            ans=ans+idx-l;
            l++;
        }
        //printf("%d\n",ans);
    }
    printf("%d\n",ans);


}

int main()
{
    //freopen("in1.txt","r",stdin);
    //freopen("out.txt","w",stdout);
	int t=1;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
	    printf("Case #%d: ",i);
		solve();
	}
}

