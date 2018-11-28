#include <bits/stdc++.h>

typedef long long ll;
using namespace std;

#define all(x) x.begin(), x.end()
#define f(i,a,b) for(int i = (a); i <= (b); i++)
#define fd(i,a,b) for(int i = (a); i >= (b); i--)
#define mp make_pair
#define faster_io() ios_base::sync_with_stdio(false)
#define pb push_back
#define pii pair<int,int>
#define SZ(x) ((int)x.size())
#define vii vector<pair<int,int>>

const int INF = 1000000005;
const ll INFLL = 100000000000000000ll;
const ll MOD = 1000000007;

ifstream fin("A.txt");
ofstream fout("A.out");

int N,T;

int main()
{
    fin >> T;

    f(t,1,T)
    {
        string s;
        fin >> N >> s;
        int acum = 0, ans = 0;
        f(i,0,N)
        {
            if(s[i] == '0') continue;
            int am = s[i] - '0';
            if(acum < i) ans += i - acum;
            acum = max(acum,i);
            acum += am;
        }
        fout << "Case #" << t << ": " << ans << "\n";
    }
}
