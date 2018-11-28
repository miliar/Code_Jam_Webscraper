#include <bits/stdc++.h>

#define all(a) (a).begin(), (a).end()
#define sz(a) (int)(a).size()
#define pb push_back
#define mp make_pair
#define int __int128

using namespace std;

mt19937 rr(random_device{}());

string conv(int x)
{
    string s = "";
    while (x) {
        s += (char)(x % 2 + '0');
        x /= 2;
    }
    reverse(all(s));
    return s;
}

string conv10(int x)
{
    string s = "";
    while (x) {
        s += (char)(x % 10 + '0');
        x /= 10;
    }
    reverse(all(s));
    return s;
}

int conv(const string& s, int base)
{
    int ans = 0;
    for (int i = 0; i < sz(s); ++i) {
        ans *= base;
        ans += (s[i] - '0');
    }
    return ans;
}

bool isPrime(int x)
{
    for (int i = 2; i * i <= x && i <= 100500; ++i) {
        if (x % i == 0) {
            return false;
        }
    }
    return true;
}

int divisor(int x)
{
    for (int i = 2; i * i <= x && i <= 100500; ++i) {
        if (x % i == 0) {
            return i;
        }
    }
    return 1;
}

main()
{
	
	ofstream cout("output.txt");
    
    int n = (1LL << 32);
    
    set<string> ans;
    
    while (sz(ans) < 500) {
        int x = (rr() % n);
        if (!x) {
            continue;
        }
        string s = conv(x);
        if (sz(s) < 32 || s.back() != '1') {
            continue;
        }
        bool ok = true;
        for (int base = 2; base <= 10; ++base) {
            int val = conv(s, base);
            if (isPrime(val)) {
                ok = false;
                break;
            }
        }
        if (ok) {
            ans.insert(s);
        }
    }
    
    cout << "Case #1:\n";
    for (auto& it : ans) {
        string s = it;
        cout << s << " ";
        for (int base = 2; base <= 10; ++base) {
            int val = conv(s, base);
            cout << conv10(divisor(val)) << " ";
        }
        cout << "\n";
    }

}
