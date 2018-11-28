#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>

#include<cmath>
#include<iostream>
#include<iomanip>
#include<fstream>

#include<string>
#include<utility>
#include<vector>
#include<list>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>

#define ii long long int
#define pi 2*acos(0.0)
#define eps 1e-9
#define mem(x,y) memset(x,y,sizeof(x))
#define all(x) x.begin(), x.end()
#define pb push_back
#define sz(a) (int)a.size()
#define inf 2147483640
#define mx 100010

using namespace std;

const int debug= 0;
bool cnt[10];
int found;

void dig(int n) {
    while (n) {
        int rem=n%10;
        n/=10;
        if (!cnt[rem]) found++;
        cnt[rem]=1;
    }
}

int main() {
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for (int x=1;x<=t;++x) {
        int n,num;
        scanf("%d",&n);

        if (!n) {
            printf("Case #%d: INSOMNIA\n",x);
            continue;
        }

        num=n;
        mem(cnt,0);found=0;

        while (1) {
            dig(num);
            if (found==10) break;
            num+=n;
        }
        printf("Case #%d: %d\n",x,num);
    }

    return 0;
}
