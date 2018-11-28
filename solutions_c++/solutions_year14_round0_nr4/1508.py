#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <stack>
#include <queue>
#include <set>
#include <string>

using namespace std;

int tcase,n;
float a[10003],b[10003];

bool mark[12];
float pa[12];
set<float> sb;
int res2;

int solveDeceitful() {
    int sid=0;

    for (int i=1; i<=n; ++i)
        if (sid+1<=n && b[sid+1]<a[i]) ++sid;

    return sid;
}

void checkSmall(int k, int cnt) {
    if (k>n) {
        if (cnt>res2) res2=cnt;
        return ;
    }

    set<float>::iterator it;
    float save;

    for (int i=1; i<=n; ++i)
        if (!mark[i]) {
            mark[i]=true;
            pa[k]=a[i];

            it=sb.upper_bound(pa[k]);
            if (it==sb.end()) it=sb.begin();
            save=*it;
            sb.erase(it);

            checkSmall(k+1,save<pa[k] ? cnt+1 : cnt);

            mark[i]=false;
            sb.insert(save);
        }
}

int solveSmall() {
    res2=0;

    for (int i=1; i<=n; ++i) mark[i]=false;

    sb.clear();
    for (int i=1; i<=n; ++i) sb.insert(b[i]);

    checkSmall(1,0);

    return res2;
}

int solveBig() {
    sb.clear();
    for (int i=1; i<=n; ++i) sb.insert(b[i]);

    res2=0;

    set<float>::iterator it;
    for (int i=1; i<=n; ++i) {
        it=sb.upper_bound(a[i]);
        if (it==sb.end()) it=sb.begin();
        if (*it<a[i]) ++res2;
        sb.erase(*it);
    }

    return res2;
}

int main() {
    freopen("D-large.in","r",stdin);
    freopen("output1.txt","w",stdout);

    scanf("%d",&tcase);

    for (int tid=1; tid<=tcase; ++tid) {
        scanf("%d",&n);
        for (int i=1; i<=n; ++i) scanf("%f",&a[i]);
        for (int i=1; i<=n; ++i) scanf("%f",&b[i]);

        sort(a+1,a+n+1);
        sort(b+1,b+n+1);

        //printf("Case #%d: %d %d\n",tid,solveDeceitful(),n<=10 ? solveSmall() : solveBig());
        printf("Case #%d: %d %d\n",tid,solveDeceitful(),solveBig());
    }

    return 0;
}
