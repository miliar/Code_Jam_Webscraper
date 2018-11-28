#include <cstdio>
#include <iostream>
#include <set>

using namespace std;

typedef long long int LL;

set<int> fac(LL x)
{
    set<int> ans;
    while(x) {
        ans.insert(x%10);
        x /= 10;
    }
    return ans;
}

LL solve(LL x)
{
    // cout << "fac " << x << ": ";
    LL t;
    set<int> ans;
    for(t=x;;t+=x) {
        set<int> u = fac(t);
        for(auto s:u) ans.insert(s);
        if(ans.size()==10) break;
    }
    // cout << t << endl;
    return t;
}

// void test(void)
// {
//     for(int i=1;i<=1000000;++i)
//         solve(i);
// }

int main(void)
{
    // test();
    int T; scanf("%d",&T);
    for(int t=1;t<=T;++t) {
        cout << "Case #" << t << ": ";
        LL x; cin >> x;
        if(x==0) cout << "INSOMNIA" << endl;
        else cout << solve(x) << endl;
    }
    return 0;
}
