#include <bits/stdc++.h>
#define for0(i, n) for(int i = 0; i < n; i++)
#define for1(i, n) for(int i = 1; i <= n; i++)
#define pb push_back
#define mp make_pair
#define all(v) v.begin(), v.end()
#define V vector<int>
#define VP vector<pair<int, int> >
#define clr(A, x) memset(A, x, sizeof(A))
#define cpy(A, B) memcpy(A, B, sizeof(B))
#define g(s) getline(cin, s) ///ai grija la fin/cin ///
#define FASTIO ios_base::sync_with_stdio(0)
const long long INFLL = (1LL<<62);
const int INFINT = 2000000000;
typedef long long ll;
typedef unsigned long long ull;
using namespace std;
/*template <typename T>
string to_string(const T& n){
    ostringstream os;
    os << n;
    return os.str();
}
*/
/*void invers_modular(int a, int b, int &d, int &x, int &y)
{
    if(!b)
    {
        d=a;
        x=1;
        y=0;
        return ;
    }
    int x0, y0;
    invers_modular(b, a%b, d, x0, y0);
    x=y0;
    y=x0-a/b*y0;
}*/ // daca x<0 se aduna cu mod pana e mai mare, x fiind rezultatul

/*ull putere(ull baza, ull exponent, ull MOD)
{
    if(exponent == 0) return 1;
    if(exponent % 2 == 0) return putere((baza * baza) % MOD, exponent / 2, MOD) % MOD;
    return ((baza % MOD) * (putere(baza, exponent - 1, MOD) % MOD) % MOD);
}*/
//ifstream fin("A-large.in"); /// modifica cu numele corespunzator
//ofstream fout("A-large.out"); /// modifica cu numele corespunzator

const int NMAX = 1e3 + 5;


int t, n, k;
int v[NMAX], bit[NMAX];

#define lsb(x) (x & (-x))

void upd(int pos, int val)
{
    for(; pos <= n; pos += lsb(pos))
        bit[pos] += val;
}

void upd2(int start, int finish)
{
    upd(start, 1);
    upd(finish + 1, -1);
}

int query(int pos)
{
    int ret = 0, temp = pos;
    for(; pos > 0; pos -= lsb(pos))
        ret += bit[pos];
    return (ret + v[temp]) % 2;
}

int main()
{
    cin >> t;
    for1(nr_t, t)
    {


        string s;
        cin >> s;
        n = s.size();
        for0(i, s.size())
            v[i + 1] = (s[i] == '-' ? 0 : 1), bit[i + 1] = 0;
        cin >> k;

        int sol = 0;
        for1(i, n - k + 1)
            if(query(i) == 0)
            {
                sol++;
                upd2(i, i + k - 1);
            }

        cout << "Case #" << nr_t << ": ";
        for(int i = n - k + 1; i <= n; i++)
            if(query(i) == 0)
            {
                cout << "IMPOSSIBLE\n";
                goto SKIP;
            }
        cout << sol << '\n';


        SKIP: ;
    }


    return 0;
}
