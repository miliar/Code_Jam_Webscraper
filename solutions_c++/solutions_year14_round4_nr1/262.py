#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#define ll long long


using namespace std;

int n,X,x[100010];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    cin>>T;
    int cas = 1;
    while (T--) {
        scanf("%d%d",&n,&X);
        for (int i = 0; i < n; i++) scanf("%d",&x[i]);
        sort(x,x+n);
        int cnt = 0;
        for (int i = 0,j = n - 1;i <= j;i++) {
            while (i < j && x[i] + x[j] > X) {
                j--;
                cnt++;
            }
            if (i == j) {
                cnt++;
                break;
            }
            j--;
            cnt++;
        }
        printf("Case #%d: %d\n",cas++,cnt);
    }
}
