#include <fstream>
#include <sstream>
#include <algorithm>
#include <vector>
using namespace std;

ifstream cin("in");
ofstream cout("out");

const int N = 100;
int t[N][N], h[N], v[N], c;

void solve(int cs)
{
    int a, b;
    cin >> a >> b;
    for (int i = 0; i < a; i++)
        h[i] = 0;
    for (int i = 0; i < b; i++)
        v[i] = 0;
    c = 0;
    for (int i = 0; i < a; i++)
        for (int j = 0; j < b; j++) {
            cin >> t[i][j];
            if (t[i][j] == 1) {
                h[i]++;
                v[j]++;
                c++;
            }
        }
    for (int i = 0; i < a; i++)
        if (h[i] == b)
            for (int j = 0; j < b; j++)
                if (t[i][j] == 1) {
                    t[i][j] = 2;
                    c--;
                }
    for (int i = 0; i < b; i++)
        if (v[i] == a)
            for (int j = 0; j < a; j++)
                if (t[j][i] == 1) {
                    t[j][i] = 2;
                    c--;
                }
    cout << "Case #" << cs << ": " << (c == 0 ? "YES" : "NO") << endl;
}

int main()
{
    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
        solve(i + 1);
    return 0;
}
