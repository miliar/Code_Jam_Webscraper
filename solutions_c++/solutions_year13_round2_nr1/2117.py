#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<iostream>
#include<algorithm>
#include<utility>
#include<set>
#include<queue>
#include<stack>
#include<vector>
#include<string>
#include<map>

#define pb push_back
#define mp make_pair
#define fs first
#define sc second

#define openfile {freopen("test.txt","r",stdin);}
#define closefile {freopen("res.txt","w",stdout);}

using namespace std;

typedef long long ll;
typedef pair<int,int> pint;

const int maxn = 1000000 + 100;

template <class T> inline T abs(T x) { if (x < 0) return -x; return x; }

int test,n,res;
ll s;
int a[maxn];

int getbit(int m,int k) {
    return (m & ( 1 << k )) >> k;
}

int main() {

    openfile
    closefile

    scanf("%d",&test);
    for(int t=1; t<=test; t++) {

        scanf("%lld%d",&s,&n);
        for(int i=0; i<n; i++) {
            scanf("%d",&a[i]);
        }

        sort(a,a+n);

        res = -1;
        int temp;
        ll stemp;
        bool ok;

        for(int u=0; u < (1 << n); u++) {
            stemp = s;
            temp = 0;
            ok = true;

            for(int i=0; i<n; i++) if (ok) {
                if (getbit(u,i)) {
                    if (stemp == 1) ok = false;
                    while (stemp <= a[i] && ok) {
                        temp++;
                        stemp += (stemp-1);
                    }
                    stemp += a[i];
                } else {
                    temp++;
                }

            }

            if (ok) {
                if (res == -1) res = temp;
                res = min(res,temp);
            }
        }

        printf("Case #%d: %d\n",t,res);
    }

	return 0;
}
