#include <bits/stdc++.h>

using namespace std;

#define MAX 100005;
#define INF 0x3f3f3f3f
#define MOD 1000000007
#define PI 3.14159265359
#define pb push_back
#define ppb pop_back()
#define sz size()
#define fi first
#define se second
#define all(c) (c).begin(), (c).end()

typedef unsigned long long ull;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vii;
typedef vector<string> vs;
typedef pair<int,int> pii;

int t, a, b, k;

int main()
{
    //freopen("input.txt", "r", stdin);
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.ou", "w", stdout);
    cin >> t;

    for(int test = 1 ; test <= t ; test++)
    {
        int ret = 0;
        cin >> a >> b >> k;
        for(int i = 0 ; i < a ; i++)
            for(int j = 0 ; j < b ; j++)
                if((i & j) < k)
                    ret++;
        cout << "Case #" << test << ": " << ret << endl;
    }
    return 0;
}
