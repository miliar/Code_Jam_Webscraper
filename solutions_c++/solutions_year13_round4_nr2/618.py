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
#define maxn 2000
#define oo 1000000000
#define clearAll(a) memset(a,0,sizeof(a))
#define sq(a) ((a)*(a))

using namespace std;

typedef long long ll;

int n,p;
int l,r;

int calcL(int x)
{
	int tmp = (1<<n)-x-1;
	int ans = 0;
    for (int i=0;i<n;i++)
	{
		ans<<=1;
		ans|=1;
		if (tmp>0)
		{
			ans=0;
			tmp = (tmp-1)/2;
		}
	}
	return ans;
}

int calcR(int x)
{
	int tmp =  x;
	int ans = 0;
	for (int i=0;i<n;i++)
	{
	    ans<<=1;
		if (tmp>0)
		{
			ans|=1;
			tmp = (tmp-1)/2;
		}
	}
	return ans;
}

int main()
{
    freopen("C:\\Users\\py\\Desktop\\gcj\\input.txt","r",stdin);
    //freopen("C:\\Users\\py\\Desktop\\gcj\\output.txt","w",stdout);

    int tt;
    cin >> tt;
    for (int id=1;id<=tt;id++)
    {
    	cin >> n >> p;
    	int al=-1,ar=-1;
    	for (int i=0;i<(1<<n);i++)
    	{
    		l=calcL(i);
    		r=calcR(i);
    		if (r<=p-1)
    			al=max(al,i);
    		if (l<=p-1)
    			ar=max(ar,i);
    	}

    	printf("Case #%d: %d %d\n",id,al,ar);
    }

    return 0;
}
