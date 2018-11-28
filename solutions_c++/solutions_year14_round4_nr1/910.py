#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <string.h>
#include <string>
#include <list>
#include <stack>
#include <cstdlib>
#include <cmath>
#include <utility>

#define pb push_back
#define SZ 10007
using namespace std;

typedef long long Long;

int disk[SZ+7];
int n,X;


int main()
{
    freopen("A.in","rt",stdin);
    freopen("A.out","wt",stdout);
    int tst,cas;
    scanf("%d",&tst);
    for(cas=1;cas<=tst;cas++) {
        scanf("%d%d",&n,&X);
        for(int i=0;i<n;i++)    scanf("%d",&disk[i]);
        sort(disk,disk+n);
        int l = 0;
        int r = n-1;
        int ans = 0;
        while(l<=r) {
            if(l==r) {
                ans++;
                break;
            }
            else if(disk[l] + disk[r] <= X) l++,r--,ans++;
            else r-- , ans++;
        }
        printf("Case #%d: %d\n",cas,ans);

    }

    return 0;
}
