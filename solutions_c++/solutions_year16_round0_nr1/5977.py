#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<string> vs;
typedef vector<vs> vvs;

#define pb(x) push_back(x)
#define all(c) (c).begin(),(c).end()
#define ins(c) inserter((c),(c).begin())
#define mp(x,y) make_pair((x),(y))
#define mt(x,y,z) make_tuple((x),(y),(z))
#define INF (1e9)
const double PI = 2 * acos(0.0);

ostream& operator<<(ostream& out, vi v)
{
    for (auto a: v)
        out << a << " ";
    return out;
}

void add_digits(set<int>& S, long long n)
{
    if (n == 0) {
        S.insert(0);
        return;
    }

    while (n) {
        S.insert(n % 10);
        n /= 10;
    }
}

int main()
{
    int T, n;

    cin >> T;
    for (int cas = 1; cas <= T; cas++) {
        cin >> n;
        if (n == 0) {
            cout << "Case #" << cas << ": INSOMNIA" << endl;
            continue;
        }

        long long a = 0;
        set<int> S;

        while (S.size() < 10) {
            a += n;
            add_digits(S, a);

            /*
            cout << "a = " << a << endl;
            for (auto b: S)
                cout << b << " ";
            cout << endl;
            */
        }

        cout << "Case #" << cas << ": " << a << endl;

    }

	return 0; 
}
