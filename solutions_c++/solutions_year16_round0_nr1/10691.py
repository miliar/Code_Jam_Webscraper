#include <bits/stdc++.h>

using namespace std;

#define sqr(x) ((x) * (x))
#define pb push_back
#define mp make_pair
#define ins insert
#define er erase
#define bg begin()
#define ed end()
#define X first
#define Y second
#define fin(name) freopen(name, "r", stdin)
#define fout(name) freopen(name, "w", stdout)
#define files(name) fin(name".in"); fout(name".out")
#define enter cout << "\n"
#define space cout << " "
#define endl "\n"
#define fi(st,n) for (int i = (st); i < (n); i++)
#define fj(st,n) for (int j = (st); j < (n); j++)
#define fk(st,n) for (int k = (st); k < (n); k++)
#define fq(st,n) for (int q = (st); q < (n); q++)
#define fw(st,n) for (int w = (st); w < (n); w++)
#define ff(i, st, n) for (int (i) = (st); (i) <= (n); (i)++)
#define ei(st,n) for (int i = (st); i >= (n); i--)
#define ei(st,n) for (int i = (st); i >= (n); i--)
#define ej(st,n) for (int j = (st); j >= (n); j--)
#define ek(st,n) for (int k = (st); k >= (n); k--)
#define clean(a) memset((a),0,sizeof (a));
#define sync ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0)

typedef long long ll;
typedef unsigned long long ull;
typedef double dbl;
typedef long double ldbl;
typedef pair<int, int> pii;
typedef vector<int> vi;

const int inf = (int) 1e9, maxn = (int) 1e5 + 5;
const dbl eps = (dbl) 1e-8;
const int mod = (int) 1000000007;

//cout<<fixed<<setprecision(10);
//srand(time(0));


int main()
{

	sync;
	int n, t;
    fout("A-large.out");
    fin("A-large.in");
	cin >> n;

	fq (0, n)
	{
	    cin >> t;
	    cout << "Case #" << q+1 << ": ";
        set <int> a;
        int k = t, i = 1;
        while (a.size() < 10 && i < 100)
        {

            while (k)
            {
                a.insert(k % 10);
                k /= 10;
            }
            ++ i;
            k = i * t;
        }
        if (i > 98)
            cout << "INSOMNIA" << endl;
        else
            cout << t * (i - 1) << endl;
	}
	return 0;
}
