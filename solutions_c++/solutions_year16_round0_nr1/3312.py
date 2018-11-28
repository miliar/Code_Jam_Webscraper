#include <bits/stdc++.h>
#include <windows.h>

#define f first
#define s second
#define ll long long
#define ld long double
#define pb push_back
#define files1 freopen("input.txt","r",stdin)
#define files2 freopen("output.txt","w",stdout)
#define mp make_pair
#define fast_io ios_base::sync_with_stdio(0);
#define forn() for(int i=0;i<n;i++)
#define pii pair<int,int>
#define vi vector<int>

using namespace std;

const int inf=2e9;
const double eps=1e-9;
const int maxn = 3e5 + 500, base = 1e9+7;

vector<int> get_numbers(ll x)
{
    vector<int> ans;
    if (x == 0){
        ans.pb(0);
        return ans;
    }
    while (x > 0){
        ans.pb(x % 10);
        x /= 10;
    }
    return ans;
}
void solve()
{
    int n;
    scanf("%d", &n);
    if (n == 0){
        puts("INSOMNIA");
        return;
    }

    bool used[10];
    int cnt = 0;
    memset(used, 0, sizeof(used));
    vector<int> numbers;
    for (int i=1;;i++){
        ll cur = 1LL * n * i;
        numbers = get_numbers(cur);
        for (int j=0;j<numbers.size();j++){
            int num = numbers[j];
            if (!used[num]){
                cnt++;
                used[num] = 1;
            }
        }
        if (cnt == 10){
            printf("%I64d\n", cur);
            return;
        }
    }
}
int main()
{
    files1;
    files2;
    int t;
    scanf("%d", &t);
    for (int i=1;i<=t;i++){
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}
