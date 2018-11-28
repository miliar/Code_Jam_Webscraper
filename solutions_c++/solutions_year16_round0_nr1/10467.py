#include<bits/stdc++.h>
#define int long long

using namespace std;

set<int> st;
void solve(int n, int number)
{
    st.clear();
    int x = n, ans;
    for(int i = 1; i <= 75 && (int)st.size() < 10; i++)
    {
        int t = n;
        ans = i;
//        cout << n << endl;
        if(t == 0)
            st.insert(0);
        while(t)
        {
            st.insert(t % 10);
            t /= 10;
        }
        if((int)st.size() < 10)
            n += x;
    }
    if(st.size() == 10)
    {
        printf("Case #%I64d: %I64d\n", number, n);
    }
    else
    {
        printf("Case #%I64d: INSOMNIA\n", number);
    }
}
main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t, n;
    scanf("%I64d", &t);
    for(int test = 1; test <= t; test++)
    {
        scanf("%I64d", &n);
        solve(n, test);
    }
}
