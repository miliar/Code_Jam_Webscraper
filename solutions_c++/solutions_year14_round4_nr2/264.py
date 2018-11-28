#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <string>
#include <cstring>
#include <vector>
#include <iostream>
#include <ctime>
#define ll long long
using namespace std;


int n,a[1100];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    int cas = 1;
    while (T--) {
        scanf("%d",&n);
        for (int i = 0;i < n; i++) {
            scanf("%d",&a[i]);
        }
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            int l,r;
            l = r =0;
            for (int j = 0; j < i; j++)
            if (a[j] > a[i]) l++;
            for (int j = i + 1; j < n; j++)
            if (a[j] > a[i]) r++;
            cnt += min(l,r);
        }
        printf("Case #%d: %d\n",cas++,cnt);
    }
}
