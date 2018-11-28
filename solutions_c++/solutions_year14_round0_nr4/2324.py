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
#define maxn 1005
#define oo 1000000000
#define clearAll(a) memset(a,0,sizeof(a))
#define sq(a) ((a)*(a))

using namespace std;

typedef long long ll;

double a[maxn],b[maxn];
int n;
int tt;

int work1()
{
	int i,j;
	int ans=0;
	i=j=1;
	while (i<=n)
	{
		while (i<=n&&a[i]<b[j]) i++;
		if (i<=n&&a[i]>b[j])
			ans++,j++;
		i++;
	}
	return ans;
}

int work2()
{
	int ans=0;
	int i,j;
	i=j=1;
	while (i<=n||j<=n)
	{
		while (j<=n&&a[i]>b[j]) j++;
		if (j<=n&&a[i]<b[j])
			j++;
		else ans++;
		i++;
	}
	return ans;
}

int main()
{
    freopen("H:\\Users\\Yun\\Desktop\\input.txt","r",stdin);
    //freopen("C:\\Users\\py\\Desktop\\output.txt","w",stdout);

    cin >> tt;
    int id=0;

    while (tt--)
    {
        id++;
    	cin >> n;
    	for (int i=1;i<=n;i++)
    		cin >> a[i];
    	for (int i=1;i<=n;i++)
    		cin >> b[i];
    	sort(a+1,a+1+n);
    	sort(b+1,b+1+n);
    	printf("Case #%d: %d %d\n",id,work1(),work2());
    }
    return 0;
}
