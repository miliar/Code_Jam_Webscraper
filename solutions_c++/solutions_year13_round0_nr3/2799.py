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
#define maxn
#define oo 1000000000
#define clearAll(a) memset(a,0,sizeof(a))
#define sq(a) ((a)*(a))

using namespace std;

typedef long long ll;

bool isP(int);

bool isS(int x)
{
	int y = sqrt(x);

	if (y*y==x&&isP(y)) return true;
	return false;
}

bool isP(int x)
{
	int a[10];

	int m =0;

	while (x)
	{
		a[++m]=x%10;
		x/=10;
	}

	for (int i=1;i<=m/2;i++)
		if (a[i]!=a[m-i+1])
			return false;
	return true;

}

int main()
{
    freopen("C:\\Users\\py\\Desktop\\input.txt","r",stdin);
    freopen("C:\\Users\\py\\Desktop\\output.txt","w",stdout);

    int tt;
    cin >> tt;
    int l,r;
    for (int id=1;id<=tt;id++)
    {
    	cin >> l >> r;

    	int ans = 0;
    	for (int i=l;i<=r;i++)
    		if (isP(i)&&isS(i))
    			ans++;
    	printf("Case #%d: %d\n",id,ans);
    }


    return 0;
}
