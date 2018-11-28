#include <bits/stdc++.h>
using namespace std;
#define MAX 50009
#define ll long long

ll fn(ll length, ll c);
string gn(string x, int n);
ll powr(ll base, ll p);

ll arr[1005];

int main()
{
     freopen("D-small-attempt6.in", "r", stdin);
    freopen("c.out", "w", stdout);

    int tc, cases = 1;
    scanf("%d", &tc);

    while(tc--)
    {
        int length, k, s;
        scanf("%d %d %d", &length, &k, &s);

        int ans = fn(length, k - 1);
        printf("Case #%d:", cases++);

        // if(ans > s)
        //   printf(" IMPOSSIBLE");
        // else
        for(ll i = 0; i < min(s, length); i++)
            printf(" %lld", i + 1);

        printf("\n");
    }

    /*  cout << gn("gll", 5)[5] << endl;
      cout << gn("lgl", 5)[5] << endl;
      cout << gn("llg", 5)[5] << endl;
    */
    /* cout << gn("glllll", 1) << endl;
     cout << gn("lgllll", 1)[1] << endl;
     cout << gn("llglll", 1)[15] << endl;
     cout << gn("lllgll", 1)[15] << endl;
     cout << gn("llllgl", 1)[29] << endl;
     cout << gn("lllllg", 1)[29] << endl << endl << endl;
     */

    return 0;
}

ll fn(ll length, ll c)
{
    c++;
    ll h = c;
    ll total = (length / c) + (length % c != 0);
    ll step = length / total + (length % total != 0);
    // printf("%lld\n", step);
    ll i2 = 1;
    int k = 0;

    for(int i = 1; i <= total; i++, i2 += step)
    {
        i2 = min(i2, length);
        ll p = i2;
        //printf("i %lld\n ", p);

        ll c = i2 + 1;
        c = min(c, length);

        for(ll j = 1; j < step && p <= powr(length, h); j++)
            p = (p - 1) * length + c, c++; //printf("%lld\n", p);;

        arr[k++] = min(p, powr(length, h));
        //printf("%lld\n", p);
    }

    return total;
}


string gn(string x, int n)
{
    string a = x;
    string b = "";

    for(int i = 0; i < n; i++)
    {
        if(i % 2 == 0)
        {
            b = "";
            for(int j = 0; j < a.length(); j++)
            {
                if(a[j] == 'l')
                    b += x;
                else
                    for(int k = 0; k < x.length(); k++)
                        b += "g";
            }

        }
        else
        {
            a = "";
            for(int j = 0; j < b.length(); j++)
            {
                if(b[j] == 'l')
                    a += x;
                else
                    for(int k = 0; k < x.length(); k++)
                        a += "g";
            }

        }
    }

    return n % 2 == 0 ? a : b;
}


ll powr(ll base, ll p)
{
    ll ret = 1;
    for(ll i = 0; i < p; i++)
        ret *= base;
    return ret;
}
