#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>

using namespace std;

#define pb push_back
#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define sz size()
#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define rep2(i,n,m) for(int i=n;i<(int)(m);i++)
#define For(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define dot(a,b) ((conj(a)*(b)).X)
#define X real()
#define Y imag()
#define length(V) (hypot((V).X,(V).Y))
#define vect(a,b) ((b)-(a))
#define cross(a,b) ((conj(a)*(b)).imag())
#define normalize(v) ((v)/length(v))
#define rotate(p,about,theta) ((p-about)*exp(point(0,theta))+about)
#define pointEqu(a,b) (comp(a.X,b.X)==0 && comp(a.Y,b.Y)==0)

typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vector<int> > vii;
typedef long long ll;
typedef long double ld;
typedef complex<double> point;
typedef pair<point, point> segment;
typedef pair<double, point> circle;
typedef vector<point> polygon;

const int oo = (int) 1e9;
const double PI = 2 * acos(0);
const double eps = 1e-9;

inline int comp(const double &a, const double &b) {
        if (fabs(a - b) < eps)
                return 0;
        return a > b ? 1 : -1;
}

int di[] = { 1, -1, 0, 0, 1, -1, 1, -1 };
int dj[] = { 0, 0, 1, -1, 1, -1, -1, 1 };
int diK[] = { -2, -2, -1, 1, 2, 2, 1, -1 };
int djK[] = { -1, 1, 2, 2, 1, -1, -2, -2 };

int I, J;

inline bool val(const int &i, const int &j) {
        if (i < 0 || j < 0 || i >= I || j >= J)
                return false;
        return true;
}

uint64_t conv_bits_to_base(int bits, int jamcoin_N, int base)
{
    uint64_t result = 0;
    for (int i = 0; i < jamcoin_N; ++i) {
        if (1<<i & bits) {
            if (i == 0) {
                result += 1;
                continue;
            }
            uint64_t to_add = 1;
            for (int j = 0; j < i; ++j) {
                to_add *= base;
            }
            result += to_add;
        }
    }
    return result;
}
string conv_bits_to_string(int bits, int jamcoin_N)
{
    string result (jamcoin_N, '0');
    for (int i = 0; i < jamcoin_N; ++i) {
        if (bits & 1 << i) {
            result[jamcoin_N - i - 1] = '1';
        }
    }
    return result;
}

bool is_prime(uint64_t number, uint64_t& divsor)
{
    if (number<2)
        return false;
    if (number == 2)
        return true;
    if (number%2==0) {
        divsor = 2;
        return false;
    }
    for(int i=3;i<=sqrt(number);i += 2)
    {
        if (number%i==0) {
            divsor = i;
            return false;
        }
    }
    return true;
}

void solve(int jamcoin_N, int J)
{
    uint64_t trial = 1;
    trial |= (1<<(jamcoin_N-1));
    cout << endl;
    for (; trial < 1 << jamcoin_N; ++trial)
    {
        if (!(trial & 1<<0))
            continue;
        if (!(trial & (1<<(jamcoin_N-1))))
            continue;
        std::list<uint64_t> v;
        std::list<uint64_t> n_base;
        bool got_n = false;
        for (int base = 2; base <= 10; ++base) {
            uint64_t n = conv_bits_to_base(trial, jamcoin_N, base);

            uint64_t divsor = 0;
            if (is_prime(n, divsor)) {
                got_n = false;
                break;
            }
            n_base.push_back(n);
            v.push_back(divsor);
            got_n = true;
        }
        if (got_n) {
            J--;
            string s = conv_bits_to_string(trial, jamcoin_N);
            cout << s << " ";
            For (it, v) {
                cout << *it << " ";
            }
            cout << endl;
            if (J == 0)
                break;
        }
    }
}
int N;
int main(int argc, char *args[]) {
    if (argc == 2 && strcmp(args[1], "small") == 0) {
        freopen("C-small-attempt0.in","rt",stdin);
        freopen("C-small-attempt0.out","wt",stdout);
    }
    else if (argc == 2 && strcmp(args[1], "large") == 0) {
        freopen("C-large.in","rt",stdin);
        freopen("C-large.out","wt",stdout);
    }
    else {
        freopen("a.txt", "rt", stdin);
    }

    cin>>N;
    rep2(nn,1,N+1) {
        printf("Case #%d: ", nn);
        int jamcoin_N,J;
        cin >> jamcoin_N >> J;
        solve(jamcoin_N, J);
        cout<<endl;
    }

    return 0;
}
