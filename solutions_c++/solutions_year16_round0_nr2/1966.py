#include<bits/stdc++.h>

#define SZ(x) ((int(x.size())))

typedef long long ll;
typedef long double ld;

using namespace std;

int t, ans;
string s;

int main()
{
    ios::sync_with_stdio(0);
    ifstream in;
    ofstream out;
    in.open ("B-large.in", ios::in);
    out.open ("B-large.out", ios::out);
    in >> t;
    for (int i = 0; i < t; i++)
    {
        in >> s;
        ans = 0;
        for (int j = 1; j < s.length(); j++)
        {
            if (s[j] != s[j - 1])
                ans++;
        }
        if (s[s.length() - 1] == '-')
            ans++;
        out << "Case #" << i + 1 << ": " << ans << endl;
    }
    in.close();
    out.close();
	return 0;
}
