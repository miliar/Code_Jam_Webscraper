#include"stdafx.h"
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<algorithm>
using namespace std;
struct data{
	int v,i;
	bool operator < (const data &cmp)const
	{
		return v<cmp.v;
	}
}a1[10000];
int a[10000];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
    int tk,tk1=0,n,i;
    scanf("%d",&tk);
    while (tk--)
    {
        tk1++;
        scanf("%d",&n);
        int pos=0;
		for (i=1;i<=n;i++)
		{
			scanf("%d",&a[i]);
			a1[i].v=a[i];
			a1[i].i=i;
		}
		sort(a1+1,a1+n+1);
		int l=1,r=n;
		int res=0;
		for (i=1;i<=n;i++)
		{
			int v=a1[i].v;
			int j;
			for (j=l;j<=r;j++)
				if (a[j]==v)
					break;
			int pos=j;
			int lv=j-l,rv=r-j;
			if (lv<rv)
			{
				res+=lv;
				for (j=pos;j>l;j--)
					swap(a[j],a[j-1]);
				l++;
			}
			else{
				res+=rv;
				for (j=pos;j<r;j++)
					swap(a[j],a[j+1]);
				r--;
			}
		}
		printf("Case #%d: %d\n",tk1,res);
    }
}
