#include <iostream>
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <algorithm>
#include <stdlib.h>
#include <string>
#include <queue>
#include <vector>
#include <set>
#define maxn 2005
#define MOD 1000002013
#define oo 1000000000
#define clearAll(a) memset(a,0,sizeof(a))
#define sq(a) ((a)*(a))

using namespace std;

typedef long long ll;

struct node
{
	int l,r,p;
};

node a[maxn];
node b[maxn];
pair<int,int> stk[maxn],top;

int n,m;

bool cmp(node x,node y)
{
	if (x.l!=y.l)
		return x.l<y.l;
	return x.r<y.r;
}

bool cmp2(node x,node y)
{
	if (x.r!=y.r)
		return x.r<y.r;
	return x.l<y.l;
}

ll calc(ll l,ll r,ll p)
{
    ll tmp = (p*(((r-l)*(2*n+1-r+l)/2)%MOD))%MOD;
    if (tmp<0) puts("fuck");
	return tmp;
}

int main()
{
    freopen("C:\\Users\\py\\Desktop\\gcj\\input.txt","r",stdin);
    freopen("C:\\Users\\py\\Desktop\\gcj\\output.txt","w",stdout);

    int tt;
    scanf("%d",&tt);

    for (int id=1;id<=tt;id++)
    {
    	cin >> n >> m;
    	for (int i=1;i<=m;i++)
    	{
    	    cin >> a[i].l >> a[i].r >> a[i].p;
    	    b[i]=a[i];
    	}

    	sort(a+1,a+1+m,cmp);
    	sort(b+1,b+1+m,cmp2);


    	ll good=0;
    	for (int i=1;i<=m;i++)
    	{
    		//good += a[i].p*(a[i].r-a[i].l)*(2*n+1-a[i].r+a[i].l)/2;
    		good += calc(a[i].l,a[i].r,a[i].p);
    		good %= MOD;
    	}

    	ll best=0;
    	int top = 0;
    	int i = 1;
    	int j = 1;
    	int k = 1;
    	a[m+1].l=oo+10;
    	b[m+1].r=oo+10;
    	while (k<=n)
    	{
    		while (k==a[i].l)
    		{
    			stk[++top]=make_pair(a[i].l,a[i].p);
    			i++;
    		}

    		while (k==b[j].r)
    		{
    			pair<int,int> tmp = stk[top--];
    			if (tmp.second>=b[j].p)
    			{
    				tmp.second-=b[j].p;
    				best += calc(tmp.first,b[j].r,b[j].p);
    				best %= MOD;
    				if (tmp.second>0)
    					stk[++top]=tmp;
    				j++;
    			}  else
    			{
    				best += calc(tmp.first,b[j].r,tmp.second);
    				best %= MOD;
    				b[j].p -= tmp.second;
    			}
    		}
    		k=min(a[i].l,b[j].r);
    	}
    	printf("Case #%d: ",id);
    	cout << ((good - best)%MOD+ MOD ) % MOD  << endl;
    }

    return 0;
}
