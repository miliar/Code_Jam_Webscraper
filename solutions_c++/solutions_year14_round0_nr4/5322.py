/* ***********************************************
Author :rabbit
Created Time :2014/4/13 9:54:48
File Name :D.cpp
************************************************ */
#pragma comment(linker, "/STACK:102400000,102400000")
#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include <string>
#include <time.h>
#include <math.h>
#include <queue>
#include <stack>
#include <set>
#include <map>
using namespace std;
#define INF 0x3f3f3f3f
#define eps 1e-8
#define pi acos(-1.0)
typedef long long ll;
double a[1005],b[1005];
double aa[1005],bb[1005];
int main()
{
    int t,ca=0;
   // freopen("D-small-attempt0.in","r",stdin);
   // freopen("D-small-attempt0.out","w",stdout);
    scanf("%d",&t);
    while(t--)
    {
        int n;
        scanf("%d",&n);
        for(int i=0;i<n;++i)
            scanf("%lf",a+i);
        for(int i=0;i<n;++i)
            scanf("%lf",b+i);
        sort(a,a+n);
        sort(b,b+n);
        int ans=0,ans1=0;
        int r=0,s=0;
        for(int i=0;i<n;++i)
            if(a[r]<b[s])
                r++,s++;
            else
            {
                while(a[r]>b[s]&&(s<n))
                    s++,ans1++;
                r++,s++;
                if(s==n)
                    break;
            }
        r=n-1,s=n-1;
        int p=0;
        for(int i=0;i<n;++i)
            if(a[r]>b[s])
                ans++,r--,s--;
            else s--;
        printf("Case #%d: %d %d\n",++ca,ans,ans1);
    }
}
