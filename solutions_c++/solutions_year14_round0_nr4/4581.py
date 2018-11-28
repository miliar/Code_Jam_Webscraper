#include <bits/stdc++.h>

#define rep(i,n) for(int i=0; i<n; i++)
#define repa(i,a,b,d) for(int i=a; i<=b; i+=d)
#define repd(i,a,b,d) for(int i=a; i>=b; i-=d)
#define repi(it,stl) for(auto it = (stl).begin(); (it)!=stl.end(); ++(it))
#define sz(a) ((int)(a).size())
#define mem(a,n) memset((a), (n), sizeof(a))
#define all(n) (n).begin(),(n).end()
#define rall(n) (n).rbegin(),(n).rend()
#define mp(a,b) make_pair((a),(b))
#define pii pair<int,int>
#define vi vector<int>
#define vs vector<string>
#define sstr stringstream
#define myfind(v,x) (find(all((v)),(x))-(v).begin())

typedef long long ll;
using namespace std;

int n;
ll num1[2000], num2[2000];

int de()
{
    int st1 = 0, en1 = n - 1, en2 = n - 1;
    int res = 0;
    while(st1 <= en1) {
        if(num1[en1] > num2[en2]) {
            --en1, --en2;
            ++res;
        } else
            st1++, en2--;
    }
    return res;
}
int war()
{
    int  en1 = n - 1, en2 = n - 1, st2 = 0;
    int res = 0;
    while(en1 >= 0) {
        if(num1[en1] > num2[en2]) {
            ++res;
            ++st2, --en1;
        } else
            --en2, --en1;
    }
    return res;
}
int main()
{

#ifndef ONLINE_JUDGE
    freopen("code.txt", "rt", stdin);
    freopen("out.txt", "wt", stdout);
#endif

    int tst;
    scanf("%d", &tst);
    repa(tt, 1, tst, 1) {
        scanf("%d", &n);
        double d;
        rep(i, n) {
            scanf("%lf", &d);
            num1[i] = (ll)(d * 1e7);
        }
        rep(i, n) {
            scanf("%lf", &d);
            num2[i] = (ll)(d * 1e7);
        }
        sort(num1, num1 + n);
        sort(num2, num2 + n);
        int x = de(), y = war();
        printf("Case #%d: %d %d\n", tt, x, y);

    }
    return 0;
}
