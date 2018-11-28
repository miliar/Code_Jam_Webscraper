#include <bits/stdc++.h>

#define pb push_back
#define mp make_pair
#define fi first
#define prev asfansjfansjabfasjlbfa
#define se second
#define I "%d"
#define II "%d%d"
#define III "%d%d%d"
#define out_files freopen("A-large.in", "r", stdin);freopen("output.txt", "w", stdout)
#define all(x) (x).begin(), (x).end()
#define fast ios_base :: sync_with_stdio(0);

using namespace std;

typedef vector <int> vi;
typedef long long ll;
typedef unsigned long long ull;
typedef pair <int, int> pii;
typedef vector <pii> vii;
typedef long double ld;

#ifdef WIN32
    #define I64 "%I64d"
#else
    #define I64 "%lld"
#endif // WIN32

const int inf = 1000000000;
const ll INF = 1LL*inf*inf;
const double eps = 1e-9;
const int MAXN = 2500;
const int md = (int)1e9 + 7;

string s;
int n, t, cnt[2000];

int main()
{
    //fast;
    out_files;
    scanf(I, &t);
    for (int w=1; w<=t; w++)
    {
        cin >> s;
        n = (int)s.length();
        for (int i=0; i<200; i++)
            cnt[i] = 0;
        for (int i=0; i<n; i++)
            cnt[s[i]]++;
        cnt[0] = cnt['Z'];
        cnt['Z'] -= cnt[0];
        cnt['E'] -= cnt[0];
        cnt['R'] -= cnt[0];
        cnt['O'] -= cnt[0];
        cnt[2] = cnt['W'];
        cnt['T'] -= cnt[2];
        cnt['W'] -= cnt[2];
        cnt['O'] -= cnt[2];
        cnt[6] = cnt['X'];
        cnt['S'] -= cnt[6];
        cnt['I'] -= cnt[6];
        cnt['X'] -= cnt[6];
        cnt[4] = cnt['U'];
        cnt['F'] -= cnt[4];
        cnt['O'] -= cnt[4];
        cnt['U'] -= cnt[4];
        cnt['R'] -= cnt[4];
        cnt[3] = cnt['R'];
        cnt['T'] -= cnt[3];
        cnt['H'] -= cnt[3];
        cnt['R'] -= cnt[3];
        cnt['E'] -= 2*cnt[3];
        cnt[8] = cnt['G'];
        cnt['E'] -= cnt[8];
        cnt['I'] -= cnt[8];
        cnt['G'] -= cnt[8];
        cnt['H'] -= cnt[8];
        cnt['T'] -= cnt[8];
        cnt[5] = cnt['F'];
        cnt['F'] -= cnt[5];
        cnt['I'] -= cnt[5];
        cnt['V'] -= cnt[5];
        cnt['E'] -= cnt[5];
        cnt[7] = cnt['S'];
        cnt['S'] -= cnt[7];
        cnt['E'] -= cnt[7];
        cnt['V'] -= cnt[7];
        cnt['E'] -= cnt[7];
        cnt['N'] -= cnt[7];
        cnt[9] = cnt['I'];
        cnt['N'] -= cnt[9];
        cnt['I'] -= cnt[9];
        cnt['N'] -= cnt[9];
        cnt['E'] -= cnt[9];
        cnt[1] = cnt['O'];
        printf("Case #%d: ", w);
        for (int i=0; i<10; i++)
            for (int j=0; j<cnt[i]; j++)
                cout << i;
        cout << "\n";
    }
    return 0;
}

