#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace std;
using namespace __gnu_pbds;

#define INF (1<<30)
#define F first
#define S second
#define mkp(a, b) make_pair(a, b)

typedef long long llong;
typedef long double ldouble;

#define FOR(I, A, B) for(int (I) = (A); (I) < (B); (I)++)
#define ROF(I, A, B) for(int (I) = (A); (I) >= (B); (I)--)
#define SQR(A) (A)*(A)

typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> ordered_set;

const char array_sep[] = " ";
const char array_end[] = "";

const char pair_sep[] = " ";
const char pair_end[] = "\n";

const char map_sep[] = "->";
const char map_end[] = "\n";

const int dx[] = {-1, 0, 1, 0};
const int dy[] = {0, 1, 0, -1};
const int ddx[] = {-1, -1, 0, 1, 1, 1, 0, -1};
const int ddy[] = {0, 1, 1, 1, 0, -1, -1, -1};

template<typename A> ostream & operator<<(ostream & os, const vector<A> & x)
{
    for(int i = 0; i < x.size(); i++)
        os << x[i] << array_sep;
    os << array_end;
    return os;
}

template<typename A, typename B> ostream & operator<<(ostream & os, const pair<A, B> & x)
{
    os << x.first << pair_sep << x.second << pair_end;
    return os;
}

template<typename A> istream & operator>>(istream & is, vector<A> & x)
{
    for(int i = 0; i < x.size(); i++)
        is >> x[i];
    return is;
}

template<typename A, typename B> istream & operator>>(istream & is, pair<A, B> & x)
{
    is >> x.first >> x.second;
    return is;
}

template<typename _key, typename _val> ostream & operator<<(ostream & os, map<_key, _val> & mp)
{
    for(auto it : mp)   // not for C++98 or earlier
        os << it->F << map_sep << it->S << map_end;
    return os;
}

void prnt(int t, int x)
{
    cout << "Case #" << t << ": " << x << endl;
}


int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
//    freopen("errlog.log", "w", stderr);
//   	ios_base::sync_with_stdio(0);

    register int T;
    cin >> T;
    for(int test = 1; test <= T; test++)
    {
//        cerr << test << endl;
        string s;
        cin >> s;

		int r = s.size() - 1, res = 0;
        while(r >= 0)
		{
//			cerr << r << endl;
//			cerr << s << " ";
            for(; r >= 0 && s[r] != '-'; r--);
            if(r < 0)
				break;
			if(s[0] == '+')
			{
				res++;
				for (int i = 0; s[i] == '+'; i++)
                    s[i] = '-';
			}

			res++;
			int t = '+' + '-';

            for(int i = 0, j = r; i <= j; i++, j--)
			{
                swap(s[i], s[j]);
				s[i] = t - s[i];
				if(i != j)
					s[j] = t - s[j];
			}
//			cerr << s << endl;
		}
        prnt(test, res);
    }


    return 0;
}
