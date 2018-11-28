#include<bits/stdc++.h>

#define SZ(x) ((int(x.size())))

typedef long long ll;
typedef long double ld;

using namespace std;

int t, k, c, s;

int main()
{
    ios::sync_with_stdio(0);
    ifstream in;
    ofstream out;
    in.open ("D-small-attempt0.in", ios::in);
    out.open ("D-small-attempt0.out", ios::out);
    in >> t;
    for (int i = 0; i < t; i++)
    {
        in >> k >> c >> s;
        out << "Case #" << i + 1 << ":";
        for (int j = 1; j <= k; j++)
            out << " " << j;
        out << endl;
    }
    in.close();
    out.close();
	return 0;
}
