
#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_set>
#include <queue>
#include <stack>
#include <string>

#define FOR(i,b,e) for(int i=(b); i <= (e); ++i)
#define FORD(i,b,e) for(int i=(b); i >= (e); --i)
#define SIZE(c) (int) (c).size()
#define FORE(i,c) FOR(i,0,SIZE(c)-1)
#define FORDE(i,c) FORD(i,SIZE(c)-1,0)
#define MIN(x,y) ( ((x) < (y))? (x) : (y) )
#define MAX(x,y) ( ((x) > (y))? (x) : (y) )
#define PB push_back
#define MP make_pair
#define ST first
#define ND second
#define INF 1000000001

using namespace std;

typedef pair < int , int > PII;
typedef long long int LLI;

typedef vector < int > VI;
typedef vector < bool > VB;
typedef vector < PII > VP;
typedef vector < LLI > VL;

typedef vector < VI > VVI;
typedef vector < VL > VVL;
typedef vector < VB > VVB;

/*************************************************************************/

vector < string > split(string &text, char delim)
{
    vector < string > T(1);

    FORE(i,text)
    {
        if (text[i] == delim)
            T.push_back("");
        else
            T.back() += text[i];
    }

    while (T.size() && !T.back().size())
        T.pop_back();

    return T;
}

#define P 359
#define MOD 1000000007

int getHash(string &s)
{
    LLI ans = 0;

    FORE(i,s)
    {
        ans *= P;
        ans += s[i];
        ans %= MOD;
    }

    return ans;
}

/*************************************************************************/

void solve()
{
    int n;
    cin >> n;

    unordered_set < int > E, F;

    string s;
    getline(cin, s);

    FOR(i,0,1)
    {
        getline(cin, s);
        vector < string > V = split(s, ' ');

        FORE(j,V)
        {
            if (!i)
                E.insert( getHash(V[j]) );
            else
                F.insert( getHash(V[j]) );
        }
    }

    vector < vector < int > > S(n-2);

    FORE(i,S)
    {
        getline(cin, s);
        vector < string > temp = split(s, ' ');

        FORE(j,temp)
            S[i].PB( getHash(temp[j]) );
    }

    random_shuffle(S.begin(), S.end());

    int N = (1 << (n-2));
    int ans = INF;

    FOR(mask,0,N-1)
    {
        unordered_set < int > _E, _F;

        FORE(i,S)
        {
            if (mask & (1 << i))
            {
                FORE(j,S[i])
                    if (E.find(S[i][j]) == E.end())
                        _E.insert(S[i][j]);
            }
            else
            {
                FORE(j,S[i])
                    if (F.find(S[i][j]) == F.end())
                        _F.insert(S[i][j]);
            }
        }

        int here = 0;

        for (auto it = _E.begin(); it != _E.end(); it++)
        {
            if (_F.find(*it) != _F.end())
                here++;
            else if (F.find(*it) != F.end())
                here++;

            if (here >= ans)
                break;
        }

        for (auto it = _F.begin(); it != _F.end(); it++)
        {
            if (E.find(*it) != E.end())
                here++;

            if (here >= ans)
                break;
        }

        ans = min(ans, here);
    }

    for (auto it = E.begin(); it != E.end(); it++)
        if (F.find(*it) != F.end())
            ans++;

    cout << ans;
}

/*************************************************************************/

int main()
{
    ios_base::sync_with_stdio(0);

    int t;
    cin >> t;

    FOR(i,1,t)
    {
        cout << "Case #" << i << ": ";
        solve();

        cout << '\n';
    }

    return 0;
}

/*************************************************************************/
