#include<bits/stdc++.h>

#define SZ(x) ((int(x.size())))

typedef long long ll;
typedef long double ld;

using namespace std;

int t, cnt;
bool flg, mark[10];
ll n, tmp, m;

int main()
{
    ios::sync_with_stdio(0);
    ifstream in;
    ofstream out;
    in.open ("A-large.in", ios::in);
    out.open ("A-large.out", ios::out);
    in >> t;
    for (int i = 0; i < t; i++)
    {
        cnt = 0;
        flg = 0;
        memset (mark, 0, sizeof mark);
        in >> n;
        if (n == 0)
        {
            out << "Case #" << i + 1 << ": INSOMNIA" << endl;
            continue;
        }
        m = n;
        for (int j = 0; j < 2000; j++, m += n)
        {
            tmp = m;
            while (tmp > 0)
            {
                if (!mark[tmp % 10])
                {
                    cnt++;
                    mark[tmp % 10] = 1;
                }
                tmp /= 10;
            }
            if (cnt == 10)
            {
                out << "Case #" << i + 1 << ": " << m << endl;
                flg = 1;
                break;
            }
        }
        if (!flg)
            out << "Case #" << i + 1 << ": INSOMNIA" << endl;
    }
    in.close();
    out.close();
	return 0;
}
