#include <cstring>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>

using namespace std;

#define pb push_back
#define sz(a) (int)a.size()
#define fs first
#define sc second

typedef long long ll;
typedef pair<int,int> ii;

struct gt {
    int x; char val;
    gt(int _x = 0, char _val = '1') {
        x = _x;
        val = _val;
    }
};

gt n[500][500], c[500][500], sum[100005];
char s[100000], s2[100005];
int L, x, st[100005];

void init() {
    n['1']['1'] = gt(0,'1');
    n['1']['i'] = gt(0,'i');
    n['1']['j'] = gt(0,'j');
    n['1']['k'] = gt(0,'k');
    ///////////////
    n['i']['1'] = gt(0,'i');
    n['i']['i'] = gt(1,'1');
    n['i']['j'] = gt(0,'k');
    n['i']['k'] = gt(1,'j');
    ////////////////
    n['j']['1'] = gt(0,'j');
    n['j']['i'] = gt(1,'k');
    n['j']['j'] = gt(1,'1');
    n['j']['k'] = gt(0,'i');
    ////////////////
    n['k']['1'] = gt(0,'k');
    n['k']['i'] = gt(0,'j');
    n['k']['j'] = gt(1,'i');
    n['k']['k'] = gt(1,'1');
    ////////////////
    c['1']['1'] = gt(0,'1');
    c['i']['1'] = gt(0,'i');
    c['j']['1'] = gt(0,'j');
    c['k']['1'] = gt(0,'k');
    ////////////////
    c['i']['i'] = gt(0,'1');
    c['1']['i'] = gt(1,'i');
    c['k']['i'] = gt(0,'j');
    c['j']['i'] = gt(1,'k');
    ////////////////
    c['j']['j'] = gt(0,'1');
    c['k']['j'] = gt(1,'i');
    c['1']['j'] = gt(1,'j');
    c['i']['j'] = gt(0,'k');
    ////////////////
    c['k']['k'] = gt(0,'1');
    c['j']['k'] = gt(0,'i');
    c['i']['k'] = gt(1,'j');
    c['1']['k'] = gt(1,'k');
}

gt tong(gt a, char b) {
    gt tmp = n[a.val][b];
    tmp.x = (tmp.x+a.x)%2;
    return tmp;
}

gt tru(gt a, gt b) {
    gt tmp = c[a.val][b.val];
    tmp.x = (tmp.x+a.x+b.x)%2;
    return tmp;
}

bool bang(gt a, gt b) {
    return (a.x==b.x && a.val==b.val);
}

int main() {
	freopen("C-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    init();
    int AAA = t;
    while (t--) {
        scanf("%d %d\n",&L,&x);
        scanf("%s\n",s);
        if (L*x < 3) {
            cout << "Case #" << AAA-t << ": NO\n";
            continue;
        }
        for (int i = 0; i < L*x; ++i)
            s2[i] = s[i%L];
        for (int i = 0; i < L*x; ++i)
            s[i] = s2[i];
        L = L*x;
        sum[0] = gt(0,s[0]);
        for (int i = 1; i < L; ++i)
            sum[i] = tong(sum[i-1],s[i]);
        st[0] = 0;
        for (int i = 2; i < L; ++i)
            if (bang(tru(sum[L-1],sum[i-1]),gt(0,'k')))
                st[++st[0]] = i;
        int j = 1; bool b = false;
        for (int i = 1; i < L; ++i)
        if (bang(sum[i-1],gt(0,'i'))) {
            while (j <= st[0] && st[j] <= i) j++;
            for (int k = j; k <= st[0]; ++k)
            if (bang(tru(sum[st[k]-1],sum[i-1]),gt(0,'j'))) {
                b = true;
                break;
            }
            if (b) break;
        }
        if (!b) cout << "Case #" << AAA-t << ": NO\n";
        else cout << "Case #" << AAA-t << ": YES\n";
    }
	return 0;
}
