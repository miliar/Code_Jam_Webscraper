#include <iostream>
#include <string>
#include <cmath>
#include <vector>

using namespace std;

bool palind(long long p)
{
    string t;
    while (p)
    {
        t += char((p % 10) + '0');
        p /= 10;
    }
    for (int i = 0; i < t.length() / 2; i++)
        if (t[i] != t[t.length() - i - 1])
            return false;
    return true;
}
vector<long long> pals;
int toInt(string k)
{
    int p = 0;
    for (int i = 0; i < k.length(); i++)
        p = p * 10 + k[i] - '0';
    return p;
}
void makePals(int len, string num)
{
    if (len == 0)
    {
        if (num[0] != '0')
            pals.push_back(toInt(num));
        return;
    }
    for (int i = 0; i <= 9; i++)
    {
        if (len % 2 == 0)
        {
            string n = "";
            n += char(i + '0');
            n += num;
            n += char(i + '0');
            makePals(len - 2, n);
        }
        else
        {
            string n = "";
            n += char(i + '0');
            makePals(len - 1, n);
        }
    }

}
int main()
{
    int t;
    cin >> t;
    for (int tt = 0; tt < t; tt++)
    {
        long long a, b;
        cin >> a >> b;
        long long s = sqrt(a), f = sqrt(b);
        int lp = 0, sp = 0;
        while (f)
        {
            f /= 10;
            lp++;
        }
        while (s)
        {
            s /= 10;
            sp++;
        }
        pals.clear();
        for (int i = sp; i <= lp; i++)
            makePals(i, "");
        int cnt = 0;
        for (int i = 0; i < pals.size(); i++)
            if (pals[i] * pals[i] >= a && pals[i] * pals[i] <= b && palind(pals[i] * pals[i]))
                cnt++;
        cout << "Case #" << tt + 1 << ": " << cnt << endl;
    }
}
