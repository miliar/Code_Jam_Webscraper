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

string hex_to_bin(int n)
{
    string s;

    if (n == 0)
        s = "0";

    while (n) {
        s.push_back('0' + n % 2);
        n /= 2;
    }

    while (s.size() < 14)
        s.push_back('0');

    s.push_back('1');
    reverse(all(s));
    s.push_back('1');

    return s;
}

long long str_to_num(string str, int n)
{
    long long ret = str[0] - '0';

    for (int i = 1; i < str.size(); i++) {
        ret = ret * n;
        if (str[i] == '1')
            ret += 1;
    }

    return ret;
}

int get_factor(long long n)
{
    for (int i = 2; i <= sqrt(n+1); i++) {
        if (n % i == 0)
            return i;
    }

    return 0;
}

int main()
{
    vs jamcoin;
    vvi factor;
    vector<long long> value;

    cout << "Case #1:" << endl;

    for (int i = 0; i < (1 << 14); i++) {
        string str = hex_to_bin(i);
        vi f(0);
        // cout << str << endl;

        for (int i = 2; i <= 10; i++) {
            long long n = str_to_num(str, i);
            int d = get_factor(n);
            // cout << i << ": " << n << ": " << d << endl;

            if (d == 0) {
                break;
            }

            f.push_back(d);
        }

        if (f.size() == 9) {
            jamcoin.push_back(str);
            factor.push_back(f);
        }

        if (jamcoin.size() >= 50)
            break;
    }

    for (int i = 0; i < jamcoin.size(); i++) {
        cout << jamcoin[i] << " " << factor[i] << endl;
    }


	return 0; 
}
