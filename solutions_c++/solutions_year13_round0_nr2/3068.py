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
#define maxn 105
#define oo 1000000000
#define clearAll(a) memset(a,0,sizeof(a))
#define sq(a) ((a)*(a))

using namespace std;

typedef long long ll;

int a[maxn][maxn];
int l[maxn],r[maxn];
int n;

int main()
{
    freopen("C:\\Users\\py\\Desktop\\input.txt","r",stdin);
    freopen("C:\\Users\\py\\Desktop\\output.txt","w",stdout);

    int tt;
    scanf("%d",&tt);

    for (int id=1;id<=tt;id++)
    {
    	int n,m;
    	cin >> n >> m;
    	for (int i=1;i<=n;i++)
    		for (int j=1;j<=m;j++)
    			cin >> a[i][j];

    	for (int i=1;i<=n;i++)
    	{
    		l[i]=a[i][1];
    		for (int j=2;j<=m;j++)
    			l[i]=max(a[i][j],l[i]);
    	}

    	for (int j=1;j<=m;j++)
    	{
    		r[j]=a[1][j];
    		for (int i=2;i<=n;i++)
    			r[j]=max(a[i][j],r[j]);
    	}	

    	bool flag = true;

    	for (int i=1;i<=n;i++)
    		for (int j=1;j<=m;j++)
    			if (l[i]>a[i][j]&&r[j]>a[i][j])
    			{
    				flag = false;
    				goto py;
    			}

    	py :
    	printf("Case #%d: ",id);
    	if (flag)
    		printf("YES\n");
    	else printf("NO\n");
    }

    return 0;
}
