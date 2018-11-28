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

void reverse_pancake(vi &v, int n)
{
    reverse(v.begin(), v.begin() + n);

    for (int i = 0; i < n; i++)
        v[i] = 1 - v[i];
}

int main()
{
    int T;

    cin >> T;
    for (int cas = 1; cas <= T; cas++) {
        string str;
        cin >> str;
        vi v(str.size(), 0);
        for (int i = 0; i < str.size(); i++) {
            if (str[i] == '+')
                v[i] = 1;
        }
        // cout << v << endl;

        int B = v.size();
        int ans = 0;

        while (B) {
            if (v[B-1] == 1) {
                B--;
                continue;
            }
            if (v[0] == 0) {
                reverse_pancake(v, B);
                ans++;
                B--;
            } else {
                int C;
                for (int i = 0; i < B; i++) {
                    if (v[i] == 0) {
                        C = i;
                        break;
                    }
                }
                reverse_pancake(v, C);
                reverse_pancake(v, B);
                ans += 2;
                B--;
            }
        }

        cout << "Case #" << cas << ": " << ans << endl;
    }

	return 0; 
}
