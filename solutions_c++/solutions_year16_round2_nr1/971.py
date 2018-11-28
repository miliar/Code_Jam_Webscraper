#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp make_pair
#define F first
#define S second
#define sd(x) scanf("%d", &x)
#define sl(x) scanf("%lld", &x)
#define debug(X) cerr << " --> " << #X << " = " << X << endl
#define rep(i, begin, end) for(__typeof(end) i =(begin)-((begin)>(end));i!=(end)-((begin)>(end));i+=1-2*((begin)>(end)))
#define endl "\n"
typedef long long ll; typedef pair<int, int> pii;
const int N = 1123456, lgN = 15, mod = 1000000007;
const double eps = 1e-3, pi = acos(-1.0);
int c[26];
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("1.out", "w", stdout);

    int t;
    sd(t);
    for(int tt = 1; tt <= t ; ++tt)
    {
        printf("Case #%d: ", tt);
        string s;
        cin>>s;
        for(int i = 0; i < 26; ++i)
            c[i] = 0;
        for(int i = 0; i < s.size(); ++i)
            c[s[i] - 'A']++;
        string ans;
        while(c['Z' - 'A'] > 0)
        {
             c['Z' - 'A']--, c['E' - 'A']--,  c['R' - 'A']--, c['O' - 'A']--;
             ans += '0';
        }
        while(c['X' - 'A'] > 0)
        {
             c['S' - 'A']--,     c['I' - 'A']--,  c['X' - 'A']--;
             ans += '6';
        }
        while(c['U' - 'A'] > 0)
        {
             c['F' - 'A']--, c['O' - 'A']--,  c['U' - 'A']--, c['R' - 'A']--;
             ans += '4';
        }
        while(c['R' - 'A'] > 0)
        {
             c['T' - 'A']--, c['H' - 'A']--,  c['R' - 'A']--, c['E' - 'A'] -= 2;
             ans += '3';
        }
        while(c['F' - 'A'] > 0)
        {
             c['F' - 'A']--, c['I' - 'A']--,  c['V' - 'A']--, c['E' - 'A']--;
             ans += '5';
        }
        while(c['V' - 'A'] > 0)
        {
             c['S' - 'A']--, c['E' - 'A']--,  c['V' - 'A']--, c['E' - 'A']--, c['N' - 'A']--;
             ans += '7';
        }
        while(c['H' - 'A'] > 0)
        {
             c['E' - 'A']--, c['I' - 'A']--,  c['G' - 'A']--, c['H' - 'A']--, c['T' - 'A']--;
             ans += '8';
        }
        while(c['T' - 'A'] > 0)
        {
             c['T' - 'A']--, c['W' - 'A']--,  c['O' - 'A']--;
             ans += '2';
        }
        while(c['O' - 'A'] > 0)
        {
             c['O' - 'A']--, c['N' - 'A']--,  c['E' - 'A']--;
             ans += '1';
        }
        while(c['I' - 'A'] > 0)
        {
             c['N' - 'A'] -= 2, c['I' - 'A']--,  c['N' - 'A']--;
             ans += '9';
        }
        sort(ans.begin(), ans.end());
        cout<<ans<<"\n";
    }
    return 0;
}



