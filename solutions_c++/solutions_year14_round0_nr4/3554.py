#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <set>
using namespace std;

const double eps = 1e-8;
const int N = 1010;

int cal(int a[],int b[],int n)
{
    int visit[N];
    memset(visit,0,sizeof(visit));
    int ans = 0;
    for(int i = 1; i <= n; i ++) {
        int find = -1;
        for(int j = 1; j <= n; j ++) {
            if(visit[j]) continue;
            if(b[j] > a[i]) {
                find = j;
                break;
            }
        }
        if(find == -1) {
            for(int j = 1; j <= n; j ++)
                if(!visit[j]) {
                    visit[j] = 1;
                    break;
                }
            ans ++;
        }
        else visit[find] = 1;
    }
    return ans;
}

int cal2(int a[],int b[],int n)
{
    set<int> st;
    for(int i = 1; i <= n; i ++) st.insert(b[i]);
    int ans = 0;
    for(int i = 1; i <= n; i ++) {
        if(a[i] > *st.begin()) {
            ans ++;
            st.erase(st.begin());
        }
        else {
            set<int>::iterator it = st.end();
            it --;
            st.erase(it);
        }
    }
    return ans;
}

void solve()
{
    int a[N],b[N];
    double x;
    int n;
    scanf("%d",&n);
    for(int i = 1; i <= n; i ++) {
        scanf("%lf",&x);
        a[i] = 100000 * (x + eps);
    }
    for(int i = 1; i <= n; i ++) {
        scanf("%lf",&x);
        b[i] = 100000 * (x + eps);
    }
    sort(a + 1,a + n + 1);
    sort(b + 1,b + n + 1);
    //for(int i = 1; i <= n; i ++) cout << a[i] << " ";
    //cout << endl;
    //for(int i = 1; i <= n; i ++) cout << b[i] << " ";
    //cout << endl;
    int ans1 = 0,ans2 = 0;
    ans1 = ans2 = cal(a,b,n);
    for(int i = 0; i < n; i ++) {
        int aa[N],bb[N];
        for(int j = i + 1, k = 0; j <= n; j ++) {
            aa[++ k] = a[j];
        }
        for(int j = 1, k = 0; j <= n - i; j ++) {
            bb[++ k] = b[j];
        }
        ans1 = max(ans1,cal2(aa,bb,n - i));
    }
    printf("%d %d\n",ans1,ans2);
}

int main()
{
    freopen("D-large.in","r",stdin);
    freopen("D-large.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int cas = 1; cas <= t; cas ++) {
        printf("Case #%d: ",cas);
        solve();
    }
    return 0;
}
