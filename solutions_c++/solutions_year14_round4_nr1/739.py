#include"stdafx.h"
#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
using namespace std;
int a[100000];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
    int tk,tk1=0,n,k,i;
    scanf("%d",&tk);
    while (tk--)
    {
        tk1++;
        scanf("%d %d",&n,&k);
        for (i=0;i<n;i++)
            scanf("%d",&a[i]);
		sort(a,a+n);
        int head=0,tail=n-1;
        int res=0;
        while (head<=tail)
        {
            while (a[tail]+a[head]>k && head<tail)
            {
                tail--;
                res++;
            }
            head++;
			tail--;
            res++;
        }
        printf("Case #%d: %d\n",tk1,res);
    }
    return 0;
}
