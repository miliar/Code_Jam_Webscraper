#include <bits/stdc++.h>
#define pb push_back
#define f first
#define s second
#define ll long long
#define pii pair<int,int>
#define pll pair<ll,ll>
#define pdd pair<double,double>
using namespace std;
int _main()
{
    int ans = 0, cnt = 0;
    string str;
    cin >> str;
    str = "+" + str;
    str += "+";
    for(int i = 1; i < str.size(); i++)
    {
        if(str[i] == '+' && str[i-1] == '-')
        {
            if(cnt == 0)ans++;
            else ans += 2;
            cnt++;
        }
        else if(str[i] == '+')cnt++;
    }
    return ans;
}
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int tt;
    cin >> tt;
    for(int i = 1; i <= tt; i++)
    {
        cout << "Case #" << i << ": " << _main() << "\n";
    }
    return 0;
}
