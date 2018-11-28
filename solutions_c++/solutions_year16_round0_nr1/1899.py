#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define ull unsigned long long
#define mp make_pair
#define pb push_back
#define RI(x) scanf("%d", &x)
#define RL(x) scanf("%I64d", &x)
#define RD(x) scanf("%f", &x)

unordered_set<int> s;

void solve(int case_number)
{
    s.clear();
    int n, k, temp;
    cin >> n;
    if (n == 0)
    {
        cout << "Case #" << case_number << ": INSOMNIA\n";
        return;
    }
    k = 0;
    do {
        k += n;
        temp = k;
        while (temp > 0)
        {
            s.insert(temp % 10);
            temp /= 10;
        }
    } while(s.size() < 10);
    cout << "Case #" << case_number << ": " << k << "\n";
}

int main()
{
    freopen("input1.in", "r", stdin);
    freopen("output1.out", "w", stdout);
    int t;
    cin >> t;
    for (int i=1; i<=t; ++i)
        solve(i);

    return 0;
}

