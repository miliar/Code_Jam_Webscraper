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
#define maxn 200000
#define oo 1000000000
#define clearAll(a) memset(a,0,sizeof(a))
#define sq(a) ((a)*(a))

using namespace std;

typedef long long ll;

int n;
int X;
int a[maxn];
bool flag[maxn];

int main()
{
    freopen("E:\\codejam\\input.txt","r",stdin);
    freopen("E:\\codejam\\output.txt","w",stdout);

    int tt;
    cin >> tt;
    int id = 0;
    while (tt--)
    {
        cin >> n >> X;
        for (int i=1;i<=n;i++)
            cin >> a[i];
        sort(a+1,a+1+n);
        clearAll(flag);

        int i,j;
        i = 1;
        j = n;
        int ans = 0;
        while (i<=n){
            if (flag[i]) { i++; continue;}
            flag[i]=true;
            while ((j>=1&&a[i]+a[j]>X)||flag[j]) j--;
            if (j>0){ flag[j]=true; }
            ans++;
        }

        id++;
        printf("Case #%d: %d\n",id, ans);
    }
    return 0;
}
