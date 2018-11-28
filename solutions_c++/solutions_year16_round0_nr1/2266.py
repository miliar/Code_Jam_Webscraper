#include <bits/stdc++.h>

#define all(a) (a).begin(), (a).end()
#define sz(a) (int)(a).size()
#define pb push_back
#define mp make_pair

using namespace std;

int d[10];

typedef long long ll;

bool ok()
{
    for (int i = 0; i < 10; ++i) {
        if (!d[i]) {
            return false;
        }
    }
    return true;
}

void solve(ll x)
{
    while (x)
    {
        d[x % 10] = 1;
        x /= 10;
    }
}

int main()
{
	
	ifstream cin("A-large.in");
	ofstream cout("output.txt");
    
    int tt;
    cin >> tt;
    int c = 1;
    
    while (tt--) {
        cout << "Case #" << c << ": ";
        for (int i = 0; i < 10; ++i) {
            d[i] = 0;
        }
        ll n;
        cin >> n;
        if (n == 0) {
            cout << "INSOMNIA\n";
            ++c;
            continue;
        }
        ll x = 0;
        do {
            x += n;
            solve(x);
        } while (!ok());
        cout << x << "\n";
        ++c;
    }

}
